import os

class Config:
    LOG_INTERVAL = 10  # seconds
    LOG_FILE_PATH = os.path.join('logs', 'active_windows.log')
    REMOTE_SERVER_URL = "myserver.com/api/logs"
    REMOTE_LOGGING = False

    def get_config(self):
        return {
            'log_interval': self.LOG_INTERVAL,
            'remote_server_url': self.REMOTE_SERVER_URL,
            'remote_logging': self.REMOTE_LOGGING
        }

    def update_config(self, new_config):
        self.LOG_INTERVAL = new_config.get('log_interval', self.LOG_INTERVAL)
        self.REMOTE_SERVER_URL = new_config.get('remote_server_url', self.REMOTE_SERVER_URL)
        self.REMOTE_LOGGING = new_config.get('remote_logging', self.REMOTE_LOGGING)