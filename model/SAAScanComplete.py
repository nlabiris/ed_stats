from datetime import datetime
from typing import Any
from helper import Helper


class SAAScanComplete:
    timestamp: datetime
    event: str
    body_name: str
    system_address: int
    body_id: int
    probes_used: int
    efficiency_target: int

    def __init__(self, timestamp: datetime, event: str, body_name: str, system_address: int, body_id: int, probes_used: int, efficiency_target: int) -> None:
        self.timestamp = timestamp
        self.event = event
        self.body_name = body_name
        self.system_address = system_address
        self.body_id = body_id
        self.probes_used = probes_used
        self.efficiency_target = efficiency_target

    @staticmethod
    def fromDict(obj: Any) -> 'SAAScanComplete':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        body_name = Helper.fromString(obj.get("BodyName", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        body_id = Helper.fromInteger(obj.get("BodyID", 0))
        probes_used = Helper.fromInteger(obj.get("ProbesUsed", 0))
        efficiency_target = Helper.fromInteger(obj.get("EfficiencyTarget", 0))
        return SAAScanComplete(timestamp, event, body_name, system_address, body_id, probes_used, efficiency_target)
