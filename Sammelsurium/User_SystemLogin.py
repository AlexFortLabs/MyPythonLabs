# -*- coding: cp1252 -*-
import sys
import time


def schleifen(warten):
    while True:  # <--- Dauerschleife bis Strg + C...
        zeitstempel = time.strftime('%d.%m.%Y %H:%M:%S')
        try:
            inp = open('log.txt', 'w')
            try:
                inp.write(zeitstempel + '\n')  # Datum + Zeilenumbruch einfügen
                # inp.flush() # da jedesmal 'close' obsolet
            finally:
                inp.close()
                print
                zeitstempel
                time.sleep(warten)
        except (IOError, OSError), error:
            print("FEHLER: Konnte Zeitstempel '%s' nicht schreiben: %s" % (zeitstempel, error))
            sys.exit(2)

def main():
    try:
        schleifen(5)  # Schleifenmethode aufrufen, mit 5 Sekunden Wartezeit
    except KeyboardInterrupt:  # wenn Strg+C gedrückt wird, passiert das...
        print
        "-- Abbruch durch Benutzer --"


if __name__ == '__main__':
    main()
