#encoding=utf-8
import numpy as np
import cPickle as pkl
from Tool import get_sub_dirnames

def parse_model_class(model_name, style_type):
    #transfer to index_name
    count_right = [0, 0]
    for index_name in [0,1]:
        f_classification = open(model_name+"style"+str(index_name)+"_classification.txt", "r")
        f_class = f_classification.readlines()
        f_classification.close()
        f_class = map(lambda x:float(x), f_class)
        f_class = [1 if i>0.5 else 0 for i in f_class]
        assert len(style_type)==len(f_class), "length error at model_class"

        for index,i in enumerate(style_type):
            if i==1-index_name:
                if f_class[index] == index_name:
                    count_right[index_name] += 1

    #print count_right[0], count_right[1]
    return float(count_right[0]+count_right[1])/2000.

def parse_model_sem(model_name, style_type):
    #transfer to index_name
    res_sem = []
    for index_name in [0,1]:
        f_semantics = open(model_name+"style"+str(index_name)+"_semantics.txt", "r")
        f_sem = f_semantics.readlines()
        f_semantics.close()
        f_sem = map(lambda x:float(x), f_sem)
        assert len(style_type)==len(f_sem), "length error at model_sem"

        for index,i in enumerate(style_type):
            if i==1-index_name:
                res_sem.append(f_sem[index])

    assert len(res_sem)==2000, "length error at model_sem2"
    res_sem = np.array(res_sem)
    return np.mean(res_sem)

def parse_dir(dir_name):
    res_class, res_sem = [], []
    f_s = open(dir_name+"/s_test.txt", "r")
    f_s_lines = f_s.readlines()
    f_s.close()

    style_type = map(lambda x: int(x), f_s_lines)
   
    print "dir_name model_type \t transfer_strength content_reservation mixture"
    print "================================================================================"
    #model_types = ["multi_decoder", "embedding", "memory"]
    model_types = get_sub_dirnames(dir_name)
    model_types = [i for i in model_types if not i.endswith("txt")]
    for model_type in model_types:
        model_name = dir_name+"/"+model_type+'/'
        score_class = parse_model_class(model_name, style_type)
        score_sem = parse_model_sem(model_name, style_type)
        #score_sem = (score_sem-0.828)/0.172 
        if model_type=="memory":
            print dir_name, "\t", model_type, "\t\t\t", score_class, "\t\t", score_sem,  "\t", score_class*score_sem/(score_class+score_sem)
        else:
            print dir_name, "\t", model_type, "\t\t", score_class, "\t\t", score_sem, "\t", score_class*score_sem/(score_class+score_sem)
        res_class.append(score_class)
        res_sem.append(score_sem)

    print "==============================================================================="
    return res_class, res_sem


def main():
    #dir_names = ["test", "test1", "test2", "test3", "test4", "test5", "test6", "test7", "test8", "test9", "test11", "test12"]
    dir_names = ["test1", "test2", "test3"]
    final_score = []
    for dir_name in dir_names:
        res_score = parse_dir(dir_name)

        final_score.append(res_score)

    pkl.dump((final_score), open("model1.pkl", "wb"))

if __name__=="__main__":
    main()

