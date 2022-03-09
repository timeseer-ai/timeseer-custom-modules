# timeseer-custom-modules

This repository contains a blueprint for writing custom analysis modules in Timeseer on Windows using Python.

## Getting started

Fork,
checkout or download an archive containing this repository to get started.

This guide uses Windows PowerShell,
but the traditional Command Prompt could be used as well.

First,
create a [virtualenv](https://docs.python.org/3/tutorial/venv.html):

```PowerShell
PS > python -m venv venv
```

Then,
activate the virtualenv:

```PowerShell
PS > .\venv\Scripts\activate
```

Depending on the security settings inside PowerShell,
the [ExecutionPolicy](https:/go.microsoft.com/fwlink/?LinkID=135170) needs to be updated.

To do this for the current process only,
run:

```PowerShell
PS > Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose
you to the security risks described in the about_Execution_Policies help topic at
https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): Y
```

If this operation is not allowed,
revert to Command Prompt and run:

```
>.\venv\Scripts\activate
```

Successful activation of the virtualenv will be indicated by a change in the shell prompt:

```PowerShell
(venv) PS >
```

or

```
(venv) >
```

This blueprint uses [cx_Freeze](https://cx-freeze.readthedocs.io/en/latest/) to transform the Python scripts in a Windows executable.
It also includes some tools to enforce coding style best practices.
Install them with `pip`:

```PowerShell
(venv) PS > pip install -r requirements.txt
```

Test building an executable:

```PowerShell
(venv) PS > python setup.py build
```

The executable can be found under `build/exe.win-amd64-3.<minor Python version>`.

Open **a new shell**,
navigate there and test it:

```PowerShell
PS build\exe.win-amd64-3.9> .\custom_modules.exe
{"my_module_name": ["help", "metadata", "analyze"]}
```

## Creating a custom module

Let's build a custom module that returns a statistic for the number of data points that have been analyzed for a time series.

Start off by making a copy of `custom_modules/my_module.py`,
for example `custom_modules/count_points.py`.

Include the module in `main.py`:

```python
# Import custom modules here
from custom_modules import count_points, my_module

# Add them to this dictionary
modules = {
    "count_points": count_points,
    "my_module_name": my_module,
}
```

Feel free to remove the existing dummy module:

```python
# Import custom modules here
from custom_modules import count_points

# Add them to this dictionary
modules = {
    "count_points": count_points,
}
```

The next step is implementing the functionality of the module.

Write a help text,
complete the metadata of the module and return the statistic.

Exhaustive reference documentation for any input and output JSON objects is available inside Timeseer (`Help` - `Admin documentation`).

The end result could be:

```python
"""Count the number of data points that have been analyzed."""

from typing import Any

import pyarrow as pa


def get_capabilities() -> list[str]:
    """List the capabilities of the module."""
    return ["help", "metadata", "analyze"]


def get_help() -> str:
    """Return the help text for the module."""
    return "The number of data points that have been analyzed for this series. "


def get_metadata() -> dict[str, Any]:
    """Return the metadata of the module."""
    return {"signature": "univariate"}


def run_analysis(_: dict[str, Any], data: pa.Table) -> dict[str, Any]:
    """Count the number of data points in the given data table."""

    statistics = [
        dict(name="Number of data points", dataType="float", result=len(data))
    ]

    return dict(statistics=statistics)
```

Note that `main.py` already loads the data into an [Apache Arrow](https://arrow.apache.org/docs/python/index.html) table.

Format all code using [black](https://github.com/psf/black):

```PowerShell
PS > black .\main.py .\custom_modules\
```

[Lint](https://pylint.org/) and [typecheck](http://mypy-lang.org/) the code:

```PowerShell
PS > pylint --disable=duplicate-code .\custom_modules\
PS > mypy --ignore-missing-imports .\custom_modules\
```

Remove the `build/` directory if it exists.
Then build the executable:

```PowerShell
PS > python setup.py build
```

Open a new shell,
then go to `build/exe.win-amd64-3.<Minor Python version>`.
Verify the executable:

```PowerShell
PS > .\custom_modules.exe
{"count_points": ["help", "metadata", "analyze"]}
```

## Deploying the custom module

Timeseer searches for custom modules in the `library` path.
Subdirectories give structure to the module collection.

Let's assume we would like to have the modules we defined available in Timeseer in the group `Custom statistics`.
To do so, create `library/analysis/custom_statistics` relative to the `timeseer.exe` executable.
Only the last segment of this path can be freely chosen,
the first two are required to be `library/analysis`.

It would now be possible to just copy over **all** files in `build/exe.win-amd64-3.<Minor Python version>` to that directory,
but to allow adding other modules later on,
developed in a separate project,
create another subdirectory: `library/analysis/custom_statistics/custom_modules`.

## GitHub Actions

This project contains a [GitHub Action](https://github.com/features/actions) that automatically builds and zips the executable and its supporting files.

Fork this repository or adapt the [workflow](.github/workflows/ci.yml) to another CI system.

## Contributing

Feel free to fork this project.
We welcome pull requests,
but consider opening an issue to discuss significant changes upfront.
