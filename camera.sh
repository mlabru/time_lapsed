#!/bin/bash

# change dir
cd ~/Public/hdw/camera.timelapse

# make 8 hours movie (8*60 = 480 min)
python3 make_tlmov.py -d 480
