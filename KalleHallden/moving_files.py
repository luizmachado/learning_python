from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import re

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            if src != folder_destination and re.search('^.*\.(avi|webm|mp4)$', filename) is not None:
                new_destination = filme_destination + "/" + filename
                os.rename(src, new_destination)


folder_to_track = '/home/luiz/Transferências'
folder_destination = '/home/luiz/Transferências/Arquivo'
filme_destination = '/home/luiz/Transferências/Arquivo/Videos'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()


try:
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    observer.stop()

observer.join()