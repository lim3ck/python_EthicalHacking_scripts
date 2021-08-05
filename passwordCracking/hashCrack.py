#!/usr/bin/python3.9

# Made by @lim3ck@
# Simple hash cracker for usual encryption methods: md5, sha1, sha224, sha256, sha512, crypt(salt)
# Arguments to pass: the hash type, the hash value and the dictionary where you want to search
# e.g:
'''
[*] Enter the hash type you want to decode (md5/sha1/sha224/sha256/sha512/crypt): sha256
[*] Enter hash value: 6382deaf1f5dc6e792b76db4a4a7bf2ba468884e000b25e7928e621e27fb23cb
[*] Enter the path of password dictionary: password.txt
[*] Trying: admin
    [+] Password found: football
'''


import hashlib
from termcolor import colored
import crypt

def comp(hashVal,hashType,passw):
    enc_pass = passw.encode('utf-8')
    if hashType == "md5":
        digest = hashlib.md5(enc_pass.strip()).hexdigest()
        if digest == hashVal:
            return True
        else:
            return False
    elif hashType == "sha1":
        digest = hashlib.sha1(enc_pass.strip()).hexdigest()
        if digest == hashVal:
            return True
        else:
            return False
    elif hashType == "sha224":
        digest = hashlib.sha224(enc_pass.strip()).hexdigest()
        if digest == hashVal:
            return True
        else:
            return False
    elif hashType== "sha256":
        digest = hashlib.sha256(enc_pass.strip()).hexdigest()
        if digest == hashVal:
            return True
        else:
            return False
    elif hashType == "sha512":
        digest = hashlib.sha512(enc_pass.strip()).hexdigest()
        if digest == hashVal:
            return True
        else:
            return False
    elif hashType == "crypt":
        salt = hashVal[0:2]
        cryptPass = crypt.crypt(passw, salt)
        if hashVal == cryptPass:
            return True
        else:
            return False

def crackPass(hashVal,hashType,dictionary):
    
    try:
        pass_file = open(dictionary,"r")
    except:
        print("[!!] No such file at the path.. ")
        quit()
    
    for passw in pass_file:
        print(colored("[*] Trying: " + passw.strip("\n"),'red'))
        if comp(hashVal,hashType,passw):
            print(colored("\t[+] Password found: "+ passw, 'green'))
            exit(0)
    print(colored("[!!] Password not in list",'yellow'))


hashType = input("[*] Enter the hash type you want to decode (md5/sha1/sha224/sha256/sha512/crypt): ")
hashvalue = input("[*] Enter hash value: ")
fileName = input("[*] Enter the path of password dictionary: ")

crackPass(hashvalue,hashType,fileName)
