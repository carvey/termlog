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
    """Serve the index HTML"""
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    emit('log_hosts', {'hosts': ['blah1', 'blah2']})

def get_log_hosts():
    host_logs = [fle for fle in listdir(storage_path) if isfile(join(storage_path, fle))]
    return host_logs

@socketio.on('log_hosts')
def on_get_hosts():
    host_logs = get_log_hosts()
    emit('log_hosts', host_logs)

@socketio.on('get_charles_log')
def on_get_charles_log(data):
    host_logs = get_log_hosts()
    log = open(join(storage_path, host_logs[0])).read()
    emit('recv_charles_log', {"log": log})

#@socketio.on('create')
#def on_create(data):
#    """Create a game lobby"""
#    gm = game.Info(
#        size=data['size'],
#        teams=data['teams'],
#        dictionary=data['dictionary'])
#    room = gm.game_id
#    ROOMS[room] = gm
#    join_room(room)
#    emit('join_room', {'room': room})

if __name__ == '__main__':
    socketio.run(app, debug=True)
