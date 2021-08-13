Kodi Control — Interactive TTY-based remote control for Kodi
============================================================

.. image:: https://pepy.tech/badge/kodi-control/month
    :target: https://pepy.tech/project/kodi-control

.. ignore:

    ..  image:: https://github.com/KenKundert/kodi-control/actions/workflows/build.yaml/badge.svg
        :target: https://github.com/KenKundert/kodi-control/actions/workflows/build.yaml

    .. image:: https://coveralls.io/repos/github/KenKundert/kodi-control/badge.svg?branch=master
        :target: https://coveralls.io/github/KenKundert/kodi-control?branch=master

.. image:: https://img.shields.io/pypi/v/kodi-control.svg
    :target: https://pypi.python.org/pypi/kodi-control

.. image:: https://img.shields.io/pypi/pyversions/kodi-control.svg
    :target: https://pypi.python.org/pypi/kodi-control/

:Author: Ken Kundert
:Version: 0.1.0
:Released: 2021-08-13

*Kodi Control* can be used to control a running instance of *Kodi* from 
a terminal.  You can use it to interactively control the app and the players by 
opening a terminal and typing individual characters to perform various actions.

Getting Started
---------------

Install using::

    pip3 install --user kodi-control

Then, you need to create a file containing the settings.  In 
~/.config/kodi-control/settings.nt (a `NestedText <https://nestedtext.org>`_ 
file) that takes the following form::

    hostname: localhost
    port: 8080
    username: kodi
    password: password

All the values are optional with the defaults shown (except for password which 
is empty by default).

Before using *Kodi Control* you must first enable the JSONRPC over HTTP 
interface.  To do so, open *Kodi* and navigate to 
*Settings*→*Services*→*Control* and enable "Allow remote control via HTTP".  
While there you can add a username and password if desired.  Do not enable SSL.

You can run *Kodi Control* on a different from the one that runs *Kodi*, you 
just need to give the hostname for the machine that is running *Kodi*, and of 
course that machine must be accessible over the network from the machine running 
*Kodi Control*.  In this case, some functionality, such as volume control, is 
not available.  Alternately, *Kodi* can be run locally or you can open an SSH 
terminal and run *Kodi Control* on the *Kodi* host.  In this case all 
functionality is available.

However you choose to do it, you would start *Kodi Control* in a terminal::

    > kodi-control
    Enter desired actions, use 'q' to terminate.
         : toggle play/pause       ENT: select                h: move left
        ': literal text            ESC: go to to home screen  i: show info
        0: go to 0%                H: go to to home screen    j: move down
        1: go to 10%               K: kill player             k: move up
        2: go to 20%               M: temporary mute          l: move right
        3: go to 30%               P: toggle player on top    m: toggle mute
        4: go to 40%               S: start player            n: toggle navigation
        5: go to 50%               T: show subtitles          p: toggle play/pause
        6: go to 60%               b: skip backward           s: go to start
        7: go to 70%               c: context menu            t: hide subtitles
        8: go to 80%               d: volume down             u: volume up
        9: go to 90%               e: go to end               x: stop
        BS: go back                f: skip forward

As it starts, it immediately prints a list of available commands.  Then you 
simply type individual characters to run the available commands.
