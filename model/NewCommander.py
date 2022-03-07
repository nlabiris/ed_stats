from datetime import datetime
from typing import Any
from helper import Helper


class NewCommander:
    timestamp: datetime
    event: str
    fid: str
    name: str
    package: str

    def __init__(self, timestamp: datetime, event: str, fid: str, name: str, package: str) -> None:
        self.timestamp = timestamp
        self.event = event
        self.fid = fid
        self.name = name
        self.package = package

    @staticmethod
    def fromDict(obj: Any) -> 'NewCommander':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        fid = Helper.fromString(obj.get("FID", ""))
        name = Helper.fromString(obj.get("Name", ""))
        package = Helper.fromString(obj.get("Package", ""))
        return NewCommander(timestamp, event, fid, name, package)
