# -*- coding: utf-8 -*-
"""
captura um frame via openCV
"""
# < imports >--------------------------------------------------------------------------------------

# python library
import argparse
import logging
import sys

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
                      help="frame height. default is '480'.")
    l_ap.add_argument("-w", "--width", required=False, type=int, default=640,
                      help="frame width. default is '640'.")
    l_ap.add_argument("-o", "--output", required=True, default="frame.jpg",
                      help="output image file.")
    l_ap.add_argument("-p", "--port", required=False, type=int, default=0,
                      help="input port.")

    l_args = vars(l_ap.parse_args())

    # arguments
    li_height = int(l_args["height"])
    li_width = int(l_args["width"])
    ls_output = l_args["output"]
    li_port = int(l_args["port"])

    l_cap = cv2.VideoCapture(li_port)
    assert l_cap

    # diminui a resolução
    l_cap.set(cv2.CAP_PROP_FRAME_WIDTH, li_width)
    l_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, li_height)

    # captura o frame
    lv_ok, l_image = l_cap.read()

    if lv_ok:
        # grava o frame
        cv2.imwrite(ls_output, l_image)

    # libera a camera
    l_cap.release()

# -------------------------------------------------------------------------------------------------
# this is the bootstrap process

if "__main__" == __name__:
    # logger
    logging.basicConfig(level=logging.INFO)

    # disable logging
    # logging.disable(sys.maxint)

    # run application
    sys.exit(main())

# < the end >--------------------------------------------------------------------------------------
