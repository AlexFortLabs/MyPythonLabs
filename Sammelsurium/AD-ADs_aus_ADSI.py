import win32com.client

adsi = win32com.client.GetObject("ADs:")
print(adsi.Class, "\n")
for i in adsi:
    print(i.Name)
