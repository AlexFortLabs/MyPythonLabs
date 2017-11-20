# --------------------------------------------------------
# Program by Alexander.F.
#
#
# Version       Date        Info
# 1.0           2017        Initial Version
# Hello Python 3
# --------------------------------------------------------
import os
import pypyodbc as db

# Hole Benutzerdefinierte Systemvariabel MYDOMAIN – von mir selbst definierte
#domaine = os.getenv('MYDOMAIN')
#mySQLServer = (domaine + "\SQL1")
#myDBase = "Stamdaten"

connect_string = 'DRIVER={SQL Server};SERVER=SQL1;DATABASE=Stammdaten;Trusted_Connection=yes'
connection = db.connect(connect_string)
cursor = connection.cursor()

mySQLQuery = ("""
                SELECT id, konto, bereich, zeitstempel
                FROM dbo.Zuordnung_Konto_Bereich
                WHERE bereich = 'Rohstoffe'
             """)

cursor.execute(mySQLQuery)
results = cursor.fetchall()

for row in results:
    id = row[0]
    konto = row[1]
    bereich = row[2]

    print("ID: " + str(id) + " Konto: " + str(konto) + " Bereich: " + str(bereich))

connection.close()
