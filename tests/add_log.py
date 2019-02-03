import random
import sys
from socketIO_client import SocketIO, BaseNamespace

class SubmitterNamespace(BaseNamespace):

    # this should not print
    def on_command_added(self, *args):
        print(args)

sock = SocketIO('localhost', 5000)
submitter_namespace = sock.define(SubmitterNamespace, '/submit')

if sys.argv[1]:
    name = sys.argv[1]
else:
    name = "charles%s" % random.choice(range(1,1000)) 

submitter_namespace.emit('push-log', {'name': name, 'command': 'root@kali:~# ls /var/log'})

