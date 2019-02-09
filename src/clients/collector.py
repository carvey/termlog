import threading
from time import sleep

from os import stat
from aggregator import LogAggregator
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CollectorAgent:

    def __init__(self, log_dir):
        self.observer = Observer()
        self.log_dir = log_dir

    def run(self):
        aggregator = LogAggregator()
        event_handler = Handler()
        setattr(Handler, 'aggregator', aggregator)
        self.observer.schedule(event_handler, self.log_dir, recursive=True)
        self.observer.start()

        try:
            while True:
                sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_created(event):
        print("created: %s" % event.src_path)

    @staticmethod
    def on_modified(event):
        if event.is_directory:
            return None

        print("modified: %s" % event.src_path)
        Handler.extract_file_data(event.src_path)

    @staticmethod
    def on_deleted(event):
        print("deleted: %s" % event.src_path)

    @staticmethod
    def extract_file_data(path):
        if stat(path).st_size == 0:
            return None

        fle = open(path, 'r')
        lines = fle.readlines()

        Handler.aggregator.recv_lines(lines)


