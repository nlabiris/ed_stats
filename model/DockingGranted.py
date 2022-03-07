from datetime import datetime
from typing import Any
from helper import Helper


class DockingGranted:
    timestamp: datetime
    event: str
    landing_pad: int
    market_id: int
    station_name: str
    station_type: str

    def __init__(self, timestamp: datetime, event: str, landing_pad: int, market_id: int, station_name: str, station_type: str) -> None:
        self.timestamp = timestamp
        self.event = event
        self.landing_pad = landing_pad
        self.market_id = market_id
        self.station_name = station_name
        self.station_type = station_type

    @staticmethod
    def fromDict(obj: Any) -> 'DockingGranted':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        landing_pad = Helper.fromInteger(obj.get("LandingPad", 0))
        market_id = Helper.fromInteger(obj.get("MarketID", 0))
        station_name = Helper.fromString(obj.get("StationName", ""))
        station_type = Helper.fromString(obj.get("StationType", ""))
        return DockingGranted(timestamp, event, landing_pad, market_id, station_name, station_type)
