import socket

OUTPUT_PATH = "output"
FOG_PATH = OUTPUT_PATH + "/fog"
EDGE_PATH = OUTPUT_PATH + "/edge"

TEST_PATH = "test"

TEST_VIDEOS = [
    "Low_Test.mp4",
    "High_Test.mp4",
    "Surveilance_Test.mov"
]
TEST_VIDEO = "Surveilance_Test.mov"

HOST = ''
try:
    FOG_HOST = socket.gethostbyname("fodeo-fog-service")
except socket.gaierror:
    FOG_HOST = "localhost"
try:
    CENTRAL_HOST = socket.gethostbyname("fodeo-central-service")
except socket.gaierror:
    CENTRAL_HOST = "localhost"
CLIENT_HOST = "172.16.143.155"
CAMERA_PORT = 8089
CLIENT_PORT = 30090  # 8090
CENTRAL_PORT = 8080


class Config(object):
    def __init__(self):
        self.verbose = False