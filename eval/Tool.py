#encoding=utf-8

import os

def get_sub_dirnames(dir_name):
    return os.listdir(dir_name)

if __name__=="__main__":
    res = get_sub_dirnames("test")
    print [i for i in res if not i.endswith("txt")]



