from setuptools import setup, find_packages

setup(
    name ="clean-folder",
    version = "0.0.1",
    entry_points = {
        "console_scripts" : ["clean-folder=console_script.my_cod:my_func"],
        },
    packages = find_packages(),
)