#encoding=utf-8

import sys
import random
from Tool import get_sub_dirnames
import xlsxwriter


def get_sample_data(dir_name):

    workbook = xlsxwriter.Workbook('toscore1.xlsx')
    worksheet = workbook.add_worksheet()
    

    subdir_names = get_sub_dirnames(dir_name)
    subdir_names = [i for i in subdir_names if not i.endswith("txt")]

    q, r = [], []
    for sub_dir_name in subdir_names:
        f0 = open(dir_name+"/"+sub_dir_name+"/style0.txt").readlines()
        f1 = open(dir_name+"/"+sub_dir_name+"/style1.txt").readlines()
        f_q = open(dir_name+"/q_test.txt").readlines()
        f_s = open(dir_name+"/s_test.txt").readlines()
        for i,j in enumerate(f0):
            if int(f_s[i].strip()) ==1 :
                continue
            else:
                q.append(f_q[i])
                r.append(j)

    random.seed(1027)
    random.shuffle(q)
    random.seed(1027)
    random.shuffle(r)

    i = -1
    count = 0
    cc = 0
    while True:
        i += 1
        if q[i].strip()==r[i].strip():
            cc += 1
            #continue

        res0 = q[i].strip()
        res1 = r[i].strip()
        worksheet.write(count , 0, res0.decode('utf-8'))
        worksheet.write(count , 1, res1.decode('utf-8'))
        count += 1
        if count>99:
            break
    print cc
    workbook.close()

if __name__=="__main__":
    dir_name = sys.argv[1]
    get_sample_data(dir_name)