#!/bin/bash

if [ $# -lt 2 ]; then
    echo "Insufficient arguments passed; pass 2 args!"
    exit 1
elif [ $# -gt 2 ]; then
    echo "Too many arguments passed! pass 2 args."
    exit 1
fi

man "$1" | grep --color -i "$2"
