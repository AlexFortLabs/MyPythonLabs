print("SAMBA reboot? (j) - Ja, (n) - Nein")
# antwort_ende = input()
antwort_ende = raw_input("j - Ja, n - Nein: ")
if antwort_ende == "n":
    exit()
elif antwort_ende == "j":
    print("SAMBA go reboot")
else:
    print("Falsche Eingabe. SAMBA wird nicht aktualisiert.")
