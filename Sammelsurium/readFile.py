import csv
#print (csv.list_dialects())

#reader = csv.reader(open("C:\test.csv", "rb"), delimiter=";")
#reader = csv.DictReader(open("test.csv", "rb")) 
#reader = csv.reader(open("C:\test.csv", "rb"))

#for rowi in reader :
#    print (rowi)

filename_in = "c:/test.csv"
filename_out = "c:/meinout.txt"

"""
with open(filename, "rt") as f:
    # tu etwas mit 'f', z. B.:
    # rb -Binär-
    # rt -Text-format
    reader = csv.reader(f)
    for row in reader:
        # row is a list of strings
        # use string.join to put them together
        print (', '.join(row))
        
f.close()
"""

fobj_in = open(filename_in)
fobj_out = open(filename_out,"w")
i = 1
for line in fobj_in:
    print (line.rstrip())
    #print (line)
    fobj_out.write(str(i) + ": " + line)
    i = i + 1
fobj_in.close()
fobj_out.close()
