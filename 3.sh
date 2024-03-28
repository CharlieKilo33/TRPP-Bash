#!/bin/bash

file="/home/mike/scripts/system_info.txt"

while IFS= read -r line; do
    echo "$line"
done < "$file"
