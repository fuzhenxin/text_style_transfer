#encoding=utf-8

from Embedding import Embedding
from emb_test import com_sent
import scipy.stats as st
import numpy as np
import csv
import cPickle as pkl


def read_csv():
    res = []
    f = open('score.csv', 'rb')
    lines = csv.reader(f, delimiter=',', quotechar='|')
    not_fisrt = True
    for row in lines:
        if not_fisrt:
            not_fisrt = False
            continue
        res.append((row[-5], row[-4], row[-3]))
    
    f.close()
    return res
    

def cal_co():
    emb = Embedding(100)
    word_dict = emb.get_all_emb()

    score_m = []
    score_h = []
    res = read_csv()
    for q,r,score in res:
        cal_dis = com_sent(q[6:], r[5:], word_dict)
        score_m.append(cal_dis)
        score_h.append(score)

    score_m = np.array(score_m, dtype=np.float32)
    score_h = np.array(score_h, dtype=np.float32)

    score_mm, score_hh = [], []

    for i in range(200):
        score_mm.append((score_m[i*3]+score_m[i*3+1]+score_m[i*3+2])/3)
    for i in range(200):
        score_hh.append((score_h[i*3]+score_h[i*3+1]+score_h[i*3+2])/3)

    for i in score_mm:
        print i,
    print
    for i in score_hh:
        print i,
    print


    score_mm = np.array(score_mm)
    score_hh = np.array(score_hh)
    pkl.dump((score_hh, score_mm), open("score_np.pkl", "wb"))

    pc, pp = st.pearsonr(score_mm, score_hh)
    sc, sp = st.spearmanr(score_mm, score_hh)

    print "\t\t c p-value"
    print "pearson : ", pc, pp
    print "spearman: ", sc, sp


if __name__=="__main__":
    cal_co()