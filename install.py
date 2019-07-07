from sys import *
import platform
import os
import shutil


class Colors:
    if (platform.system() == "Windows"):
         ERROR = ''
         END = ''
         LOG_BLUE = ''
    else:
         ERROR = '\033[91m'
         END = '\033[0m'
         LOG_BLUE = '\033[94m'

venv = "venv"

if 'SUDO_UID' in os.environ.keys():
    answer = input(
        "You are about to install your virtualenv only for root, this is discouraged, are you sure ? (Y/N) If you are not sure relaunch the script without super user privileges\n")
    while (answer != 'Y' and answer != 'y' and answer != 'n' and answer != 'N'):
        answer = input(
            "You are about to install your virtualenv only for root, this is discouraged, are you sure ? (Y/N) \n")
    if (answer not in ['y', 'Y']):
        exit(1)


## deleting if already exist then creating the venv
#

while (True):
    try:
        if (os.path.isdir(venv)):
            print(
                Colors.LOG_BLUE + "-----------------------------Deleting existing venv-----------------------------" + Colors.END)
            shutil.rmtree(venv)
        break
    except:
        continue

#
## update of tools and installation of dependencies in REQUIREMENTS.txt or REQUIREMENTS_WINDOWS.txt
#

end_of_line = '\n\n'
python = 'python3'
pip = '/bin/pip'

REQUIREMENTS = 'REQUIREMENTS.txt'

if (platform.system() == "Windows"):
    end_of_line = "\r\n\r\n"
    python = 'py'
    pip = '\Scripts\pip'
    REQUIREMENTS = 'REQUIREMENTS_WINDOWS.txt'


print(
    Colors.LOG_BLUE + "-----------------------------Creating venv " + venv + "-----------------------------" + end_of_line + Colors.END)
os.system(python + " -m venv " + venv)
print(
    Colors.LOG_BLUE + "-----------------------------Installing python packages via pip-----------------------------" + Colors.END)
os.system(venv + '\Scripts\python -m pip install --upgrade pip')
os.system(venv + pip + ' install --upgrade wheel')
os.system(venv + pip + ' install --upgrade setuptools')
'''if (platform.system() == "Windows"):
    if (platform.machine() == "x86"):
        os.system(venv + '\Scripts\pip install ../install\windows\lxml-4.1.1-cp36-cp36m-win32.whl')
    else:
        os.system(venv + '\Scripts\pip install ../install\windows\lxml-4.1.1-cp36-cp36m-win_amd64.whl')'''
os.system(venv + pip + ' install -r' + REQUIREMENTS)


#
## creating database and creating and granting user pyros
#



print(
    Colors.LOG_BLUE + "\r\n\r\n-----------------------------Install successfull !-----------------------------" + Colors.END)

