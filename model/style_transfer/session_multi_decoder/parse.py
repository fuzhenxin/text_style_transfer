#-*- coding:utf-8 -*-
# AUTHOR:   fuzx
# FILE:     parse.py
# ROLE:     TODO (some explanation)
# CREATED:  2017-06-26 21:40:31
# MODIFIED: 2017-12-19 11:11:50




#0 wei bo
#1 douban
import sys
file_input = open(sys.argv[1],"r").readlines()
file_style = open(sys.argv[2],"r").readlines()
file_input_style0 = open(sys.argv[3],"r").readlines()
file_input_style1 = open(sys.argv[4],"r").readlines()

assert len(file_input)==len(file_input_style0), "error"
assert len(file_input_style0)==len(file_input_style1), "error"

file_len = len(file_input)

for i in range(file_len):
    if file_style[i][:-1]=="0":
        style_name = "neg"
    else:
        style_name = "pos"
    print i,": ",style_name,":\t",file_input[i]
    print "\t\t\tneg: ",file_input_style0[i]
    print "\t\t\tpos: ",file_input_style1[i]

