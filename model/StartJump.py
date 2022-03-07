from datetime import datetime
from typing import Any
from helper import Helper


class StartJump:
    timestamp: datetime
    event: str
    jump_type: str
    star_system: str
    system_address: int
    star_class: str

    def __init__(self, timestamp: datetime, event: str, jump_type: str, star_system: str, system_address: int, star_class: str) -> None:
        self.timestamp = timestamp
        self.event = event
        self.jump_type = jump_type
        self.star_system = star_system
        self.system_address = system_address
        self.star_class = star_class

    @staticmethod
    def fromDict(obj: Any) -> 'StartJump':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        jump_type = Helper.fromString(obj.get("JumpType", ""))
        star_system = Helper.fromString(obj.get("StarSystem", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        star_class = Helper.fromString(obj.get("StarClass", ""))
        return StartJump(timestamp, event, jump_type, star_system, system_address, star_class)
