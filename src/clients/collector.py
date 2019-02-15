import threading
from time import sleep

from os import stat
from os.path import join
from aggregator import LogAggregator
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class CollectorAgent:

    def __init__(self, log_dir, store_path=None):
        self.observer = Observer()
        self.log_dir = log_dir

        self.store_path = join(self.log_dir, 'plaintxt/')
        self.watch_path = join(self.log_dir, 'tscript/')

    def run(self):
        aggregator = LogAggregator(store=self.store_path)

        patterns = ['*.tscript']
        event_handler = Handler(patterns=patterns, ignore_directories=True)
        setattr(Handler, 'aggregator', aggregator)
        self.observer.schedule(event_handler, self.watch_path, recursive=True)
        self.observer.start()

        try:
            while True:
                sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
            print("\n")

        self.observer.join()


class Handler(PatternMatchingEventHandler):

    @staticmethod
    def on_created(event):
        print("created: %s" % event.src_path)
        Handler.extract_file_data(event.src_path)

    @staticmethod
    def on_modified(event):
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

        Handler.aggregator.recv_lines(path, lines)


