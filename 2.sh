#!/bin/bash

dir="/home/mike/scripts"

if [ -d "$dir" ]; then
    ls -l "$dir"
else
    echo "Directory does not exist."
fi
