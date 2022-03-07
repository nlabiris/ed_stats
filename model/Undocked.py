from datetime import datetime
from typing import Any
from helper import Helper


class Undocked:
    timestamp: datetime
    event: str
    station_name: str
    station_type: str
    market_id: int

    def __init__(self, timestamp: datetime, event: str, station_name: str, station_type: str, market_id: int) -> None:
        self.timestamp = timestamp
        self.event = event
        self.station_name = station_name
        self.station_type = station_type
        self.market_id = market_id

    @staticmethod
    def fromDict(obj: Any) -> 'Undocked':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        station_name = Helper.fromString(obj.get("StationName", ""))
        station_type = Helper.fromString(obj.get("StationType", ""))
        market_id = Helper.fromInteger(obj.get("MarketID", 0))
        return Undocked(timestamp, event, station_name, station_type, market_id)
