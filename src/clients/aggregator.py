import threading
import socketserver
import json
import re
import unicodedata

from os.path import join

class LogAggregator:
    
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

    def __init__(self, store=None, forward=None):
        self.store = store
        self.forward = forward

    def recv_lines(self, path, lines):
        stripped_lines = []

        for line in lines:
            cleaned_line = self.clean(line)

            if cleaned_line:
                stripped_lines.append(cleaned_line)

        self.format_lines(stripped_lines, _print=True)

        if self.store:
            log_name = self.extract_log_name(path)
            self.store_locally(log_name, stripped_lines)

    def extract_log_name(self, path):
        name = path.split('/')[-1]
        name = name.split('.')[0]
        return name

    def clean(self, line):
        escaped = "".join(ch for ch in escaped if unicodedata.category(ch)[0]!="C")
        escaped = escaped.replace('\x00', '')

        if escaped == "%":
            return None

        if not escaped:
            return None

        if escaped[-1] == "$" or escaped[-1] == "#":
            escaped = escaped + " "

        return escaped
    
    def format_lines(self, lines, _print=False):
        lines_str = "\n".join(lines)
        if _print:
            print(lines_str)

        return lines_str

    def forward(self):
        pass

    def store_locally(self, log, lines):
        log_path = join(self.store, log)
        log = open(log_path, 'a')
        
        lines_str = self.format_lines(lines)
        log.write(lines_str)

        log.close()

