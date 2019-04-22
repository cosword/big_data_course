#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
for line in sys.stdin:
    line = line.strip().split(":")
    ID = line[0]
    line = line[1].split(" ")
    for f in line:
        print f + "\t" + str(ID)
