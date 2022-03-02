"""Boilerplate for a custom module."""

from typing import Any
import pyarrow as pa


def get_capabilities() -> list[str]:
    """Get the capabilities of the module."""
    return ["help", "metadata", "analyze"]


def get_help() -> str:
    """Get the documentation of the module."""
    return ""


def get_metadata() -> dict[str, Any]:
    """Get the metadata of the module."""
    return {"signature": "univariate"}


# pylint:disable=unused-argument
def run_analysis(
    analysis_input: dict[str, Any], data_table: pa.Table
) -> dict[str, Any]:
    """Run the analysis of the custom module.

    analysis_input contains the available input to run the analysis.
    Data can be found in the pyarrow table: data_table.
    """

    # write code for the analysis to run.

    return {}
