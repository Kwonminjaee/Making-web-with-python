#!C:\Users\민재\AppData\Local\Programs\Python\Python37-32\python.exe

import os
import os, html_sanitizer
def getList():
    sanitizer = html_sanitizer.Sanitizer()
    files = os.listdir('data')
    listStr = ''
    for item in files:
        item = sanitizer.sanitize(item)
        listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr
