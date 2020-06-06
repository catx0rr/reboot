#!/usr/bin/env python

''' 
    reboot.py -- Router reboot python script

    Telnet Protocol

    Disclaimer:
        For personal use only.
        For obfuscated password never store it in plaintext, use encoders.

'''

import sys

from telnetlib import Telnet
from time import sleep

# Change as per requirement

HOST = ''
PORT = '23'
USERNAME = ''
PASSWD = ''


def main():

    # Connect to HOST, PORT
    t = Telnet(HOST, PORT)

    # Telnet Login
    t.write((USERNAME + '\n').encode('utf-8'))

    t.write((PASSWD + '\n').encode('utf-8'))

    print('[+] Rebooting router..')

    # Command Execution
    t.write('reboot\n'.encode('utf-8'))

    t.write('exit\n'.encode('utf-8'))

    # Cancelable timeout 7 seconds
    for i in range(6):
        sleep(1)

    sys.exit()


if __name__ == '__main__':

    main()
