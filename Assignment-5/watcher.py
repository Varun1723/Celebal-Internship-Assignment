import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class TriggerHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".trigger"):
            subprocess.call(["export_all.bat"])

if __name__ == "__main__":
    path = "."
    observer = Observer()
    observer.schedule(TriggerHandler(), path=path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
