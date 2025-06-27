#!/usr/bin/python3
import importlib.util
import sys

if __name__ == "__main__":
    # Load the compiled module from hidden_4.pyc
    spec = importlib.util.spec_from_file_location(
        "hidden_4", "hidden_4.pyc"
    )
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get all attributes of the module
    names = dir(hidden_4)

    # Filter out names starting with '__' and sort alphabetically
    filtered_names = sorted(
        name for name in names if not name.startswith("__")
    )

    # Print each name on a separate line
    for name in filtered_names:
        print(name)
