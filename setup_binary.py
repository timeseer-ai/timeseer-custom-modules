"""Create Windows executables."""

import os

from cx_Freeze import setup, Executable

executables = [
    Executable(
        'main.py',
        target_name='custom_modules.exe',
    ),
]


setup(
    name="Custom module",
    version="0.0.0",
    description="Custom modules",
    executables=executables,
    options={
        "build_exe": {
            "include_files": [
                ('custom_modules', 'custom_modules'),
            ],
            "replace_paths": [(os.getcwd(), "")],
        },
    },
)
