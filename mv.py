# -*- coding: utf-8 -*-
import os
print("Root permissions are needed for some files/directories!")
print("This program will not work if you type like this “/Users/username but will work if you type like this ../../username!")
old_name = raw_input("Please enter the file or directory name.  ")
new_name = raw_input("Please enter the new name/location for the file or directory.  ")
os.rename(old_name, new_name)