#!/bin/bash

directory="/home/mike/scripts"

for file in "$directory"/*; do
    if [ -x "$file" ]; then
        echo "$file is executable."
    fi
done
