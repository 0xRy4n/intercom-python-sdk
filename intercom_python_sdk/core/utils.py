"""
# Common Utilities

`core/utils.py`

Contains various utility functions used throughout the SDK.
"""
import importlib
import os

def _import_classes_from_files(directory, filename):
    """ Recursively searches a directory for files with a given name, and imports all classes from them."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == filename:
                file_path = os.path.join(root, file)
                module_name = os.path.splitext(file)[0]
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                for name, obj in module.__dict__.items():
                    if isinstance(obj, type):
                        globals()[name] = obj