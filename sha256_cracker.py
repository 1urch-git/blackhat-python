from pwn import *
import sys


if len(sys.argv) != 2:
  print("Invalid number of arguments")
  print(">> {} <sha256sum>".format(sysargv[0]))
  exit()
