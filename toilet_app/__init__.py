from flask import Flask, render_template, redirect, url_for
from flask.ext.socketio import SocketIO, emit

DEFAULT_APP_CONFIG = "toilet_app.config.DevelopmentConfig"

app = Flask(__name__)
app.config.from_object(DEFAULT_APP_CONFIG)
socketio = SocketIO(app)

import models
import controllers
