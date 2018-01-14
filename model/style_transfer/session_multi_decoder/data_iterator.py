import numpy

import cPickle as pkl
import gzip


def fopen(filename, mode='r'):
    if filename.endswith('.gz'):
        return gzip.open(filename, mode)
    return open(filename, mode)


class TextIterator:
    """Simple Bitext iterator."""
    def __init__(self, source, target, senti,
                 source_dict, target_dict,
                 batch_size=128,
                 maxlen=100,
                 n_words_source=-1,
                 n_words_target=-1,
                 val=False):
        self.source = [fopen(source, 'r'), fopen(source, 'r')]
        self.target = [fopen(target, 'r'), fopen(target, 'r')]
        self.senti = [fopen(senti, 'r'), fopen(senti, 'r')]
        self.val_flag = val
        with open(source_dict, 'rb') as f:
            self.source_dict = pkl.load(f)
        with open(target_dict, 'rb') as f:
            self.target_dict = pkl.load(f)

        self.batch_size = batch_size
        self.maxlen = maxlen

        self.n_words_source = n_words_source
        self.n_words_target = n_words_target

        self.source_buffer = [[],[]]
        self.target_buffer = [[],[]]
        self.senti_buffer = [[],[]]
        self.k = batch_size * 20

        self.style_index = 0
        self.end_of_data = [False, False]

    def __iter__(self):
        return self

    def reset(self, index):
        if self.val_flag:
            self.source[1-index].seek(0)
            self.target[1-index].seek(0)
            self.senti[1-index].seek(0)
        self.source[index].seek(0)
        self.target[index].seek(0)
        self.senti[index].seek(0)
            
    def next(self):
        if self.style_index%2==0:
            s_index = 0
        else:
            s_index = 1
        self.style_index += 1

        if self.end_of_data[s_index]:
            self.end_of_data[s_index] = False
            self.reset(s_index)
            raise StopIteration

        source = []
        target = []
        senti = []

        # fill buffer, if it's empty
        assert len(self.source_buffer[s_index]) == len(self.target_buffer[s_index]), 'Buffer size mismatch!'
        assert len(self.source_buffer[s_index]) == len(self.senti_buffer[s_index]), 'Buffer size mismatch!'

        if len(self.source_buffer[s_index]) == 0:
            for k_ in xrange(self.k):
                ss = self.source[s_index].readline()
                if ss == "":
                    break
                tt = self.target[s_index].readline()
                if tt == "":
                    break
                st = self.senti[s_index].readline()
                if st == "":
                    break
                if st.strip()!=str(s_index):
                    continue

                self.source_buffer[s_index].append(ss.strip().split())
                self.target_buffer[s_index].append(tt.strip().split())
                self.senti_buffer[s_index].append(st.strip())

            # sort by target buffer
            tlen = numpy.array([len(t) for t in self.target_buffer[s_index]])
            tidx = tlen.argsort()

            _sbuf = [self.source_buffer[s_index][i] for i in tidx]
            _tbuf = [self.target_buffer[s_index][i] for i in tidx]
            _stbuf = [self.senti_buffer[s_index][i] for i in tidx]

            self.source_buffer[s_index] = _sbuf
            self.target_buffer[s_index] = _tbuf
            self.senti_buffer[s_index] = _stbuf

        if len(self.source_buffer[s_index]) == 0 or len(self.target_buffer[s_index]) == 0 or len(self.senti_buffer[s_index]) == 0 :
            self.end_of_data[s_index] = False
            self.reset(s_index)
            raise StopIteration

        try:

            # actual work here
            while True:

                # read from source file and map to word index
                try:
                    ss = self.source_buffer[s_index].pop()
                except IndexError:
                    break
                ss = [self.source_dict[w] if w in self.source_dict else 1
                      for w in ss]
                if self.n_words_source > 0:
                    ss = [w if w < self.n_words_source else 1 for w in ss]

                # read from source file and map to word index
                tt = self.target_buffer[s_index].pop()
                tt = [self.target_dict[w] if w in self.target_dict else 1
                      for w in tt]
                if self.n_words_target > 0:
                    tt = [w if w < self.n_words_target else 1 for w in tt]

                #read from senti file
                st = self.senti_buffer[s_index].pop()
                st = int(st)

                if len(ss) > self.maxlen and len(tt) > self.maxlen:
                    continue

                source.append(ss)
                target.append(tt)
                senti.append(st)

                if len(source) >= self.batch_size or \
                        len(target) >= self.batch_size or \
                            len(senti) >= self.batch_size :
                    break
        except IOError:
            self.end_of_data[s_index] = True

        if len(source) <= 0 or len(target) <= 0:
            self.end_of_data[s_index] = False
            self.reset(s_index)
            raise StopIteration

        return source, target, senti, s_index
