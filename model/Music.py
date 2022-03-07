from datetime import datetime
from typing import Any
from helper import Helper


class Music:
    timestamp: datetime
    event: str
    music_track: str

    def __init__(self, timestamp: datetime, event: str, music_track: str) -> None:
        self.timestamp = timestamp
        self.event = event
        self.music_track = music_track

    @staticmethod
    def fromDict(obj: Any) -> 'Music':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        music_track = Helper.fromString(obj.get("MusiscTrack", ""))
        return Music(timestamp, event, music_track)
