#! python3
# --------------------------------------------------------
# Program by Alexander.F.
#
#
# Version       Date        Info
# 1.0           2017        Initial Version
# Suchergebnis in mehrerren tabs öfnen
# --------------------------------------------------------
import requests, sys, webbrowser, bs4

print('Googele mal...') # wird angezeigt beim laden der Google Seiten

res = requests.get('http://google.de/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#print(res)
# Holen einige gefundene Links
soup = bs4.BeautifulSoup(res.text)

# ausgewelte Links in einzelnen Tabs zeigen
linkElems = soup.select(' .r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.de' + linkElems[i].get('href'))
