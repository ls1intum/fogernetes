from os import listdir
from os.path import isfile, join
from datetime import datetime

import SocketServer
import threading

import requests

import cv2
import pickle
import numpy as np
import struct

from ..settings import FOG_PATH, HOST, \
    CAMERA_PORT, CLIENT_PORT, \
    CENTRAL_HOST, CENTRAL_PORT


class CameraServer(SocketServer.BaseRequestHandler):
    def setup(self):
        major = cv2.__version__.split(".")[0]
        if int(major) > 2:
            self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        else:
            self.fourcc = cv2.cv.FOURCC(*'XVID')
        timestring = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')[:-3]
        self.filename = "output/fog/output-%s.avi" % timestring
        self.fps = 20
        self.writer = None

    def handle(self):
        (h, w) = (None, None)
        zeros = None

        data = b""
        payload_size = struct.calcsize("L")

        while True:
            print "Reading data from stream..."
            break_stream = False
            while len(data) < payload_size:
                tmp = self.request.recv(4096)
                if not tmp:
                    break_stream = True
                    break
                data += tmp
            if break_stream:
                break
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("L", packed_msg_size)[0]
            while len(data) < msg_size:
                data += self.request.recv(4096)
            print "Creating initial frame..."
            frame_data = data[:msg_size]
            data = data[msg_size:]

            frame = pickle.loads(frame_data)
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if self.writer is None:
                print "Creating Writer Object..."
                (h, w) = frame.shape[:2]
                self.writer = cv2.VideoWriter(self.filename, self.fourcc, self.fps, (w * 2, h * 2), True)
                zeros = np.zeros((h, w), dtype="uint8")

            print "Creating new frame..."
            # (B, G, R) = cv2.split(frame)
            # R = cv2.merge([zeros, zeros, R])
            # G = cv2.merge([zeros, G, zeros])
            # B = cv2.merge([B, zeros, zeros])

            cv2.putText(frame, "Fog Computing is awesome!", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

            output = np.zeros((h, w, 3), dtype="uint8")
            output[0:h, 0:w] = frame
            # output[0:h, w:w * 2] = R
            # output[h:h * 2, w:w * 2] = G
            # output[h:h * 2, 0:w] = B

            print "Writing to output file..."
            self.writer.write(output)
            # https://gist.github.com/keithweaver/4b16d3f05456171c1af1f1300ebd0f12

            print "Loop closed."

    def finish(self):
        if self.writer is not None:
            print "Releasing Video Writer..."
            self.writer.release()
        print "Request Finished."
        print "Uploading to Central..."
        files = {'file': open(self.filename, 'rb')}
        requests.post("http://%s:%d/upload" % (CENTRAL_HOST, CENTRAL_PORT), files=files)
        print "Uploading finished."


class ClientServer(SocketServer.BaseRequestHandler):
    def handle(self):
        files = [f for f in listdir(FOG_PATH) if isfile(join(FOG_PATH, f))]
        # Send the second to last file, last one could still be written
        filename = join(FOG_PATH, sorted(files)[-2])
        print "Sending file: %s" % filename
        f = open(filename, 'rb')
        l = f.read(1024)
        while l:
            self.request.send(l)
            l = f.read(1024)
        f.close()
        print "File sent."


class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


def middleman_main():
    try:
        global TDC_servers
        global TDC_server_threads

        TDC_servers = []
        TDC_server_threads = []

        TDC_servers.append(ThreadedServer((HOST, CAMERA_PORT), CameraServer))
        TDC_servers.append(ThreadedServer((HOST, CLIENT_PORT), ClientServer))

        for TDC_server in TDC_servers:
            TDC_server_threads.append(threading.Thread(target=TDC_server.serve_forever))

        for TDC_server_thread in TDC_server_threads:
            TDC_server_thread.setDaemon(True)
            TDC_server_thread.start()

        for TDC_server_thread in TDC_server_threads:
            TDC_server_thread.join()
    finally:
        print('quitting servers')

        for TDC_server in TDC_servers:
            TDC_server.server_close()