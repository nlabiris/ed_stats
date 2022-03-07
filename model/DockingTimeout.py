from datetime import datetime
from typing import Any
from helper import Helper


class DockingTimeout:
    timestamp: datetime
    event: str
    market_id: int
    station_name: str
    station_type: str

    def __init__(self, timestamp: datetime, event: str, market_id: int, station_name: str, station_type: str) -> None:
        self.timestamp = timestamp
        self.event = event
        self.market_id = market_id
        self.station_name = station_name
        self.station_type = station_type

    @staticmethod
    def fromDict(obj: Any) -> 'DockingTimeout':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        market_id = Helper.fromInteger(obj.get("MarketID", 0))
        station_name = Helper.fromString(obj.get("StationName", ""))
        station_type = Helper.fromString(obj.get("StationType", ""))
        return DockingTimeout(timestamp, event, market_id, station_name, station_type)
