# timeseer-custom-modules

## Create a custom module

Copy (or rename) the boilerplate `custom_module`.

Adjust the `main.py` file to import your new custom module,
Add it to the capabilities,
and make sure there is a check on the name (provided by the first argument of the request).

Write documentation in the `get_help` function, 
metadata of the check in the `get_metadata` function,
and the analysis in the `run_analysis` function.

More information can be found in the Timeseer admin documentation.

## Build an executable

To build the executable on windows,
create a venv
```
PS > python -m venv venv
```

Enter the virtual environment
```
PS > .\venv\Scripts\activate
(venv) PS >
```

Install the requirements to build the executable file.
```
(venv) PS > pip install -r requirements.txt
```

and create the executable in a `build` folder:
```
(venv) PS > python ./setup_binary.py build
```

The binary files are created in the `build` folder.
Copy all of the files into your `module_type` folder in timeseer.