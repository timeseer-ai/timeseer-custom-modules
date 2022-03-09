"""Create a Windows executable."""

import os

from cx_Freeze import setup, Executable

executables = [
    Executable(
        'main.py',
        target_name='custom_modules.exe',
    ),
]


setup(
    name="Custom modules",
    version="0.0.0",
    description="Custom modules for Timeseer.AI",
    executables=executables,
    options={
        "build_exe": {
            "excludes": [
                "unittest",
                "mypy",
                "mypy_extensions",
                "numpy.testing",
                "setuptools",
                "tkinter",
                "typing_extensions",
            ],
            "replace_paths": [(os.getcwd(), "")],
        },
    },
)
