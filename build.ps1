$ErrorActionPreference = "Stop"

uv run ruff format --check
if (-not $?) {
    throw "Build failure"
}
uv run ruff check
if (-not $?) {
    throw "Build failure"
}
uv run mypy --ignore-missing-imports .\custom_modules\
if (-not $?) {
    throw "Build failure"
}
Remove-Item .\build\ -Recurse -ErrorAction Ignore
uv run cxfreeze build_exe
if (-not $?) {
    throw "Build failure"
}
