#! python3
# --------------------------------------------------------
# Program by Alexander.F.
#
#
# Version       Date        Info
# 1.0           2017        Initial Version
# Hello Python 3
# --------------------------------------------------------
import os
import shutil

#pc_list = ["W7-FPL-7", "w7-fpl-5", "w7-fpl-6", "WKS-FPL001", "WKS-FPL002", "WKS-FPL003", "WKS-FPL004"]
#pc_list = ["W7-FPL-7", "WKS-FPL002", "WKS-FPL003", "WKS-FPL004", "WKS-W7-DEVEL"]
#pc_list = ["W7-FPL-7", "WKS-FPL003", "W7-FPL-2", "MOBIL-W7-FPL2"]
pc_list = ["W7-FPL-2"]
#pc_list = ["depcl080"]

file_name1 = r"\Maintenance.TSK"
file_name2 = r"\Job10011-32-64.exe"
source_path = r"\\localhost\work"

for next_pc in pc_list:
    dest_path1 = r"\\" + next_pc + "\C$\Support\MyDevices\Maintenance"
    dest_path2 = r"\\" + next_pc + "\C$\Support\Jobs"
    if os.path.exists(dest_path1):  # == True:
        print(dest_path1, " Ordner existiert.")
        shutil.copyfile((source_path + file_name1), (dest_path1 + file_name1))
        shutil.copyfile((source_path + file_name2), (dest_path2 + file_name2))
    else:
        print("Auf ", dest_path1, " Ordner konte nicht zugegriffen werden.")

# source_path = "//localhost/work"
# dest_path = "//depcl080/C$/Support/MyDevices/Maintenance"
# file_name = "/myfile.txt"
#shutil.copyfile(os.path.join(source_path, file_name), os.path.join(dest_path, file_name))

#print(os.path.join(source_path, file_name1))
#print(os.path.join(dest_path1, file_name2))
