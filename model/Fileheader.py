from datetime import datetime
from typing import Any
from helper import Helper


class Fileheader:
    timestamp: datetime
    event: str
    part: int
    language: str
    gameversion: str
    build: str

    def __init__(self, timestamp: datetime, event: str, part: int, language: str, gameversion: str, build: str) -> None:
        self.timestamp = timestamp
        self.event = event
        self.part = part
        self.language = language
        self.gameversion = gameversion
        self.build = build

    @staticmethod
    def fromDict(obj: Any) -> 'Fileheader':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        part = Helper.fromInteger(obj.get("part", 0))
        language = Helper.fromString(obj.get("language", ""))
        gameversion = Helper.fromString(obj.get("gameversion", ""))
        build = Helper.fromString(obj.get("build", ""))
        return Fileheader(timestamp, event, part, language, gameversion, build)
