#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=4:00:00
#PBS -N session1_default
#PBS -A course
#PBS -q ShortQ

#source ~/v_python/bin/activate
export THEANO_FLAGS=device=cpu,floatX=float32

python ./translate.py -n -p 10 \
	models/model.npz  \
	../../data/dict.pkl \
	../../data/dict.pkl \
	../../data/q_test.txt \
	./q_test_style0.txt



python ./translate1.py -n -p 10 \
	models/model.npz  \
	../../data/dict.pkl \
	../../data/dict.pkl \
	../../data/q_test.txt \
	./q_test_style1.txt
