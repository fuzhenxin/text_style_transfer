#encoding=utf-8
from Embedding import Embedding
import sys
import numpy as np
from scipy import spatial
from Tool import get_sub_dirnames
import random

def get_sent_emb(line, word_dict):
    line_split = line.strip().split()
    res = []
    for i in line_split:
        if i in word_dict:
            res.append(word_dict[i])
    if len(res)==0:
        res.append(word_dict["the"])
        print "all word not found"
    res = np.array(res)
    mm = np.mean(res, 0)
    mi = np.min(res, 0)
    ma = np.max(res, 0)
    emb = np.concatenate((mm, mi, ma))
    #emb = mm
    return emb


def com_sent(line0, line1, word_dict):
    emb0 = get_sent_emb(line0, word_dict)
    emb1 = get_sent_emb(line1, word_dict)
    result = 1 - spatial.distance.cosine(emb0, emb1)
    return result

def com_file(q_file, r_file, w_file, word_dict):
    q_file = open(q_file, "r")
    r_file = open(r_file, "r")
    w_file = open(w_file, "w")
    q_file_lines = q_file.readlines()
    r_file_lines = r_file.readlines()
    q_file.close()
    r_file.close()
    assert len(q_file_lines)==len(r_file_lines), "length error"
    for line0, line1 in zip(q_file_lines, r_file_lines):
        score = com_sent(line0, line1, word_dict)
        w_file.write(str(score)+"\n")
    w_file.close()
    return

def com_file_score(q_file, r_file, word_dict):
    q_file = open(q_file, "r")
    r_file = open(r_file, "r")
    q_file_lines = q_file.readlines()
    r_file_lines = r_file.readlines()
    q_file.close()
    r_file.close()

    res = []
    assert len(q_file_lines)==len(r_file_lines), "length error"
    for line0, line1 in zip(q_file_lines, r_file_lines):
        score = com_sent(line0, line1, word_dict)
        res.append(score)
    return res

def gen_score(test_dir_name):
    emb = Embedding(100)
    word_dict = emb.get_all_emb()
    subdir_names = ['multi_decoder', 'embedding', 'memory']
    subdir_names = get_sub_dirnames(test_dir_name)
    subdir_names = [i for i in subdir_names if not i.endswith("txt")]
    for dir_name in subdir_names:
        for index_name in ["0", "1"]:
            q_file = test_dir_name+"/q_test.txt"
            r_file = test_dir_name+"/"+dir_name+"/style"+index_name+".txt"
            w_file = test_dir_name+"/"+dir_name+"/style"+index_name+"_semantics.txt"
            com_file(q_file, r_file, w_file, word_dict)
    return 



def random_content_reservation():
    f0 = 'q.txt'
    f1 = 'r.txt'

    emb = Embedding(100)
    word_dict = emb.get_all_emb()

    scores = com_file_score(f0, f1, word_dict)
    scores = np.array(scores, dtype=np.float32)

    print np.mean(scores)



if __name__=="__main__":
    test_dir_name = sys.argv[1]
    gen_score(test_dir_name)
    #random_content_reservation()
    
