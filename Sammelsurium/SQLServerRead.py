# --------------------------------------------------------
# Program by Alexander.F.
#
#
# Version       Date        Info
# 1.0           2017        Initial Version
# Hello Python 3
# --------------------------------------------------------

import pypyodbc as db

mySQLServer = "FUNKEGRUPPE\SQL1"
myDBase = "northwind"

connect_string = 'DRIVER={SQL Server};SERVER=SQL1;DATABASE=test_vertrieb;Trusted_Connection=yes'
connection = db.connect(connect_string)
cursor = connection.cursor()

mySQLQuery = ("""
                SELECT kdnr, kdname, plz, land
                FROM dbo.Hilmes_Kunden
                WHERE land = 'NL'
             """)

cursor.execute(mySQLQuery)
results = cursor.fetchall()

for row in results:
    compName = row[0]
    contactName = row[1]
    landName = row[2]

    print("Welcome: " + str(compName) + " User: " + str(contactName) + " Land: " + str(landName))

connection.close()
