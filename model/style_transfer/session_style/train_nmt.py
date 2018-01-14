import numpy
import os

from nmt import train

def main(job_id, params):
    print params
    data_name = '../../data'
    validerr = train(saveto=params['model'][0],
                    reload_=params['reload'][0],
                    dim_word=params['dim_word'][0],
                    dim=params['dim'][0],
                    n_words=params['n-words'][0],
                    n_words_src=params['n-words'][0],
                    decay_c=params['decay-c'][0],
                    lrate=params['learning-rate'][0],
                    optimizer=params['optimizer'][0],
                    maxlen=40,
                    batch_size=128,
                    valid_batch_size=128,
                    datasets=[data_name+'/q_train.txt',
                              data_name+'/r_train.txt',
                              data_name+'/s_train.txt'],
                    valid_datasets=[data_name+'/q_val.txt',
                                    data_name+'/r_val.txt',
                                    data_name+'/s_val.txt'],
                    dictionaries=[data_name+'/dict.pkl',
                                  data_name+'/dict.pkl'],
                    validFreq=1000,
                    dispFreq=100,
                    saveFreq=1000,
                    sampleFreq=1000,
                    use_dropout=params['use-dropout'][0],
                    overwrite=True,
                    
                    max_epochs=15,
                    senti_num=2,
                    senti_dim=64,
                    weight_d=1.,
                    weight_h=1.,
                    style_class=True,
                    style_adv=True,
                    adv_thre=1)
    return validerr

if __name__ == '__main__':
    main(0, {
        'model': ['models/model.npz' ,],
        'dim_word': [64],
        'dim': [32],
        'n-words': [60000],
        'optimizer': ['adadelta'],
        'decay-c': [0.],
        'use-dropout': [False],
        'learning-rate': [0.0001],
        'reload': [False]})


