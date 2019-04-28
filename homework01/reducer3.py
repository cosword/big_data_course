#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
current_ID = None
f_ID = None
li = [None] * 10
count = 0
for line in sys.stdin:
    line = line.strip().split("\t")
    #print len(line)
    ID = line[0]
    f = line[2]
    if current_ID == ID:
        li[count % 10] = f
        count = count + 1
    else:
        if current_ID is not None:
            print current_ID + str(li)
            del li[:]
            li = [None] * 10
        current_ID = ID
        count = 0

