from subprocess import check_call
from sys import platform

def copy(answer): # copy to clipboard
    cmd = ('echo "{0}"|clip'.format(answer.strip())) if platform == "Windows" else ('echo "{0}"|pbcopy'.format(answer.strip()))
    return check_call(cmd, shell=True)