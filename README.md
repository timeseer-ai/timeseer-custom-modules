# timeseer-custom-modules

This repository contains a blueprint for writing custom analysis modules in Timeseer on Windows using Python.

## Getting started

Fork,
checkout or download an archive containing this repository to get started.

Ensure [uv](https://docs.astral.sh/uv/) is available.

This blueprint uses [cx_Freeze](https://cx-freeze.readthedocs.io/en/latest/) to transform the Python scripts in an executable.

Some dependencies to ensure a clean coding style are available:

```PowerShell
PS > uv run ruff format
PS > uv run ruff check
PS > uv run mypy
```

Build the executable using:

```PowerShell
PS > uv run cxfreeze
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

Format all code using [ruff](https://docs.astral.sh/ruff/):

```PowerShell
PS > uv run ruff format
```

[Lint](https://docs.astral.sh/ruff/) and [typecheck](http://mypy-lang.org/) the code:

```PowerShell
PS > uv run ruff check
PS > uv run mypy --ignore-missing-imports .\custom_modules\
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

## Testing in a container image

Once built,
the module can be mounted in a container image and tested.

This example works after building the example above on Linux (`uv run cxfreeze build_exe`).

```bash
docker run \
    --rm \
    -u $(id -u) \
    -v $PWD/examples/Timeseer.toml:/usr/src/app/Timeseer.toml \
    -v $PWD/db:/usr/src/app/db \
    -v $PWD/build/exe.linux-x86_64-3.12/:/usr/src/app/library/analysis/custom_modules/count \
    -p 8080:8080 \
    -it container.timeseer.ai/timeseer:latest
```

Adapt the module name as required.

## GitHub Actions

This project contains a [GitHub Action](https://github.com/features/actions) that automatically builds and zips the executable and its supporting files.

Fork this repository or adapt the [workflow](.github/workflows/ci.yml) to another CI system.

## Contributing

Feel free to fork this project.
We welcome pull requests,
but consider opening an issue to discuss significant changes upfront.
