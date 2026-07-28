#!/bin/bash
search_conf() {
sudo find /etc -name "*.$1" -type f | sudo xargs grep "$2"
}

search_conf "$1" "$2"

