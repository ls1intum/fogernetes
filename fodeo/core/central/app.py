from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True
app.config.from_object('core.central.config')

toolbar = DebugToolbarExtension(app)

from . import views, uploads