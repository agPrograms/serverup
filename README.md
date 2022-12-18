# serverup

Check the status of a program/server and send a message to a Discord channel via POST Method & Webhooks.

## Purpose

The purpose of this tool is quite literally just to check a program task and send a message based on conditions (True/False). Specifically, *I made this tool look for a Minecraft Server that is running on Windows Server.* It really isn't much, but it gets the job done. Use it how ever you please! I made it for myself, but I am always willing to share my weird projects..

## Prerequisites

- Microsoft Windows OS (Server, Pro, etc.)
- [Minecraft Server](https://www.minecraft.net/en-us/download/server) (Forge, Vanilla, Spigot, etc.) -- Link takes you to vanilla.
- [Python](https://www.python.org/), ([pyinstaller package/tool](https://pypi.org/project/pyinstaller/) optional!)

## Install/Usage

**Note: This is a Windows-focused tool. It will not work on Linux/UNIX enviorments, EVEN EMULATORS LIKE WINE!**
1. Download the serverup-public.py python file and edit the ``'webhook_url'`` and ``'mc'`` variables to match your discord webhook and process you want to check the condition of.
2. Save your changes, and utilize python to execute the file via the CMD: ``python3 serverup-public.py`` or you can compile it to a Windows Executable (.exe) by using the *[pyinstaller](https://pypi.org/project/pyinstaller/)* package.
3. Enjoy!
