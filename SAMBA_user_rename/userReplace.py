#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pwd
import csv

grpPath = "/etc/group"
smbPath = "/etc/samba/smb.conf"

# ----------------------------------------------------------------------
def UserDa(userName):
    # os.system("id " +
    return (userName in [entry.pw_name for entry in pwd.getpwall()])


# ----------------------------------------------------------------------
def EditMyFile(nameAlt, nameNeu, myFile):
    os.system("sed -i.$(date +%F) 's/" + nameAlt + "/" + nameNeu + "/g' " + myFile)


# ----------------------------------------------------------------------
def UserRename(userAlt, userNeu):
    if (UserDa(userAlt)):
        if (UserDa(userNeu)):
            print("Achtung! User " + userNeu + " bereits vorhanden.")
        else:
            print("X" * 50)
            print("User " + userNeu + " wird erstehlt!")
            os.system("useradd -g users " + str.upper(userNeu))

            print("ACTUNG! Gruppen Zugehoerigkeit wird nicht geender!!!")
            # EditMyFile(userAlt, str.upper(userNeu), grpPath)
            print(os.system("id " + userAlt))

            print("SAMBA Konfiguration wird geender!!!")
            EditMyFile(userAlt, str.upper(userNeu), smbPath)

            print("User " + userAlt + " wird geloescht!")
            # os.system("userdel -f " + str.upper(userAlt))
            os.system("userdel -f " + userAlt)

            raw_input("Weiter mit ENTER.")
            print("User " + userNeu + " ist eingerichtet!")
    else:
        print("Achtung! User " + userAlt + " ist nicht vorhanden")


# ----------------------------------------------------------------------
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=';')
    for line in reader:
        UserRename(line["Alt ProfileDirectory"], line["Logon Username"])
        # print(line["Personalnummer"])
        print("." * 50)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    with open("New-Users_Sent.csv") as f_obj:
        csv_dict_reader(f_obj)

print("X" * 50)
print("ACHTUNG! SAMBA Dienst neustarten nicht vergessen!")
print("X" * 50)
#
#
