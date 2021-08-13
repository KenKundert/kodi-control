from setuptools import setup

with open("README.rst", encoding="utf-8") as file:
    readme = file.read()

setup(
    name='kodi-control',
    version='0.0.0',
    description='interactive tty-based remote control for Kodi',
    long_description=readme,
    long_description_content_type='text/x-rst',
    scripts='kodi-control'.split(),
    install_requires='appdirs docopt inform nestedtext shlib voluptuous'.split(),
)
