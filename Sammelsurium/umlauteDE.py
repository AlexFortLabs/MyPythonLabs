#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
"""
import re
msg = "blöbber"
p = re.compile('[^a-zA-Z0-9]')
p.subn('_', msg)

"""
text = 'Gäßler'
#for zeichen in zeile:
# ü
#	if zeichen == '\xfc':
#		text +='\xc3\xbc'
#ö
#	elif zeichen == '\xf6':
#		text +='\xc3\xb6'
#ä
#	elif zeichen == '\xe4':
#		text +='\xc3\xa4'
#ß
#	elif zeichen == '\xdf':
#		text +='\xc3\x9f'
#Ä
#	elif zeichen == '\xc4':
#		text +='\xc3\x84'
#Ö
#	elif zeichen == '\xd6':
#		text +='\xc3\x96'
#Ü
#	elif zeichen == '\xdc':
#		text +='\xc3\x9c'
#	else:
#		text += zeichen
zeile = text
zeile = zeile.decode('utf-8')

print (zeile)

