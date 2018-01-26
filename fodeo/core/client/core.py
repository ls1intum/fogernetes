import socket

from ..settings import CLIENT_HOST, CLIENT_PORT


def client_main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((CLIENT_HOST, CLIENT_PORT))

    f = open('output/edge/last_video.avi', 'wb')

    print "Receiving..."
    l = s.recv(1024)
    while l:
        f.write(l)
        l = s.recv(1024)
    f.close()
    print "Done Receiving"
    s.close()
