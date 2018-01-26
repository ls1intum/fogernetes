import cv2
import socket
import pickle
import struct
import time
import random
from os import path

from ..settings import TEST_PATH, TEST_VIDEOS, TEST_VIDEO, FOG_HOST, CAMERA_PORT


def send_video(video):
    videoCapture = cv2.VideoCapture(video)
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((FOG_HOST, CAMERA_PORT))
    start = time.time()
    i = 0
    while i < 20:
        ret, frame = videoCapture.read()
        if not ret:
            break
        data = pickle.dumps(frame)
        to_send = struct.pack("L", len(data)) + data
        clientSocket.sendall(to_send)
        i += 1
        print "Sent frame (%i) at time:" % i, time.time() - start
    clientSocket.shutdown(1)
    clientSocket.close()


def select_video(video, r):
    if not video:
        video = path.join(TEST_PATH, TEST_VIDEO)
    if r:
        video = path.join(TEST_PATH, random.choice(TEST_VIDEOS))
    return video


def camera_main(video, n, r):
    if n == 0:
        while True:
            send_video(select_video(video, r))
    else:
        for i in range(n):
            send_video(select_video(video, r))
