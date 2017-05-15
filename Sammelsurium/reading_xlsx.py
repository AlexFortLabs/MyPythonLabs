import xlrd

workbook = xlrd.open_workbook("F:\\ProgrammingLab\\PShel\\Rename-ADUser\\New-Users_Sent.xlsx")

sheet_count = workbook.nsheets
print("Numbers of sheet: {0}".format(sheet_count))

sheets_name = workbook.sheet_names()
print("Sheet names: {0}".format(sheets_name))
