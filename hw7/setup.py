from setuptools import setup

setup(
    name ='clean-folder',
    version = '0.0.1',
    entry_points = {
        'clean_folder' : ['clean-folder=clean_folder.clean:main'],
    },
    
)