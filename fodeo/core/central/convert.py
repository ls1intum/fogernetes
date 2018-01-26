import schedule
import time
import os

import subprocess

from . import config

# ffmpeg -i input.avi -c:v libx264 -crf 19 -preset slow -c:a libfdk_aac -b:a 192k -ac 2 out.mp4


def convert():
    print "Converting .avi files..."
    videos = os.listdir(config.UPLOADED_FILES_DEST)
    videos = [video for video in videos if video.endswith('avi')]
    print "Files to convert: videos"

    for video in videos:
        video_name = video.split('.')[0]
        print "Converting: " + video
        subprocess.call(
            'ffmpeg -i "%s/%s.avi" -c:v libx264 -crf 19 -preset slow -c:a libfdk_aac -b:a 192k -ac 2 "%s/%s.mp4"' %
            (config.UPLOADED_FILES_DEST, video_name, config.UPLOADED_FILES_DEST, video_name),
            shell=True)
        os.remove(os.path.join(config.UPLOADED_FILES_DEST, video))


def schedule_main():
    print "Convert directory: %s" % config.UPLOADED_FILES_DEST
    convert()
    schedule.every(5).minutes.do(convert)
    while True:
        # print "."
        schedule.run_pending()
        time.sleep(1)
