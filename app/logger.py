import json
import os
from datetime import datetime

class LogManager:
    def __init__(self, config):
        self.config = config
        self.ensure_log_directory()

    def ensure_log_directory(self):
        os.makedirs('logs', exist_ok=True)

    def log(self, windows):
        entry = {
            'timestamp': datetime.now().isoformat(),
            'windows': windows
        }
        
        with open(self.config.LOG_FILE_PATH, 'a') as f:
            f.write(json.dumps(entry) + '\n')

    def get_logs(self):
        logs = []
        if os.path.exists(self.config.LOG_FILE_PATH):
            with open(self.config.LOG_FILE_PATH, 'r') as f:
                for line in f:
                    logs.append(json.loads(line))
        return logs