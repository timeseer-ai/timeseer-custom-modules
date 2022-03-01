# timeseer-custom-modules

To build the executable,
create a venv
```
PS > python -m venv venv
```

Enter the virtual environment
```
PS > .\venv\Scripts\activate
(venv) PS >
```

Install cx-freeze and pyarrow to build the executable file.
```
(venv) $ pip install -r requirements.txt
```

and create the executable in a `build` folder:
```
(venv) $ python ./setup_binary.py build
```

The binary files are created in the `build` folder.
Copy all of them into your module_type folder in timeseer.