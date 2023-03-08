 #!/usr/bin/python

import subprocess
from termcolor import colored
def change_mac(interface, mac):
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface,  "hw", "ether", mac])
	subprocess.call(["ifconfig", interface,  "up"])


def main():
	interface = input("[*] enter interface to change MAC on: ")
	new_mac = input("[*] enter new MAC address to change to: ")
	
	before = subprocess.check_output(["ifconfig", interface])
	change_mac(interface, new_mac)
	
	after = subprocess.check_output(["ifconfig", interface])
	if before == after:
		print(colored("[!!] Failed to change MAC address to:" + new_mac,'red'))
	else:
		print(colored("[+] MAC address changed to: " + new_mac +" on "+ interface + " interface", 'green'))

main()



