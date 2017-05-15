# -*- coding: cp1251 -*-

# Object umbenennen

import win32com.client

dso = win32com.client.GetObject("LDAP:")
obj = dso.OpenDSObject("LDAP://DC=funkegrp/DC=de", "funkegrp\\p0532", "geheim#15", 0)

print(obj)


#obj.MoveHere("LDAP://DC=ru/DC=domen/OU=podrazdelenie/CN=_TestAdmin", "CN=_CoolAdmin")
