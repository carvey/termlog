import threading
import socketserver
import json
import re
import unicodedata

from shlex import quote
from os.path import join
from os import popen

class LogAggregator:
    
    def __init__(self, store=None, forward=None):
        self.store = store
        self.forward = forward

    def recv_lines(self, path):
        store = join(self.store, self.extract_log_name(path))
        cmd = "cat %s | perl -pe 's/\e([^\[\]]|\[.*?[a-zA-Z]|\].*?\a)//g' | col -b" % quote(path)
        output = popen(cmd).read()

        if output[-2:] == "$\n" or output[-2:] == "#\n":
            output = output[:-1] + " "

        fle = open(store, 'a')
        fle.write(output)
        fle.close()

        open(path, 'w').close()

    def extract_log_name(self, path):
        name = path.split('/')[-1]
        name = name.split('.')[0]
        return name

    def forward(self):
        pass

    def store_locally(self, log, lines):
        log_path = join(self.store, log)
        log = open(log_path, 'a')
        
        lines_str = self.format_lines(lines)
        log.write(lines_str)

        log.close()

