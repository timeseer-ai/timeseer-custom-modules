"""The main file. Executable is made from this file."""

import json
import sys

from pyarrow import feather

from custom_modules.custom_module import (
    get_capabilities,
    get_help,
    get_metadata,
    run_analysis,
)


def _return(data) -> None:
    sys.stdout.write(json.dumps(data))
    sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        _return({"custom_module": get_capabilities()})
    if sys.argv[1] == "custom_module":
        if sys.argv[2] == "help":
            _return(get_help())
        elif sys.argv[2] == "metadata":
            _return(get_metadata())
        elif sys.argv[2] == "analyze":
            analysis_input: dict = json.load(sys.stdin)
            data_table = feather.read_table(analysis_input["data"]["path"])
            _return(run_analysis(analysis_input, data_table))
