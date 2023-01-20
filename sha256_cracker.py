from pwn import *
import sys


if len(sys.argv) != 2:
  print("Invalid number of arguments")
  print(">> {} <sha256sum> <wordlist>".format(sysargv[0]))
  exit()

  wanted_hash = sys.argv[1]
  print(wanted_hash)
  password_file = sys.argv[2]
  #"/usr/share/wordlists/rockyou.txt" as an example
  attempts = 0
  
  with log.progress("Attempting: {}!\n".format(wanted_hash)) as p:
      with open(password_file, "r", encoding='latin-1') as password_list:
          for password in password_file:
              password = password.strip("\n").encode('latin-1')
              #strip newline character from password file so it is not included in hashing operation
              password_hash = sha256sumhex(password)
              p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash)
              if password_hash == wanted_hash:
                  print("password")
              attempts += 1
          p.failure("Password not found")
  
  
