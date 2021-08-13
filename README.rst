Kodi Control — Interactive TTY-based remote control for Kodi
============================================================

.. image:: https://pepy.tech/badge/kodi-control/month
    :target: https://pepy.tech/project/kodi-control

..  image:: https://github.com/KenKundert//kodi-controlactions/workflows/build.yaml/badge.svg
    :target: https://github.com/KenKundert/kodi-control/actions/workflows/build.yaml

.. image:: https://coveralls.io/repos/github/KenKundert/kodi-control/badge.svg?branch=master
    :target: https://coveralls.io/github/KenKundert/kodi-control?branch=master

.. image:: https://img.shields.io/pypi/v/kodi-control.svg
    :target: https://pypi.python.org/pypi/kodi-control

.. image:: https://img.shields.io/pypi/pyversions/kodi-control.svg
    :target: https://pypi.python.org/pypi/kodi-control/

:Author: Ken Kundert
:Version: 0.0.0
:Released: 2021-08-12

*Kodi Control* can be used to control a running instance of *Kodi* from 
a terminal.  You can use it to interactively control the app and the players by 
opening a terminal and typing individual characters to perform various actions.

Getting Started
---------------

Install using::

    pip3 install --user kodi-control

Then, you need to create a file containing the settings.  In 
~/.config/kodi-control/settings.nt (a `NestedText <https://nestedtext.org>` 
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
While there you can add a username and password if desired.

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
         : toggle play/pause       >: forward 90 seconds      f: forward 30 seconds
        ': literal pass through    H: go to to home screen    h: move left
        ,: backward 10 seconds     K: kill player             i: show info
        .: forward 10 seconds      M: temporary mute          j: move down
        0: go to 0%                P: toggle player on top    k: move up
        1: go to 10%               S: start player            l: move right
        2: go to 20%               T: show subtitles          m: toggle mute
        3: go to 30%               [: go to start             n: toggle navigation
        4: go to 40%               ]: go to end               p: toggle play/pause
        5: go to 50%               b: backward 30 seconds     t: hide subtitles
        6: go to 60%               bs: go back                u: volume up
        7: go to 70%               c: context menu            x: stop
        8: go to 80%               d: volume down
        9: go to 90%               ent: select
        <: backward 90 seconds     esc: go to to home screen

As it starts, it immediately prints a list of available commands.  Then you 
simply type individual characters to run the available commands.
