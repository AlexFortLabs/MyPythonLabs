# -*- coding: cp1251 -*-
import win32com.client

dso = win32com.client.GetObject("LDAP:")
obj = dso.OpenDSObject("LDAP://DC=de/DC=funkegrp/OU=подразделениеКкуда","домен\\пользователь", "пароль", 0)


#obj.MoveHere("LDAP://DC=ru/DC=домен/OU=подразделение куда/CN=_CoolAdmin", "CN=_CoolAdmin")
