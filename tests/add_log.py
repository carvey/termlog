
from socketIO_client import SocketIO, BaseNamespace

class SubmitterNamespace(BaseNamespace):

    # this should not print
    def on_command_added(self, *args):
        print(args)

sock = SocketIO('localhost', 5000)
submitter_namespace = sock.define(SubmitterNamespace, '/submit')
submitter_namespace.emit('recv-log', {'name': 'joe', 'command': '> $ ls'})


