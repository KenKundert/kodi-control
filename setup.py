from setuptools import setup

setup(
    name='kodi-control',
    version='0.0',
    description='interactive tty-based remote control for Kodi',
    scripts='kodi-control'.split(),
    install_requires='appdirs docopt inform nestedtext shlib voluptuous'.split(),
)
