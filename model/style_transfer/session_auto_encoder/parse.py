#-*- coding:utf-8 -*-
# AUTHOR:   fuzx
# FILE:     parse.py
# ROLE:     TODO (some explanation)
# CREATED:  2017-06-26 21:40:31
# MODIFIED: 2017-09-29 15:58:08




#0 wei bo
#1 douban
import sys
file_input0 = open("q_test_style.txt","r").readlines()
file_input1 = open("../../data/r_test.txt","r").readlines()


file_len = len(file_input0)

for i in range(file_len):
    print "origin  : ",file_input0[i],
    print "generate: ",file_input1[i],
    print ""

