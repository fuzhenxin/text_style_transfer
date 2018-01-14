#encoding=utf-8

import cPickle as pkl
import numpy as np
import sys

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt


def get_data():
    res = pkl.load(open("score_np.pkl", "rb"))
    return res

def get_data_model():
    res0 = pkl.load(open("model1.pkl", "rb"))
    res1 = pkl.load(open("model2.pkl", "rb"))
    return res0, res1

def plot_co():
    score_m, score_h = get_data()
    assert len(score_m)==len(score_h), "input lenght error from file"
    
    """
    print len(score_h)
    ff = [(i,j) for i,j in zip(score_h, score_m) if i>0.8]
    print len(ff)
    score_h = [i for i,j in ff]
    score_m = [j for i,j in ff]
    print len(score_h)
    """

    fit = np.polyfit(score_h, score_m, 1)
    fit_fn = np.poly1d(fit)


    plt.figure()
    plt.plot(score_h, score_m, 'bo', score_h, fit_fn(score_h), ':k')
    #plt.scatter(score_h, score_m)
    plt.xlabel("content reservation")
    plt.ylabel("human evaluation score")
    plt.savefig("human.png")



def plot_model():
    task_data = get_data_model()

    sub_plot_id = [121, 122]
    lower_bound = [0.828657, 0.8801]
    titles = ["Paper-News Title", "Positive-Negative Review"]
    plt.figure(figsize=(10,4))
    for i in range(2):
        plt.subplot(sub_plot_id[i])
        data0, data1, data2 = task_data[i]
        lower_bound_per = lower_bound[i]
        data00 = np.array(data0[1], dtype=np.float32)
        data11 = np.array(data1[1], dtype=np.float32)
        data22 = np.array(data2[1], dtype=np.float32)
        plt.scatter(data0[0], (data00-lower_bound_per)/(1-lower_bound_per), c='g', marker='+', label="autoencoder")
        plt.scatter(data1[0], (data11-lower_bound_per)/(1-lower_bound_per), c='r', marker='o', label="multi-decoder")
        plt.scatter(data2[0], (data22-lower_bound_per)/(1-lower_bound_per), c='b', marker='^', label="style-embedding")
        plt.xlabel("transfer strength")
        plt.ylabel("content reservation")
        plt.title(titles[i])
        plt.legend()
        plt.grid(linestyle=':')
    plt.savefig("result.png")

if __name__=="__main__":
    if sys.argv[1]=="human":
        plot_co()
    elif sys.argv[1]=="model":
        plot_model()