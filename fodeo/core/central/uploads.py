from flask_wtf import Form
from flask_uploads import UploadSet, configure_uploads
from app import app

files = UploadSet('files', app.config['ALLOWED_EXTENSIONS'])
configure_uploads(app, files)


class UploadForm(Form):
    pass
