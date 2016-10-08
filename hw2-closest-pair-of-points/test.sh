#!/bin/bash

N=1
#for i in 125 250 500 1000 2000 4000 8000
for i in 16000
do
    res=$(python main.py -g $i --brutal -t $N | cut -d' ' -f3)
    echo $i $res
    echo $i $res >> brutal.txt
done

#for i in 125 250 500 1000 2000 4000 8000 16000 32000 64000 128000 256000 512000 1024000
for i in 2048000
do
    res=$(python main.py -g $i --nlogn -t $N | cut -d' ' -f2)
    echo $i $res
    echo $i $res >> nlogn.txt
done
