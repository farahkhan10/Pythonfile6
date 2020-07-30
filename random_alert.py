#!/usr/bin/env python

from random import choices

hours = list(range(1,25))
status = ["Alert", "No Alert"]
for h in hours:
	print(f"Hour: {h} -- {choices(status)}") 
