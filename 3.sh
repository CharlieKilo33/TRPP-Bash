#!/bin/bash

file="/home/mike/scripts/system_info.txt"

while read -r line; do
    echo "$line"
done < "$file"
