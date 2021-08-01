#!/usr/bin/python3.9

# Made by @lim3ck@
#Vulnerability Scanner that will display all vulns for a single IP under multiple ports:
# e.g: 
# Enter target IP: 192.168.0.100
# Enter the nr of ports to scan: 6000
#         [+] 192.168.0.100/21: ......Vulnerability name you can search for exploits......
#         [+] 192.168.0.100/22: ......Vulnerability name you can search for exploits......
#         [+] 192.168.0.100/5900: ......Vulnerability name you can search for exploits......

import socket
from termcolor import colored

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)   # change the <1024> argument if you think there will be a longer vuln name
        return banner
    except:
        return 

def main():
    ip = input(" Enter target IP: ")
    portRange= input(" Enter the nr of ports to scan: ")
    for port in range(1,int(portRange)+1):
        banner =retBanner(ip,port)
        if banner:
            print(colored("\t [+] " + str(ip) + "/" + str(port)+ ": "+ str(banner),'green'))

main()