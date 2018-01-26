import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

ALLOWED_EXTENSIONS = tuple('mp4 avi mkv'.split())
UPLOADED_FILES_DEST = os.path.join(basedir, '../../output/cloud')
UPLOADED_FILES_URL = '/uploads/'  # http://127.0.0.1:8080

DEBUG_TB_INTERCEPT_REDIRECTS = False
