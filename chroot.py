# -*- coding: utf-8 -*-
import os
id = os.getuid()
if id = 0:
	path = raw_input("")
	os.chroot(path)
else:
	print("Root permissions are needed!")