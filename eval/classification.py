'''Trains a LSTM on the IMDB sentiment classification task.
The dataset is actually too small for LSTM to be of any advantage
compared to simpler, much faster methods such as TF-IDF + LogReg.
Notes:

- RNNs are tricky. Choice of batch size is important,
choice of loss and optimizer is critical, etc.
Some configurations won't converge.

- LSTM loss decrease patterns during training can be quite different
from what you see with CNNs/MLPs/etc.
'''
import numpy as np
np.random.seed(1337)  # for reproducibility
import random
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Activation, Embedding
from keras.layers import LSTM
from keras.models import model_from_json
import tensorflow as tf

import cPickle as pkl
import sys
from Tool import get_sub_dirnames

max_features = 80000
maxlen = 20  # cut texts after this number of words (among top max_features most common words)
batch_size = 128


def get_date():
    word_bench = 2
    word_count = dict()
    word_index = dict()

    train_data = open("train/q_train.txt", "r").readlines()
    val_data = open("train/q_val.txt", "r").readlines()
    style_train_data = open("train/s_train.txt", "r").readlines()
    style_val_data = open("train/s_val.txt", "r").readlines()

    for line in train_data:
        line = line.strip()
        for word in line.split():
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    word_count = sorted(word_count.items(), lambda x,y : cmp(x[1],y[1]), reverse=True)


    #map word to index
    index_iter = 3
    for i in word_count:
        if i[1]>=word_bench:
            word_index[i[0]] = index_iter
            index_iter += 1
    assert len(word_index)==index_iter-3, "word_index count wrong"
    print "filter word_count:", len(word_index)

    style_train_data = map(lambda x: int(x.strip()), style_train_data)
    style_train_data0 = np.array(style_train_data)
    style_train_data = []
    count0, count1 = 0,0
    #get sentence with index
    sent_index=[]
    for ii,line in enumerate(train_data):
        x=[1,]
        for i in line.strip().split():
            if word_index.has_key(i):
                x.append(word_index[i])
            else:
                x.append(2)
                #what to do, if the word is not in the index
        if count0>99000 and style_train_data0[ii]==0:
            continue
        elif style_train_data0[ii]==0:
            count0 += 1
        if count1>99000 and style_train_data0[ii]==1:
            continue
        elif style_train_data0[ii]==1:
            count1 += 1
        sent_index.append(x)
        style_train_data.append(style_train_data0[ii])
    
    random.seed(1027)
    random.shuffle(sent_index)
    random.seed(1027)
    random.shuffle(style_train_data)

    sent_index_train = np.array(sent_index)
    print "sentence train number:",sent_index_train.shape[0]
    style_train_data = np.array(style_train_data)
    sent_index = []
    for line in val_data:
        x=[1,]
        for i in line.strip().split():
            if word_index.has_key(i):
                x.append(word_index[i])
            else:
                x.append(2)
                #what to do, if the word is not in the index
        sent_index.append(x)
    sent_index_val = np.array(sent_index)
    print "sentence val number:",sent_index_val.shape[0]



    style_val_data = map(lambda x: int(x.strip()), style_val_data)
    style_val_data = np.array(style_val_data)

    assert style_train_data.shape[0]==sent_index_train.shape[0], "label length error"
    assert style_val_data.shape[0]==sent_index_val.shape[0], "label length error"

    #save
    f = open(r"./model/train.pkl",'wb')
    pkl.dump(( (sent_index_train, style_train_data), (sent_index_val, style_val_data) ), f )

    f = open(r"./model/word_index.pkl",'wb')
    pkl.dump(word_index,f)

    sent_label1 = np.array([1 if i==1. else 0. for i in style_train_data])
    sent_label0 = np.array([1 if i==0. else 0. for i in style_train_data])
    print "senti_pos: "+str(sent_label1.sum())
    print "senti_neg: "+str(sent_label0.sum())


def train():
    
    print 'Loading data...'
    (X_train, y_train), (X_test, y_test) = pkl.load(open("./model/train.pkl",'rb'))
    print len(X_train), 'train sequences'
    print len(X_test), 'test sequences'

    print 'Pad sequences (samples x time)'
    X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
    X_test = sequence.pad_sequences(X_test, maxlen=maxlen)
    print 'X_train shape:', X_train.shape
    print 'X_test shape:', X_test.shape 

    #print y_test[:100]
    print 'Build model...'
    model = Sequential()
    model.add(Embedding(max_features, 128))
    model.add(LSTM(128, dropout_W=0.2, dropout_U=0.2))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    # try using different optimizers and different optimizer configs
    model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

    print 'Train...'
    model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=2,
          validation_data=(X_test, y_test))
    score, acc = model.evaluate(X_test, y_test,
                            batch_size=batch_size)
    print 'Test score:', score
    print 'Test accuracy:', acc

    json_string = model.to_json()  
    open('./model/model_architecture.json','w').write(json_string)  
    model.save_weights('./model/model_weights.h5')  

def get_test_data(test_data_path):
    file_sent = open(test_data_path,'r')
    word_index = pkl.load(open("model/word_index.pkl",'rb'))
    sent_index = []
    while True:
        line=file_sent.readline()
        if line=="":
            break
        line = line.strip()
        seg_list = line.split()
        x=[1,]
        for i in seg_list:
            if word_index.has_key(i):
                x.append(word_index[i])
            else:
                x.append(2)
                #what to do, if the word is not in the index
        sent_index.append(x)
    sent_index = np.array(sent_index)
    print "test sentence number:",sent_index.shape[0]
    return sent_index

def test(test_dir_name):
    model = model_from_json(open('./model/model_architecture.json').read())  
    model.load_weights('./model/model_weights.h5')
    

    #subdir_names = ['multi_decoder', 'embedding', 'memory']
    subdir_names = get_sub_dirnames(test_dir_name)
    subdir_names = [i for i in subdir_names if not i.endswith("txt")]

    for dir_name in subdir_names:
        for index_name in ["0", "1"]:
            test_x = get_test_data(test_dir_name + "/"+ dir_name +"/style"+ index_name +".txt")
            test_x = sequence.pad_sequences(test_x, maxlen=maxlen)
            print "test_x shape:"+str(test_x.shape)   
            scores=model.predict_proba(test_x)
            f = open(test_dir_name + "/"+ dir_name +"/style"+ index_name +"_classification.txt", "w")
            for score in scores:
                f.write(str(score[0])+"\n")
            f.close()
    return



def print_help():
    print "Usage python class.py data|train|test"


if __name__=="__main__":
    if len(sys.argv)==1:
        print_help()
        exit()

    if sys.argv[1]=="data":
        get_date()
    elif sys.argv[1]=="train":
        train()
    elif sys.argv[1]=="test":
        test(sys.argv[2])
    else:
        print_help()

