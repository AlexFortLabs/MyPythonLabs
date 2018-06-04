#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Erstellt eine CSV Datei, in der die Luftfeuchtigkeit jede 5 min abgespeichert werden soll.

from time import *

HOST = "localhost"
PORT = 4223

UID_Hum = "Hu"

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_humidity import BrickletHumidity

if __name__ == "__main__":

    # Verbindung zu Bricklets wird aufgebaut.
    ipcon = IPConnection()

    Hum = BrickletHumidity(UID_Hum, ipcon)
    ipcon.connect(HOST, PORT)  # Connect to brickd

    # Don't use device before ipcon is connected

    t = time()
    flag = False
    j = True

    while True:

        Time_akt = localtime()

        if ((Time_akt[4] == 0 or Time_akt[4] == 5 or Time_akt[4] == 10 or Time_akt[4] == 15 or Time_akt[4] == 20 or
             Time_akt[4] == 25 or Time_akt[4] == 30 or Time_akt[4] == 35 or Time_akt[4] == 40 or Time_akt[4] == 45 or
             Time_akt[4] == 50 or Time_akt[4] == 55) \
                and flag == False):
            flag = True
            print('Flag: ' + str(flag))
            # Sensoren auslesen alle 5min

            Luftfeuchtigkeit = Hum.get_humidity()

            # Akutelle Systemzeit auslesen
            Jahr = str(Time_akt[0])
            Monat = str(Time_akt[1])
            Tag = str(Time_akt[2])
            Stunde = str(Time_akt[3])
            Minute = str(Time_akt[4])

            # Sensordaten konvertieren und speichern

            Hum_str = str(Luftfeuchtigkeit)

            Ausgabe = (Jahr + '.' + Monat + '.' + Tag + ';' \
                       + Stunde + ':' + Minute + ';' \
                       + Hum_str + ';' \
                       + '\n')

            filename = (Jahr + '_' + Monat + '_' + Tag + '_schnell' + '_' + 'Data.csv')

            data = open(filename, 'a')
            data.write(Ausgabe)
            data.close()

        if ((Time_akt[4] >= 1 and Time_akt[4] < 5) or \
                (Time_akt[4] >= 6 and Time_akt[4] < 10) or \
                (Time_akt[4] >= 11 and Time_akt[4] < 15) or \
                (Time_akt[4] >= 16 and Time_akt[4] < 20) or \
                (Time_akt[4] >= 21 and Time_akt[4] < 25) or \
                (Time_akt[4] >= 26 and Time_akt[4] < 30) or \
                (Time_akt[4] >= 31 and Time_akt[4] < 35) or \
                (Time_akt[4] >= 36 and Time_akt[4] < 40) or \
                (Time_akt[4] >= 41 and Time_akt[4] < 45) or \
                (Time_akt[4] >= 46 and Time_akt[4] < 50) or \
                (Time_akt[4] >= 51 and Time_akt[4] < 55) or \
                (Time_akt[4] >= 56 and Time_akt[4] < 60)):
            flag = False

        t = time()

        if j == False:
            break

    ipcon.disconnect()