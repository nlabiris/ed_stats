from datetime import datetime
from typing import Any, List
from helper import Helper


class Signal:
    type: str
    type_localised: str
    count: int

    def __init__(self, type: str, type_localised: str, count: int) -> None:
        self.type = type
        self.type_localised = type_localised
        self.count = count

    @staticmethod
    def fromDict(obj: Any) -> 'Signal':
        assert isinstance(obj, dict)
        type = Helper.fromString(obj.get("Type"))
        type_localised = Helper.fromString(obj.get("Type_Localised"))
        count = Helper.fromInteger(obj.get("Count"))
        return Signal(type, type_localised, count)

class SAASignalsFound:
    timestamp: datetime
    event: str
    body_name: str
    system_address: int
    body_id: int
    signals: List[Signal]

    def __init__(self, timestamp: datetime, event: str, body_name: str, system_address: int, body_id: int, signals: List[Signal]) -> None:
        self.timestamp = timestamp
        self.event = event
        self.body_name = body_name
        self.system_address = system_address
        self.body_id = body_id
        self.signals = signals

    @staticmethod
    def fromDict(obj: Any) -> 'SAASignalsFound':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        body_name = Helper.fromString(obj.get("BodyName", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        body_id = Helper.fromInteger(obj.get("BodyID", 0))
        signals = Helper.fromList(Signal.fromDict, obj.get("Signals", []))
        return SAASignalsFound(timestamp, event, body_name, system_address, body_id, signals)
