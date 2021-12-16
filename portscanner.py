#Simple Port Scanner because why not
#MrPanford

#All the imports, all the time.
import socket
import os
import subprocess
import sys
import colorama
from colorama import Fore, Style
from datetime import datetime


#clear screen
subprocess.call('clear', shell=True)

#Address Resolution Protocol prompt and code
arpin = input(Style.BRIGHT + "Would you like an ARP table? Yes or No: " + Style.RESET_ALL).lower()
if arpin == ("yes"):
	print("ARP table")
	print("-" * 60)
	arp = subprocess.run(['arp', '-a'])
	print(arp.returncode)
else:
	print(Style.DIM + "Bypassing ARP Table" + Style.RESET_ALL)

print("-" * 60)


#ip or host
print("Port Scanner")
print("-" * 60)
host = input("Please input a hostname, IP address: ")

#Information
print("-" * 60)
print(Style.BRIGHT + "Scanning..." + Style.RESET_ALL)
print("-" * 60)
#Date Time Block
time1 = datetime.now()

#Port Scan block, using sockets.
def scan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        print(Fore.GREEN + Style.BRIGHT + "Port open: " + str(port) + Style.RESET_ALL)
        s.close()
    except:
        pass
host
for port in range (1,65536):
    scan(host, port)

#Date Time Block 2
time2 = datetime.now()

#scan time
timevar = time2 - time1

#information
print(Style.BRIGHT + 'Scan Complete: ' + Style.RESET_ALL)
print(Style.BRIGHT + 'Scan Time:' + Style.RESET_ALL)
print(timevar)
print("-" * 60)
