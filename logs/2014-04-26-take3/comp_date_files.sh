#!/bin/bash

shopt -s nullglob
glucoseFiles=(*ReadGlucoseHistory*.hex)
isigFiles=(*ReadISIGHistory*.hex)

declare -a sortedGlucoseFiles
declare -a sortedIsigFiles

# sor the glucose files
touch tmp
for i in ${glucoseFiles[@]}; do
        echo $i >> tmp
        `sort tmp -o tmp`
done

while read line; do
        sortedGlucoseFiles=(${sortedGlucoseFiles[@]} $line)
done < tmp
rm tmp

#sort the ISIG files
touch tmp
for i in ${isigFiles[@]}; do
        echo $i >> tmp
        `sort tmp -o tmp`
done

while read line; do
        sortedIsigFiles=(${sortedIsigFiles[@]} $line)
done < tmp
rm tmp

echo "" > glucoseFiles.diff
for((i=1; i<${#sortedGlucoseFiles[*]}; i++))
do
	echo "********** $sortedGlucoseFiles[$i-1] compared to $sortedGlucoseFiles[$i] *********" >> glucoseFiles.diff
	echo "diff ${sortedGlucoseFiles[(($i-1))]} ${sortedGlucoseFiles[$i]} >> glucoseFiles.diff "
	diff ${sortedGlucoseFiles[(($i-1))]} ${sortedGlucoseFiles[$i]} >> glucoseFiles.diff
done

echo "" > isigFiles.diff
for((i=1; i<${#sortedIsigFiles[*]}; i++))
do
	echo "********** $sortedIsigFiles[$i-1] compared to $sortedIsigFiles[$i] *********" >> isigFiles.diff
	echo "diff ${sortedIsigFiles[(($i-1))]} ${sortedIsigFiles[$i]} >> isigFiles.diff "
	diff ${sortedIsigFiles[(($i-1))]} ${sortedIsigFiles[$i]} >> isigFiles.diff
done


