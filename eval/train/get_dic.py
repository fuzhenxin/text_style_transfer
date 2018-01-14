#encoding=utf-8

import cPickle as pkl
import collections
import os


file_name=['q_train.txt']
count = dict()
for i in file_name:
    with open(i,'r') as f:
        for line in f.readlines():
            line=line.split()
            for line_per in line:
                if count.has_key(line_per):
                    count[line_per]+=1
                else:
                    count[line_per]=1

count = sorted(count.items(),lambda x,y:cmp(x[1],y[1]), reverse=True)
print len(count)
count_write = collections.OrderedDict()
count_write['eos'] = 0
count_write['UNK'] = 1
index=2
for i in count:
    count_write[i[0]]=index
    index+=1
    #if index>=29998:
    #    break

f = open(r"dict.pkl",'wb')
pkl.dump(count_write,f)
f.close()
