# --------------------------------------------------------
# Program by Alexander.F.
#
#
# Version       Date        Info
# 1.0           2017        Initial Version
# Python 3 gzip: create and unpack archive
# --------------------------------------------------------
import os, glob, tarfile, filecmp
#import random
#import string
#import shutil

source_dir = "/raid/Klicktel"
destination_dir = "/raid/daten/klicktelBK"
archive_name = "archive.tar.gz"

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def okay():
    print("Done.\n")

print("Compressing files to %s..." % archive_name)
tar = tarfile.open(archive_name, "w:gz")
for file_name in glob.glob(os.path.join(source_dir, "*")):
    print("  Adding %s..." % file_name)
    tar.add(file_name, os.path.basename(file_name))
tar.close()
okay()

"""
print("Decompressing files to %s..." % destination_dir)
shutil.rmtree(destination_dir)
create_dir(destination_dir)
tar = tarfile.open(archive_name, "r:gz")
for tarinfo in tar:
    print("  Extracting %s (size: %db; type: %s)..." % (tarinfo.name,
        tarinfo.size, "regular file" if tarinfo.isreg() else "directory"
        if tarinfo.isdir() else "something else")
    tar.extract(tarinfo, destination_dir)
tar.close()
okay()
"""

"""
#  Here is a simple code to extract both .tar and .tar.gz in one go:
import tarfile
if (fname.endswith("tar.gz")):
    tar = tarfile.open(fname, "r:gz")
    tar.extractall()
    tar.close()
elif (fname.endswith("tar")):
    tar = tarfile.open(fname, "r:")
    tar.extractall()
    tar.close()
"""
print("Comparing source and result...")
dc = filecmp.dircmp(source_dir, destination_dir)
print("Same: [%s]" % ", ".join(dc.same_files))
print("Different: [%s]" % ", ".join(dc.diff_files))
print("Funny: [%s]" % ", ".join(dc.funny_files))

print("Test passed." if len(dc.diff_files) == 0
    and len(dc.funny_files) == 0 else "Test failed.")