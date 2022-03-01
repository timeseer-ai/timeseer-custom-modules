#!/bin/sh

import json
import sys

from custom_modules.custom_module import get_capabilities, get_help, get_metadata, run_analysis

def _return(data) -> None:
    sys.stdout.write(json.dumps(data))
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        _return(get_capabilities())
    if sys.argv[1] == "help":
        _return(get_help())
    elif sys.argv[1] == "metadata":
        _return(get_metadata())
    elif sys.argv[1] == "analyze":
        analysis_input: dict = json.load(sys.stdin)
        _return(run_analysis(analysis_input))
