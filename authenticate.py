#! /usr/bin/python
# -+- coding: utf-8 -+-

print "Content-Type: text/html"
import cgitb; cgitb.enable()
import cgi

form = cgi.FieldStorage()

f = open('username_passwords.txt','r')
names = f.read().split('\n')
f.close()

def authentic(name, password):
    if password == "":
        return "NP"
    for namer in names:
        temp = (namer.split(':'))
        temper = temp[0]
        if temper == name:
            return "V"
    return "NR"

def register(name, password):
    writer = open('username_passwords.txt','w')
    x = ''
    for namer in names:
        x += namer + '\n'
    x += name
    x += ':'
    x += password
    x += '\n'
    writer.write(x)
    writer.close()
