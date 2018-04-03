# INI-Datei bearbeiten
# INI-Datei liegt unter C:\Program Files\uvnc bvba\UltraVNC
# zu Ändernde Werte:
# primary=1
# secondary=1

#import os, io
#from ConfigParser import SafeConfigParser

import configparser

#import SafeConfigParser
#import ConfigParser

parser = configparser.ConfigParser()

#str_pc = (input("Name des Rechner: "))
#int_value = int(input("Auf welches Wert 0/1 setzen: "))

#####
#from configparser import SafeConfigParser

#parser = configparser.ConfigParser()
#parser.read('ultravnc.ini')


####

#parser = SafeConfigParser()
#parser.read('ultravnc.ini')

#print (parser.get('ultravnc', 'secondary'))

#parser = ConfigParser.RawConfigParser() # SafeConfigParser
#parser.read('ultravnc.ini')

#print(parser.get('ultravnc', 'value'))


# parser.set('Section1', 'baz', 'fun')
#parser.set('admin', 'secondary', '15')

# Writing our configuration file to 'example.ini'
with open('ultravnc.ini', 'wb') as configfile:
    parser.set('admin', 'secondary', '15')
    parser.write(configfile)

####
parser.read('ultravnc.ini')
print('WERT:', parser.get('admin', 'secondary'))
print('WERT:', parser.get('admin', 'primary'))
