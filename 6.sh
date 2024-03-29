#!/bin/bash

directory="/home/mike/scripts"

for file in "$directory"/*; do
    if [ -x "$file" ]; then
        echo "$file is executable."
    else 
        echo "$file is non executable."
    fi
done
