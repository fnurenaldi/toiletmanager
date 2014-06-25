from flask import render_template, url_for, redirect, flash, request
from flask.ext.socketio import SocketIO, emit

from toilet_app import app, socketio

MAIN_TOILET = 1
SECOND_TOILET = 2

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status/<int:toilet_id>', methods=["POST", "GET"])
def status_update(toilet_id):
    
    status = None
    if request.method == 'POST':
        status = request.json['status']
        
    else:
        status = request.args.get('status')

    if MAIN_TOILET == toilet_id:
        socketio.emit('main toilet status',
                      {'data': status},
                      namespace='/test')

    elif SECOND_TOILET == toilet_id:
        socketio.emit('second toilet status',
                      {'data': status},
                      namespace='/test')
    return "ok"
        

@socketio.on('connect', namespace='/test')
def test_connect():
    socketio.emit('main toilet status',
                      {'data': 'available'},
                      namespace='/test')
    socketio.emit('second toilet status',
              {'data': 'available'},
              namespace='/test')

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


