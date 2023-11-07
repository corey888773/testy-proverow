# !/bin/bash

totalNumber=`ls | grep \.in$ | wc -l`
currentNumber=1

for f in *.in
do
	dfg2tptp $f $f.p
done

for f in ./*.p
do
	echo Currently processed formula: $f, $currentNumber / $totalNumber
	currentNumber=$((currentNumber+1))
	
	$VAMPIRE_PATH $f | sed 's/% //'> ./Results/$f.vampire.out
	$EPROVER_PATH --cpu-limit=15 -sR $f | tail -n 20 | sed 's/# //' > ./Results/$f.e.out
	rm $f
done

python3 ResultAnalysis.py