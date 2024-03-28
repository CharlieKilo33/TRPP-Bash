#!/bin/bash

current_date=$(date)
users=$(cut -d: -f1 /etc/passwd)
system_uptime=$(uptime)

echo "Current date and time: $current_date"
echo "List of registered users: $users"
echo "System uptime: $system_uptime"

echo "Current date and time: $current_date" > system_info.txt
echo "List of registered users: $users" >> system_info.txt
echo "System uptime: $system_uptime" >> system_info.txt
