import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from organizer import FileOrganizer
from config import WATCHED_FOLDER


class WatcherHandler(FileSystemEventHandler):
    def __init__(self) -> None:
        self.organizer = FileOrganizer()

    def on_created(self, event):
        if not event.is_directory:
            file_path = Path(event.src_path)
            self.organizer.organize(file_path)


def start_watching():
    event_handler = WatcherHandler()
    observer = Observer()
    observer.schedule(event_handler, str(WATCHED_FOLDER), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
