#!/bin/bash

# change dir
cd ~/Public/hdw/camera.timelapse/02.git/time_lapsed

# hostname
HOST=`hostname`

function shot_tl() {

    # get current date
    DATE=$(date +"%Y-%m.%d_%H%M")

    # take JPG capture
    raspistill -a 12 -h 480 -w 640 -t 60000 -tl 2000 --nopreview -o ./photos/${HOST}_${DATE}_%03d.jpg

} # shot

function shot_1() {

    # get current date
    DATE=$(date +"%Y-%m.%d_%H%M%S")

    # take JPG capture
    raspistill -a 12 -h 480 -w 640 -t 100 --nopreview -o ./photos/${HOST}_${DATE}.jpg

} # shot

# get shot
# for i in {1..10} ; do shot_1 ; done

# get shot
shot_tl
