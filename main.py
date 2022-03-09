"""The custom module executable entry point."""

# SPDX-FileCopyrightText: 2022 Timeseer.AI
# SPDX-License-Identifier: Apache-2.0

import json
import sys

from pyarrow import feather

# Import custom modules here
from custom_modules import my_module

# Add them to this dictionary
modules = {
    "my_module_name": my_module,
}


def _return(data) -> None:
    sys.stdout.write(json.dumps(data))
    sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        _return({name: module.get_capabilities() for name, module in modules.items()})
    if sys.argv[1] in modules:
        module = modules[sys.argv[1]]
        if sys.argv[2] == "help":
            _return(module.get_help())
        elif sys.argv[2] == "metadata":
            _return(module.get_metadata())
        elif sys.argv[2] == "analyze":
            analysis_input: dict = json.load(sys.stdin)
            data_table = feather.read_table(analysis_input["data"]["path"])
            _return(module.run_analysis(analysis_input, data_table))
