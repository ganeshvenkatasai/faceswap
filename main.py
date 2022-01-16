#! /usr/bin/env python
import os
import cv2
import argparse

from face_detection import select_face
from face_swap import face_swap


if __name__ == '__main__':
 

    # Read images
    src_img = cv2.imread("source.jpg")
    dst_img = cv2.imread("destination.jpg")

    # Select src face
    src_points, src_shape, src_face = select_face(src_img)
    # Select dst face
    dst_points, dst_shape, dst_face = select_face(dst_img)

    if src_points is None or dst_points is None:
        print('Detect 0 Face !!!')
        exit(-1)

    output = face_swap(src_face, dst_face, src_points, dst_points, dst_shape, dst_img)

 

    cv2.imwrite("output.jpg", output)


