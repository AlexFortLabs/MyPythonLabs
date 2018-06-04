import locale
import csv
import re
#hand = open('Protokol.txt')

def parse(filepath):
    data = list()
    header = ['Umsatz (ohne Soll/Haben-Kz)', 'Soll/Haben-Kennzeichen', 'WKZ Umsatz', 'Kurs', 'Basis-Umsatz',	'WKZ Basis-Umsatz',	'Konto', \
              'Gegenkonto (ohne BU-Schlüssel)', 'BU-Schlüssel',	'Belegdatum', 'Belegfeld 1', 'Belegfeld 2',	'Skonto',	'Buchungstext', \
              'Postensperre', 'Diverse Adressnummer', 'Geschäftspartnerbank', 'Sachverhalt', 'Zinssperre', 'Beleglink']
    data.append(header)

    hand = open(filepath)
    feldBU_Schluessel = ' '
    for line in hand:
        line = line.rstrip()

        if re.search('^Umsatz: ', line):
            feldBU_Schluessel = ' '
            x = re.findall('^Umsatz: ', line)
            if len(x) > 0 :
                feldName, feldWert = re.split(":", line)
                feldWertOhne = (abs(int(feldWert)))
                feldWertComa = locale.format("%.02f", (int(feldWertOhne) / 100))
                if (int(feldWert) < 0):
                    #print(feldWert, " H")
                    shKenzeichen = "H"
                    #feldWertOhne = (abs(int(feldWert)))
                    #feldWertComa = locale.format("%.02f",(int(feldWertOhne) / 100))
                else:
                    #print(feldWert, " S")
                    shKenzeichen = "S"
        elif re.search('^Gegenkonto:', line):
            feldName, feldGegenkonto = re.split(":", line)
            #........if shKenzeichen == "H"
            #print(feldGegenkonto)
        elif re.search('^Belegfeld1: ', line):
            feldName, feldBelegfeld1 = re.split(":", line)
        elif re.search('^Datum: ', line):
            feldName, feldDatum = re.split(":", line)
        elif re.search('^Konto:', line):
            reUmsatz = re.findall("Konto:.*", line)
            for item in reUmsatz:
                for line in re.findall("\w\S*:.*\w", item):
                    feldName, feldKonto = re.split(":", line)
                    #print(feldKonto)
        elif re.search('^Text: ', line):
            feldName, feldBuchungstext = re.split(":", line)
        elif re.search('^BU-Schluessel: ', line):
            x = re.findall('^BU-Schluessel: ', line)
            if len(x) > 0:
                feldName, feldBU_Schluessel = re.split(":", line)
            else: feldBU_Schluessel = ' '
                #print(feldBU_Schluessel)
        elif re.search('^Waehrungskennung: ', line):
            #feldName, feldWKZumsatz = re.split(":", line)
            #print('-------------Satz komplet------------')
            #dataSatz = [feldWertComa, shKenzeichen, feldWKZumsatz, '', '', '', feldKonto, feldGegenkonto, feldBU_Schluessel, feldDatum, feldBelegfeld1, '', '', feldBuchungstext, '', '', '', '', '', '']
            dataSatz = [feldWertComa, shKenzeichen, '', '', '', '', feldKonto, feldGegenkonto, feldBU_Schluessel, feldDatum, feldBelegfeld1, '', '', feldBuchungstext, '', '', '', '', '', '']
            # добавляем в конец списка
            data.append(dataSatz)
        else: pass
    return data

def info():
    print("KHK in DATEV Converter")
    print("Version 1.0 Windows")
    print("Lizenzprogramm - Eigentum der ALMACOM GmbH\n")
    print("Copyright 2018 A.Fortowski")
    print("Alle Rechte vorbehalten\n")

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, "de")  # для  Windows
    info()
    filepath = 'Protokol.txt'
    data = parse(filepath)
    #print(data)
#  1
    #with open("DATEV_output.csv", "wb") as csv_file:
    #    writer = csv.writer(csv_file, delimiter=',')
    #    for line in data:
    #        writer.writerow(line)
#  2
    #myFile = open('DATEV_output.csv', 'w')
    #with myFile:
    #    writer = csv.writer(myFile)
    #    writer.writerows(data)
#  3
    with open("DATEV_output.csv", "w", newline="") as out_csv:
        out = csv.writer(out_csv, delimiter=";")
        #out = csv.writer(out_csv)
        #out = csv.writer(out_csv, delimiter=',')
        out.writerows(data)
        #for row in data:
        #    out.writerow(row)

    input("Writing complete")