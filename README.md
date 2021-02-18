# DarkU
![License](https://img.shields.io/github/license/vincent-coding/darku?style=for-the-badge) ![100% Python](https://img.shields.io/github/languages/top/vincent-coding/darku?style=for-the-badge) ![Downloads](https://img.shields.io/github/downloads/vincent-coding/darku/total?style=for-the-badge) ![Stars](https://img.shields.io/github/stars/vincent-coding/DarkU.svg?style=for-the-badge&label=Stars)
![Python 3.8 and newer](https://img.shields.io/badge/Python-3.8%20and%20newer%20-informational?style=for-the-badge&logo=python)
<br />
DarkU is a software developed in Python by vincent-coding, with the help of TnT GuN. Its purpose is to temporarily change the background of your wiiu.

**WARNING:** From version 2.2 onwards, the software is licensed under the _GPL-3.0_, older versions of DarkU remain under the _Apache 2.0_ license.

## What are the colors available in DarkU?
For the moment it's just shades of grey, but its creator is looking to be able to put other colors.
-   Default
-   White
-   Light grey
-   Grey
-   Dark grey
-   Very dark grey
-   Black

## Pictures?
This is what the software looks like since version 2.2.
![](https://i.imgur.com/6CncFnz.png)<br />
<br />
Here is the result on the WiiU for the grey colour.
![Example](https://i.imgur.com/jdfWh88.jpg)

## Library used
### Version 2.2 or newer
**Please be careful when installing these modules. They must be installed for Python 3.8 or newer!**
- **PyQt5** (*Required)*<br />
PyQt5 is the module that creates the graphical interface. If this module is not installed, the program will never run!<br />
To install it simply use the pip package manager.<br />
If you only have one version of Python 3 and that version is 3.8 or newer:<br />
`pip3 install pyqt5`<br />
Else:
`pip3.8 install pyqt5`

- **PyPresence** (*Not obligatory but recommended*)<br />
PyPresence is a library to display a status on Discord.<br />
To install it simply use the pip package manager.<br />
If you only have one version of Python 3 and that version is 3.8 or newer:<br />
`pip3 install pypresence`<br />
Else:
`pip3.8 install pypresence`

- **PyGecko**<br />
This library is already provided with the program ~~but if you wish you can install the module version available [here](https://github.com/vincent-coding/pyGecko/tree/master/Python%20Code/TCPGecko/Module%20Version)~~. **The module version is no longer updated, it is still possible to use it but we strongly advise against it!**

### Version lower than 2.2
- **Tkinter**<br />
Tkinter allows to create all the interface of the software.<br />
It is often installed with python, but just in case here is the command to install it.<br />
Windows: `py -3 -m pip install tkinter` or `pip install tkinter`<br />
Linux: `sudo apt-get install python3-tk`<br />

- **PyPresence**<br />
PyPresence is a library to display a status on Discord.<br />
Windows: `pip install pypresence`<br />
Linux: `pip3 install pypresence`<br />

- **PyGecko**<br />
This library is already installed in the software.

## Launch the software
- **Version 2.2 or newer**
These versions are only compatible from **python 3.8** onwards!
To launch the software, simply use the following command:<br />
```
python3 DarkU.py
```

- **Version lower than 2.2**<br />
This version is compatible with **all versions of Python 3**.<br />
To launch the software, simply use the following command:<br />
```
python3 Main.py
```

## Feedback
If you encounter a problem or have a suggestion, just go to the GBAtemp page and write on the topic page, available [here](https://gbatemp.net/threads/release-darku.535159/).<br />
You can also send me a private message on Discord: **VCoding#4488**