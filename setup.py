from setuptools import setup

with open("README.rst", encoding="utf-8") as file:
    readme = file.read()

setup(
    name='kodi-control',
    version='0.1.0',
    description='interactive tty-based remote control for Kodi',
    long_description=readme,
    long_description_content_type='text/x-rst',
    scripts='kodi-control'.split(),
    install_requires='appdirs docopt inform nestedtext shlib voluptuous'.split(),
    python_requires = '>=3.6',
    keywords = 'kodi'.split(),
    classifiers = [
        #'Development Status :: 5 - Production/Stable',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
