import json
from os import listdir
from os.path import isfile, join, expanduser

from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit

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

@socketio.on('connect')
def on_connect():
    host_logs = get_log_hosts()
    emit('recv_log_hosts', host_logs)

@socketio.on('recv-log', namespace='/submit')
def on_log(data):
    name = data['name']
    command = data['command']
    add_command(name, command)
    
    # TODO: is this sending data back to the sender?
    socketio.emit('command_added', data, broadcast=True)

def add_command(name, command):
    # Ensure a log already exists for someone with this name, and add the command to it
    fle = open(join(storage_path, name, '.log'), 'a')
    fle.write(command) 
    fle.write("\n")

def get_log_hosts():
    host_logs = [fle for fle in listdir(storage_path) if isfile(join(storage_path, fle))]
    host_logs = [host.replace('.log', '') for host in host_logs]
    return host_logs

@socketio.on('log_hosts')
def on_get_hosts():
    host_logs = get_log_hosts()
    emit('recv_log_hosts', host_logs)

@socketio.on('get_charles_log')
def on_get_charles_log(data):
    host_logs = get_log_hosts()
    log = open(join(storage_path, host_logs[0])).read()
    emit('recv_charles_log', {"log": log})

if __name__ == '__main__':
    socketio.run(app, debug=True)
