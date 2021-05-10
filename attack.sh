#!/bin/bash

i=0
pids=()

while [ $i -lt 10 ]
do
  ((i++))
  ./loop_discovery.sh &
  pids+=($!) 
done

read -n 1 -p Stop?;

for pid in ${pids[@]}; do
  kill $pid
done



