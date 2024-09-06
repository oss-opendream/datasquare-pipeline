import os
import time

class FileRotator:
    def __init__(self, base_filename, max_bytes=0, interval_seconds=0):
        self.base_filename = base_filename
        self.max_bytes = max_bytes
        self.interval_seconds = interval_seconds
        self.start_time = time.time()
        self.current_file = self._open_new_file()

    def _open_new_file(self):
        filename = f"{self.base_filename}"
        return open(filename, mode='a', encoding='utf-8')

    def _should_rollover(self, message):
        if self.max_bytes > 0:
            self.current_file.seek(0, os.SEEK_END)
            if self.current_file.tell() + len(message) >= self.max_bytes:
                return True
        if self.interval_seconds > 0:
            if time.time() - self.start_time >= self.interval_seconds:
                return True
        return False

    def write(self, message):
        flag = False
        if self._should_rollover(message):
            self.current_file.close()
            self.current_file = self._open_new_file()
            # self.current_file = self.base_filename
            self.start_time = time.time()
            flag = True

        self.current_file.write(message)
        self.current_file.flush()
        return flag
    
    def close(self):
        if self.current_file:
            self.current_file.close()