import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

current_process = None

class PyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global current_process
        if event.src_path.endswith(".py"):
            if current_process and current_process.poll() is None:
                current_process.kill()
            print(f"🔄 Detected change in {event.src_path}, running debug session...")
            current_process = subprocess.Popen([
                "python3",
                "-m",
                "debugpy",
                "--listen", "0.0.0.0:5678",
                "--wait-for-client",
                event.src_path
            ])

path = "./"
event_handler = PyHandler()
observer = Observer()
observer.schedule(event_handler, path=path, recursive=True)
observer.start()

print("👀 Watching for Python file changes...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
