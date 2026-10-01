param(
    [Parameter(Mandatory = $true)]
    [string]$Pdf,

    [Parameter(Mandatory = $true)]
    [int]$PrimaPagina,

    [Parameter(Mandatory = $true)]
    [int]$UltimaPagina,

    [Parameter(Mandatory = $true)]
    [string]$CartellaOutput,

    [string]$Prefisso = "pagina",

    [int]$Dpi = 180
)

$ErrorActionPreference = "Stop"

if ($PrimaPagina -lt 1 -or $UltimaPagina -lt $PrimaPagina) {
    throw "Intervallo di pagine non valido: $PrimaPagina-$UltimaPagina"
}

$pdfRisolto = (Resolve-Path -LiteralPath $Pdf).Path
if ([System.IO.Path]::IsPathRooted($CartellaOutput)) {
    $outputRisolto = [System.IO.Path]::GetFullPath($CartellaOutput)
}
else {
    $outputRisolto = [System.IO.Path]::GetFullPath(
        (Join-Path -Path (Get-Location).Path -ChildPath $CartellaOutput)
    )
}
[System.IO.Directory]::CreateDirectory($outputRisolto) | Out-Null

$pdftoppm = (Get-Command pdftoppm -ErrorAction Stop).Source

Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime]
$null = [Windows.Storage.Streams.IRandomAccessStream, Windows.Storage.Streams, ContentType = WindowsRuntime]
$null = [Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType = WindowsRuntime]
$null = [Windows.Graphics.Imaging.SoftwareBitmap, Windows.Graphics.Imaging, ContentType = WindowsRuntime]
$null = [Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType = WindowsRuntime]
$null = [Windows.Media.Ocr.OcrResult, Windows.Foundation, ContentType = WindowsRuntime]

function Wait-WinRtOperation {
    param(
        [Parameter(Mandatory = $true)]
        $Operation,

        [Parameter(Mandatory = $true)]
        [Type]$ResultType
    )

    $method = (
        [System.WindowsRuntimeSystemExtensions].GetMethods() |
            Where-Object {
                $_.Name -eq "AsTask" -and
                $_.IsGenericMethod -and
                $_.GetParameters().Count -eq 1
            }
    )[0].MakeGenericMethod($ResultType)

    $task = $method.Invoke($null, @($Operation))
    $task.Wait()
    return $task.Result
}

$ocr = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
if ($null -eq $ocr) {
    throw "Il motore OCR di Windows non è disponibile."
}

$indice = [System.Collections.Generic.List[object]]::new()

for ($pagina = $PrimaPagina; $pagina -le $UltimaPagina; $pagina++) {
    $base = Join-Path $outputRisolto ("{0}-p{1:D3}" -f $Prefisso, $pagina)
    $png = "$base.png"
    $txt = "$base.txt"

    if (-not (Test-Path -LiteralPath $png)) {
        & $pdftoppm -f $pagina -l $pagina -r $Dpi -png -singlefile $pdfRisolto $base
        if ($LASTEXITCODE -ne 0) {
            throw "pdftoppm non riuscito sulla pagina fisica $pagina."
        }
    }

    $file = Wait-WinRtOperation (
        [Windows.Storage.StorageFile]::GetFileFromPathAsync($png)
    ) ([Windows.Storage.StorageFile])
    $stream = Wait-WinRtOperation (
        $file.OpenAsync([Windows.Storage.FileAccessMode]::Read)
    ) ([Windows.Storage.Streams.IRandomAccessStream])
    $decoder = Wait-WinRtOperation (
        [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)
    ) ([Windows.Graphics.Imaging.BitmapDecoder])
    $bitmap = Wait-WinRtOperation (
        $decoder.GetSoftwareBitmapAsync()
    ) ([Windows.Graphics.Imaging.SoftwareBitmap])
    $result = Wait-WinRtOperation (
        $ocr.RecognizeAsync($bitmap)
    ) ([Windows.Media.Ocr.OcrResult])

    [System.IO.File]::WriteAllText(
        $txt,
        $result.Text,
        [System.Text.UTF8Encoding]::new($true)
    )

    $indice.Add([pscustomobject]@{
        pagina_fisica = $pagina
        immagine = [System.IO.Path]::GetFileName($png)
        testo_ocr = [System.IO.Path]::GetFileName($txt)
        caratteri_ocr = $result.Text.Length
    })

    $stream.Dispose()
}

$csv = Join-Path $outputRisolto ("{0}-indice-ocr.csv" -f $Prefisso)
$indice | Export-Csv -LiteralPath $csv -Delimiter ";" -NoTypeInformation -Encoding UTF8

Write-Output ("OCR completato: pagine {0}-{1}, output {2}" -f $PrimaPagina, $UltimaPagina, $outputRisolto)
