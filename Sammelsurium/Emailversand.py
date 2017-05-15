#!/usr/bin/python
 # -*- coding: utf-8 -*-

 import smtplib
 from email.mime.text import MIMEText

 umlautstring="Text mit Umlauten ÖöÄäÜüß"
 print umlautstring.encode('latin-1')

 Empfaenger = 'xxxx@yyy.zz'
 Absender = 'zzzz@yyy.zz'
 Passwort = '***'
 smtpserver = smtplib.SMTP('smtp.mail.yahoo.com', 587)
 smtpserver.ehlo()
 smtpserver.starttls()
 smtpserver.ehlo
 smtpserver.login(Absender, Passwort)

 antwortvonrequests.encoding='UTF-8'
"""
 msg = MIMEText(inhalt.encode("latin-1"), _charset="latin-1")
 msg['Subject'] = umlautstring.encode('latin-1')

 msg['From'] = Absender
 msg['To'] = Empfaenger

 smtpserver.sendmail(Absender, [Empfaenger], msg.as_string())
"""
 msg = MIMEText(umlautstring.encode("utf-8"), _charset="utf-8")
 msg['Subject'] = umlautstring
 msg['From'] = Absender
 msg['To'] = Empfaenger
 smtpserver.sendmail(Absender, [Empfaenger], msg.as_string("utf-8"))

 smtpserver.quit()
