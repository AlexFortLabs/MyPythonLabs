#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

userAlt = "p0300"
workPath = "/raid/profile/"

# os.environ['HOME'] # der aktuelle Benutzerordner

print("Test")
path = (workPath + userAlt)

if os.path.exists(path) == True:
    print(path, "existiert.")
    print(path, "Ordner umbenennen.")
	#os.renames(source, target)
else:
    print(path, "existiert nicht.")

