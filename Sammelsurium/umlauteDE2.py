# -*- coding: utf-8 -*-

table = {
u"ä": u"ae",
u"ö": u"oe",
u"ü": u"ue",
u"ß": u"ss",
u"A": u"Ae",
u"Ö": u"Oe",
u"E": u"Ue",
}

t2 = {}
for k,v in table.iteritems():
    t2[ord(k)] = v
table = t2

print ("Martin v. Löwis".translate(table))

#te(table))
