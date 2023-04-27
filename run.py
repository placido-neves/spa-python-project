from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from threading import Timer
from subprocess import Popen

class Runner:
    _proc = None
    _handle_func = None
    
    @staticmethod
    def run():
        Runner._proc = Popen(['python3','runner.py'])
        
    @staticmethod
    def handle_file_modified(event):
        if Runner._proc != None:
            Runner._proc.kill()
        if Runner._handle_func != None:
            Runner._handle_func.cancel()
        Runner._handle_func = Timer(1, Runner.run)
        Runner._handle_func.start()

Runner.run()
file_watcher = Observer()
file_modified_event_handler = PatternMatchingEventHandler(patterns = ["*"], ignore_patterns = ["__pycache__", "cli_service/app.py",'run.py'])
file_modified_event_handler.on_modified = Runner.handle_file_modified
file_watcher.schedule(file_modified_event_handler,".",recursive =True)

file_watcher.start()

try:
    while file_watcher.is_alive():
        file_watcher.join(1)
except KeyboardInterrupt:
    file_watcher.stop()
    
file_watcher.join()