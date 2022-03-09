$ErrorActionPreference = "Stop"

black --check .\main.py .\custom_modules\
if (-not $?) {
    throw "Build failure"
}
pylint --disable=duplicate-code .\custom_modules\
if (-not $?) {
    throw "Build failure"
}
mypy --ignore-missing-imports .\custom_modules\
if (-not $?) {
    throw "Build failure"
}
Remove-Item .\build\ -Recurse -ErrorAction Ignore
python setup.py build
if (-not $?) {
    throw "Build failure"
}
