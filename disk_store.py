import time
import struct
import os

HEADER_FORMAT = "<LLL"


class KeyEntry:

    def __init__(self, timestamp: int, position: int, total_size: int) -> None:
        self.timestamp = timestamp
        self.position = position
        self.total_size = total_size


class DiskStorage:

    def __init__(self, file_name='data.db'):
        self.file = open(file_name, 'a+b')
        self.key_dir: Dict[str, ]

    def set(self, key: str, value: str):
        timestamp = int(time.time())
        header = struct.pack(HEADER_FORMAT, timestamp, len(key), len(value))
        data = b"".join([str.encode(key), str.encode(value)])
        self.file.write(header + data)
        os.fsync(self.file)

    def get(self, key) -> str:
        raise NotImplementedError
