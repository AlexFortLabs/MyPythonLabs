#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
"""
import re
msg = "bl�bber"
p = re.compile('[^a-zA-Z0-9]')
p.subn('_', msg)

"""
text = 'G��ler'
#for zeichen in zeile:
# �
#	if zeichen == '\xfc':
#		text +='\xc3\xbc'
#�
#	elif zeichen == '\xf6':
#		text +='\xc3\xb6'
#�
#	elif zeichen == '\xe4':
#		text +='\xc3\xa4'
#�
#	elif zeichen == '\xdf':
#		text +='\xc3\x9f'
#�
#	elif zeichen == '\xc4':
#		text +='\xc3\x84'
#�
#	elif zeichen == '\xd6':
#		text +='\xc3\x96'
#�
#	elif zeichen == '\xdc':
#		text +='\xc3\x9c'
#	else:
#		text += zeichen
zeile = text
zeile = zeile.decode('utf-8')

print (zeile)

