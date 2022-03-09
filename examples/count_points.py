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
