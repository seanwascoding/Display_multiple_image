import cv2
import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ImageHandler(FileSystemEventHandler):
    def  __init__(self, folder_path):
        super().__init__()
        cv2.namedWindow("Image Stream", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Image Stream", 416, 416)
        self.folder_path = folder_path
        self.latest_file = None
        self.image = None

    def on_created(self, event):
        print("create start")
        if not event.is_directory and event.src_path.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            self.latest_file = event.src_path
            self.process_image()

    def on_deleted(self, event):
        print("delete start" , event.src_path , self.latest_file)
        if event.src_path == self.latest_file:
            print(f"Deleted file: {self.latest_file}")
            self.latest_file = None
            self.image = None

    def process_image(self):
        print("new image" , self.latest_file)
        time.sleep(1)
        self.image = cv2.imread(self.latest_file)

    def getImage(self):
        return self.image
        

def start():
    print('start')
    path = sys.argv[1]
    print(path)
    event_handler = ImageHandler(path)
    observer = Observer()
    observer.schedule(event_handler=event_handler, path=path, recursive=False)
    observer.start()

    try:
        while True:
            # time.sleep(1)
            frame = event_handler.getImage()
            if frame is not None:
                cv2.imshow("Image Stream", frame)
                cv2.waitKey(1)
            # else:
                # print('error')
    except KeyboardInterrupt:
        pass
    finally:
        observer.stop()
        cv2.destroyAllWindows()
        observer.join()
        print("end thread")

if __name__ == '__main__':
    start()