import os

from flask import render_template, flash, request, send_from_directory
from flask_uploads import UploadNotAllowed

from app import app
from .uploads import files


@app.route('/videos')
def video_feed():
    videos = os.listdir(app.config["UPLOADED_FILES_DEST"])
    videos = sorted([video for video in videos
                     if video.endswith(('mp4', 'avi'))])
    # print videos
    return render_template('videos.html', videos=videos)


@app.route('/video_show/<video_name>')
def video_show(video_name):
    return render_template('video.html', filesrc=files.url(video_name))


@app.route('/upload', methods=['POST'])
def video_upload():
    if request.method == 'POST' and 'file' in request.files:
        try:
            filename = files.save(request.files['file'], folder=".")
            flash("File saved: %s" % filename)
        except UploadNotAllowed:
            flash("The upload was not allowed")
        return "success", 200
    else:
        return "fail", 403


@app.route('/uploads/<path:folder>')
def show_upload(folder):
    path = os.path.join(app.config["UPLOADED_FILES_DEST"], folder)
    return send_from_directory(os.path.dirname(path),
                               os.path.basename(path))
