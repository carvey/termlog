
from socketIO_client import SocketIO, LoggingNamespace

with SocketIO('localhost', 5000, LoggingNamespace) as socketIO:
    socketIO.emit('recv-log', {'name': 'joe', 'command': '> $ pwd'})


