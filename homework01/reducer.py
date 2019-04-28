#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
dic = {}
for line in sys.stdin:
    line = line.strip().split("\t")
    ID = line[0]
    if dic.get(ID) == None:
        dic[ID] = []
    dic[ID].append(line[1])

for key in dic.keys():
    print key + ":" + " ".join(dic[key])
