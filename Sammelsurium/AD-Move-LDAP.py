# -*- coding: cp1251 -*-
import win32com.client

dso = win32com.client.GetObject("LDAP:")
obj = dso.OpenDSObject("LDAP://DC=de/DC=funkegrp/OU=podrazdelenie kuda","domen\\polzovatel", "parol", 0)


#obj.MoveHere("LDAP://DC=ru/DC=domen/OU=podrazdelenie kuda/CN=_CoolAdmin", "CN=_CoolAdmin")
