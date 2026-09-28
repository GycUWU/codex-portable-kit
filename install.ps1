param([switch]$Mcp, [switch]$Plugins, [switch]$Preferences, [switch]$Video, [switch]$Runtimes)
$ErrorActionPreference = 'Stop'
$installArgs = @((Join-Path $PSScriptRoot 'scripts/install.py'))
foreach ($name in @('Mcp', 'Plugins', 'Preferences', 'Video', 'Runtimes')) {
    if ((Get-Variable -Name $name).Value) { $installArgs += ('--' + $name.ToLower()) }
}
if (Get-Command python -ErrorAction SilentlyContinue) {
    & python @installArgs
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 @installArgs
} else {
    throw '请先安装 Python 3.12，再重新打开终端。'
}
if ($LASTEXITCODE -ne 0) { throw ('安装失败，退出码：' + $LASTEXITCODE) }
