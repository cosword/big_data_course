#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
dic = {}
for line in sys.stdin:
    line = line.strip().split(":")
    ID = line[0]
    li = line[1].split(" ")
    lenth = len(li)
    for i in range(lenth-1):
        print ID + "\t" + li[i]
        print li[i] + "\t" + ID
        for j in range(i+1,lenth):
            print li[i] + "\t" + li[j]
            print li[j] + "\t" + li[i]
    print ID + "\t" + li[lenth - 1]
    print li[lenth - 1] + "\t" + ID
    del li[:]
    del lenth
