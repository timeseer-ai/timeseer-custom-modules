"""Boilerplate for a custom module."""

# SPDX-FileCopyrightText: 2022 Timeseer.AI
# SPDX-License-Identifier: Apache-2.0

from typing import Any

import pyarrow as pa


def get_capabilities() -> list[str]:
    """List the capabilities of the module."""
    return ["help", "metadata", "analyze"]


def get_help() -> str:
    """Return the help text for the module."""
    return ""


def get_metadata() -> dict[str, Any]:
    """Return the metadata of the module."""
    return {"signature": "univariate"}


# pylint:disable=unused-argument
def run_analysis(analysis_input: dict[str, Any], data: pa.Table) -> dict[str, Any]:
    """Run the analysis of the custom module.

    analysis_input contains the available input to run the analysis.
    Data can be found in the pyarrow Table: data.
    """

    # write code for the analysis to run.

    return {}
