#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Linux
#userAlt = "p0300"
#workPath = "/raid/profile/"

# Windows
userAlt = "p0537"
workPath = "C:\\Users\\"


# os.environ['HOME'] # der aktuelle Benutzerordner

print("Test")
path = (workPath + userAlt)

if os.path.exists(path): # == True:
    print(path, "existiert.")
    print(path, "Ordner umbenennen.")
	#os.renames(source, target)
else:
    print(path, "existiert nicht.")

# ist das Ordner oder File & exsistiert das?
print(os.path.exists('C:\\Windows'))        # True unter Windows
print(os.path.exists('C:\\bin_nicht_da'))   # False

print(os.path.isdir('C:\\Windows\\System32'))   # True
print(os.path.isfile('C:\\Windows\\System32'))  # False

print(os.path.isdir('C:\\Windows\\System32\\calc.exe'))   # False
print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))  # True

# pruefen ob FlashDisk angeschlossen ist als E:
if os.path.exists('E:\\'):
    print("Flash Disk E ist angesteckt")
else:
    print("Flash Disk E ist nicht angesteckt")