#! python3
# --------------------------------------------------------
# Program by Alexander.F.
#
#
# Version       Date        Info
# 1.0           2017        Initial Version
# Starte Webbrowser auf bestimte Seite
# --------------------------------------------------------
import webbrowser
#webbrowser.open('https://www.synology.com/de-de/releaseNote/DS212j')
address = ['Klusenerweg 38A, 59494 Soest, DE', 'Siegenbeckstr. 15, 59071 Hamm-Uentrop, DE']
webbrowser.open('https://www.google.com/maps/place/' + address[0])
webbrowser.open('https://www.google.com/maps/place/' + address[1])