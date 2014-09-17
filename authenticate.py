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
    for name in names:
        if name.strip() == name:
            return "V"
    return "NR"

def register():
    writer = open('username_passwords.txt','w')
    sure = open('username_passwords.txt','r')
    sure2 = sure.read()
    x= form['username'].value
    x+= ':'
    x+= form['pswd'].value
    x+= '\n'
    sure2 += x
    writer.write(sure2)
    writer.close
