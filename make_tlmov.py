# -*- coding: utf-8 -*-
"""
captura um video via openCV
"""
# < imports >--------------------------------------------------------------------------------------

# python library
import argparse
import datetime
import logging
import platform
import sys
import time

# openCV
import cv2

# -------------------------------------------------------------------------------------------------
def main():
    """
    main
    """
    # construct the argument parser and parse the arguments
    l_ap = argparse.ArgumentParser()
    assert l_ap

    l_ap.add_argument("-e", "--height", required=False, type=int, default=480,
                      help="frame height. default is 480.")
    l_ap.add_argument("-w", "--width", required=False, type=int, default=640,
                      help="frame width. default is 640.")
    l_ap.add_argument("-d", "--duracao", required=False, type=int, default=1,
                      help="recording duration in minutes. default is 1")
    l_ap.add_argument("-f", "--fps", required=False, type=int, default=10,
                      help="frames per second. default is 10")
    l_ap.add_argument("-i", "--interval", required=False, type=int, default=1,
                      help="interval between frames in sec. default is 1")
    l_ap.add_argument("-o", "--output", required=False, default="x",
                      help="output video file.")
    l_ap.add_argument("-p", "--port", required=False, type=int, default=0,
                      help="input port.")
    l_ap.add_argument("-s", "--still", action='store_true',
                      help="keep still frames.")

    # parse args
    l_args = vars(l_ap.parse_args())
    logging.debug("args: %s.", str(l_args))

    # data atual
    ldt_date = datetime.datetime.now()

    # have output ?
    if "x" == l_args["output"]:
        # hostname
        ls_hostname = platform.uname()[1]
        logging.debug("hostname: %s.", str(ls_hostname))

        # data
        ls_data = datetime.datetime.strftime(ldt_date, "%Y-%m.%d")

        # output video name
        ls_output_fn = "movies/{}_{}".format(ls_hostname, ls_data)
        logging.debug("output_fn: %s.", str(ls_output_fn))

    # senão,...
    else:
        # output video name
        ls_output_fn = l_args["output"]
        logging.debug("output_fn: %s.", str(ls_output_fn))

    # intervalo dos frames em segundos
    li_interval = l_args["interval"]
    logging.debug("interval: %s.", str(li_interval))

    # open video
    l_cap = cv2.VideoCapture(int(l_args["port"]))
    assert l_cap

    # diminui a resolução
    l_cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(l_args["width"]))
    l_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(l_args["height"]))

    # frame size
    lt_size = (int(l_cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
               int(l_cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    # create video codec, compression format, and color/pixel format
    l_fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    # create video writer
    l_video = cv2.VideoWriter(ls_output_fn + ".mp4", l_fourcc, int(l_args["fps"]), lt_size)

    # for low quality webcams...
    for _ in range(42):
        # ...discard the starting unstable frames
        l_cap.read()

    # end time of recording
    ldt_delta = ldt_date + datetime.timedelta(minutes=int(l_args["duracao"]))
    ldt_delta = ldt_delta.time()

    # hora atual
    ldt_hour = datetime.datetime.now().time()

    # capture frames to video
    while ldt_hour < ldt_delta:
        # tempo inicial em segundos
        lf_ini = time.time()

        # capture frame
        _, l_frame = l_cap.read()
        # write to video
        l_video.write(l_frame)

        # optional
        if l_args["still"]:
            # in case you need the frames for gif or so
            ls_filename = "photos/{}_{}_{}.jpg".format(ls_hostname, ls_data, int(time.time()))
            # write PNG file
            cv2.imwrite(ls_filename, l_frame)

        # tempo final em segundos e cálculo do tempo decorrido
        lf_dif = time.time() - lf_ini

        # está adiantado ?
        if li_interval > lf_dif:
            # permite o scheduler
            time.sleep(li_interval - lf_dif)

        # hora atual
        ldt_hour = datetime.datetime.now().time()

    # release videoWriter
    l_video.release()
    # release camera
    l_cap.release()

# -------------------------------------------------------------------------------------------------
# this is the bootstrap process

if "__main__" == __name__:

    # logger
    logging.basicConfig(level=logging.WARNING)

    # disable logging
    # logging.disable(sys.maxsize)

    # run application
    sys.exit(main())

# < the end >--------------------------------------------------------------------------------------
