#!/usr/bin/python2.7

# Vulnerability Scanner
# Arguments to pass: The filname that contains the vulnerabilities that we want to know

import socket
import os
import sys
#from termcolor import colored


class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
 

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(3)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return 

def checkVulns(banner, filename):
    f = open(filename,"r")
    for line in f.readlines():
        if line in str(banner):
            print(bcolors.OKGREEN + "\t[+] Server is vulnerable: " + str(banner))
            continue

def main():
    if len(sys.argv)==2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("[-] File doesn't exist! ")
            exit(0)
        if not os.access(filename,os.R_OK):
            print("[-] Access denied.. ")
            exit(0)
    else:
        print("[-] Usage " + str(sys.argv[0]) +" <vuln filname>")
        exit(0)
    portlist = [21,22,25,80,110,443,445]
    for x in range(100,101):
        ip = "192.168.0." + str(x)
        print(bcolors.WARNING + "Scann for "+ ip+": \n")
        for port in portlist:
            banner = retBanner(ip,port)
            if banner:
                checkVulns(banner, filename)

main()
