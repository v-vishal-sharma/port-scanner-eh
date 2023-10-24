#!/bin/python3

import sys
import socket
from datetime import datetime as dt

#Define our target

#sys.argv will get all the arguments given while calling this .py file in a list format.
#python3 (not counted as an argument) scanner.py (argument0) <ip> (argument1)
#sys.argv will have => ['scanner.py','<ip>']
#Pass in your 'Default Gateway' as ip
#Linux => route -n, #windows => ifconfig / ipconfig

if (len(sys.argv) == 2):
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
	#this will translate or convert the hostname(if given) to its ip address.
	
else:
	print("Invalid Synatx/ Invalid amount of arguments")
	print("Syntax: python3 scanner.py <ip>")

#Adding a banner
print("-" * 50)
print(f"Scanning target: {target}")
print("Time Started: " + str(dt.now()))
print("-" * 50)

#Actual Work

try:
	#Since we are scanning the home network, it generally consisits of port 50-85
	for port in range(1,65536):
		#ipv4,port
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #wait for only 1 sec then move on to next port
		result = s.connect_ex((target,port)) #will give 0 or 1, give status of whether the port is open or not
		if (result == 0):
			print(f"Port {port} is open")
		s.close() #close connection to that port 
		
except KeyboardInterrupt:
	print("\nTerminating....")
	sys.exit()
	
except socket.gaierror:
	#For when gibberish value is passed on instead of ip or hostname
	print("Hostname could not be resovled.")
	print("\nTerminating....")
	sys.exit()
	
except socket.error:
	#When the ip address or server refuses to connect altogether
	print("Could not connect to server.")
	print("\nTerminating....")
	sys.exit()





