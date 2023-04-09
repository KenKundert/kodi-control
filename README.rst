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
:Version: 1.0
:Released: 2023-04-08

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
interface.  To do so, open *Kodi* and navigate to *Settings* → *Services* 
→ *Control* and enable "Allow remote control via HTTP".  While there you can add 
a username and password if desired.  Do not enable SSL.

You can run *Kodi Control* on a host different from the one that runs *Kodi*, 
you just need to give the hostname for the machine that is running *Kodi*, and 
of course that machine must be accessible over the network from the machine 
running *Kodi Control*.  In this case, some functionality, such as volume 
control and starting and killing *Kodi*, is not available.  Alternately, *Kodi* 
can be run locally (best with two screens) or you can open an SSH terminal and 
run *Kodi Control* on the *Kodi* host.  In this case all functionality is 
available.  To control a remote *Kodi* while using an SSH terminal, you must 
specify the name of your display in your ``settings.nt`` file.  The typical 
value is ``:0`` or ``:0``, but you can examine your DISPLAY environment variable 
and specify whatever it contains::

    display: :0

However you choose to do it, you would start *Kodi Control* in a terminal::

    > kodi-control
    Enter desired actions, use 'q' to terminate.

    Navigation Keys:
        BS: go back                h: move left
        ENT: select                j: move down
        ESC: go to to home screen  k: move up
        H: go to to home screen    l: move right
        c: context menu

    Player Keys:
         : toggle play/pause     7: go to 70%             i: show info
        0: go to 0%              8: go to 80%             n: toggle navigation
        1: go to 10%             9: go to 90%             p: toggle play/pause
        2: go to 20%             P: toggle player on top  s: go to start
        3: go to 30%             T: show subtitles        t: hide subtitles
        4: go to 40%             b: skip backward         x: stop player
        5: go to 50%             e: go to end
        6: go to 60%             f: skip forward

    Sound Keys:
        M: temporary mute  m: toggle mute
        d: volume down     u: volume up

    Kodi Keys:
        ': enter text  K: kill kodi   S: start kodi

As it starts, it immediately prints a list of available actions.  Then you 
simply type individual characters to run the desired action.

The temporary mute action (``M``) engages mute for settable number of seconds.  
This can be used to turn off the sound during commercials.  Once engaged you 
will see a count down with the sound being re-enabled when the count reaches 0.  
During the interim all input is ignore except ``ctrl-C`` which immediately 
terminates the count-down and immediately re-activates the sound.  You can 
specify the duration of the temporary mute with the following setting::

    temporary mute duration: 30

You can specify the path to the *Kodi* executable in your settings file::

    kodi: kodi-standalone

``kodi`` holds the command used to start *Kodi*.  It can be just the command 
name, in which case it must be on your path, or it can be the full path to the 
command.  By default it is simply *kodi*.

Older versions of *Kodi* have a bug that interferes with proper operation of 
forward seeks of less than 60 seconds.  *Kodi Control* works around this issue 
if you specify the version number of *Kodi* in the settings file::

    kodi version: 18.7

Currently, the workaround is disabled if the version is 19 or later.

If you have any trouble, you can enable the log file and examine it for clues.  
To enable the log file, add the following to your settings file::

    log: yes

The log file can then be found at ``~/.local/share/kodi-control/log``.

Feel free to post questions or bug report to `GitHub Issues 
<https://github.com/KenKundert/kodi-control/issues>`_.
