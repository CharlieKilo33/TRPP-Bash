#!/bin/bash

directory="/home/mike/Scripts"

if [ -d "$directory" ]; then
    ls -l "$directory"
else
    echo "Directory does not exist."
fi
