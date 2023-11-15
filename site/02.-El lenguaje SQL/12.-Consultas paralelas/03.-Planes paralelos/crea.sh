#!/bin/bash

names=(




"01.-Parallel Scans"
"02.-Parallel Joins"
"03.-Parallel Aggregation"
"04.-Parallel Append"
"05.-Parallel Plan Tips"



"index"


)

for name in "${names[@]}"
do
  touch "$name.md"
done

