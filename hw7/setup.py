from setuptools import setup, find_packages

setup(
    name="clean-folder",
    version="0.0.1",
    entry_points={
        "console_scripts": ["clean-folder=clean_folder.clean:my_func"],
    },
    packages=find_packages(),
)