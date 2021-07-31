#!/usr/bin/python2.7

# Vulnerability Scanner
# Arguments to pass: The filname that contains the vulnerabilities
# that we search for and the IP range of the network
# ex ./vulnerabiliyScan.py vulnerabilities.txt  102-105 21,22,23,25


import socket
import os
import sys

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

def main():
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("[-] File doesn't exist! ")
            exit(0) 
        if not os.access(filename,os.R_OK):
            print("[-] Access denied.. ")
            exit(0)
    elif len(sys.argv)== 2:
        print("[-] No IP range specified.. ")
        exit(0) 
    elif len(sys.argv)== 3:
        print("[-] No port list specified.. ")
        exit(0)
    else:
        print("[-] Usage " + str(sys.argv[0]) +" <vuln filname>"+ " <IP range separated by \"-\"> <target ports separated by comma>")
        exit(0)

    portlist = str(sys.argv[3]).split(',')
    for i in range(0, len(portlist)):
        portlist[i] = int(portlist[i])

    ipRange = str(sys.argv[2]).split('-')
    for x in range(int(ipRange[0]),int(ipRange[1])):
        ip = "192.168.0." + str(x)      # You can change the network here
        print(bcolors.WARNING + "\nScann for " + ip+": ")
        ok=0
        for port in portlist:
            banner = retBanner(ip,port)
            if banner:
                checkVulns(banner, filename)
                ok = ok +1
        if ok == 0:
            print(bcolors.FAIL + "[-] No vulnerabilities found.. " )    

main()
