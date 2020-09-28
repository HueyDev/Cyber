#!/bin/bash

sudo rm /bin/cyber &> /dev/null
sudo rm -r /bin/Cyber_Commands &> /dev/null
sudo rm -r /bin/Config_Files &> /dev/null

sudo cp cyber /bin/cyber
sudo cp -r Cyber_Commands /bin/Cyber_Commands
sudo cp -r Config_Files /bin/Config_Files
