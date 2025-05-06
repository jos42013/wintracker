import win32gui
import threading
import time
from datetime import datetime

class WindowMonitor:
    def __init__(self, log_manager):
        self.log_manager = log_manager
        self.start_monitoring()

    def get_open_windows(self):
        windows = []
        
        def callback(hwnd, _):
            if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
                windows.append(win32gui.GetWindowText(hwnd))
        
        win32gui.EnumWindows(callback, None)
        return windows

    def get_current_timestamp(self):
        return datetime.now().isoformat()

    def start_monitoring(self):
        def monitor_loop():
            while True:
                windows = self.get_open_windows()
                if windows:
                    self.log_manager.log(windows)
                time.sleep(self.log_manager.config.LOG_INTERVAL)

        thread = threading.Thread(target=monitor_loop, daemon=True)
        thread.start()