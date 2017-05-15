#import csv

#f = open("New-Users_Sent_test.csv")

#for row in csv.reader(f):
#    print(row)

import csv
 
#----------------------------------------------------------------------
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=';')
    for line in reader:
        print(line["Alt ProfileDirectory"]),
        print(line["Logon Username"])
        print(line["Personalnummer"])
        print("." * 25)
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    with open("New-Users_Sent_test.csv") as f_obj:
        csv_dict_reader(f_obj)
