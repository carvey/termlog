import json
from os import listdir, stat
from os.path import isfile, join, expanduser

from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, emit, send

# initialize Flask
app = Flask(__name__, 
        template_folder='conlog/dist',
        static_folder='conlog/dist',
        static_url_path='')

socketio = SocketIO(app)

ROOMS = {} # dict to track active rooms
storage_path = expanduser("~/shlogs/")
host_logs = []

@app.route('/')
def index():
    return "Hello"

@socketio.on('push-log', namespace='/submit')
def on_log_pushed(data):
    name = data['name']
    command = data['command']
    add_command(name, command)
    
    # TODO: is this sending data back to the sender?
    socketio.emit('append_command', command, room=name)

def add_command(name, command):
    path = join(storage_path, name)
    # Ensure a log already exists for someone with this name, and add the command to it
    fle = open(path, 'a')
    if stat(path).st_size == 0:
        socketio.emit('host_added', name, broadcast=True)
    
    fle.write(command) 
    fle.write("\n")

def get_log_hosts():
    host_logs = [fle for fle in listdir(storage_path) if isfile(join(storage_path, fle))]
    return host_logs

def join_host_room(new_room, old_room=None):

    if old_room:
        leave_room(old_room)

    join_room(new_room)

@socketio.on('log_hosts')
def on_get_hosts():
    host_logs = get_log_hosts()
    emit('recv_log_hosts', host_logs)

@socketio.on('pull_log')
def on_get_log(log_name):
    host_logs = get_log_hosts()

    # if log exists, read it and send data to user
    if log_name in host_logs:
        log = open(join(storage_path, log_name)).readlines()
        join_host_room(log_name)
        emit('pull_log', {"log": log})


if __name__ == '__main__':
    socketio.run(app, debug=True)
