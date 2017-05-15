# -*- coding: cp1251 -*-
import win32com.client

adsi = win32com.client.GetObject("LDAP://DC=de/DC=funkegrp/OU=Admin-Accounts")
for entry in adsi:
    print(entry.Class, entry.Get('objectClass'))
    
