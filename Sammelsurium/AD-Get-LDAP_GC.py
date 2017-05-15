# -*- coding: cp1251 -*-
import win32com.client

# poluchenie objekta tekushhego domena v lokal'noj seti:
adsi = win32com.client.GetObject("LDAP:")
print(adsi.Class, adsi.ADsPath, '\n')
for i in adsi:
    print(i.Class, i.ADsPath)
    print(i.Name, "\n")

# poluchenie objekta kornevogo domena v lokal'noj seti:
adsi = win32com.client.GetObject("GC:")
print(adsi.Class, adsi.ADsPath, '\n')
for i in adsi:
    print(i.Class, i.ADsPath)
    print(i.Name, "\n")
# Primechanie: v dannom sluchae idjot obrashhenie
# k global'nomu katalogu kontrollera domena (Global Catalog, GC).
#////
#Namespace LDAP: 

#domainDNS LDAP://DC=funkegrp,DC=de
#DC=funkegrp 

#Namespace GC: 

#top GC://funkegrp.de
#funkegrp.de
#////
