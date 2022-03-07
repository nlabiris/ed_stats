from datetime import datetime
from typing import Any, List
from helper import Helper


class Mission:
    mission_id: int
    name: str
    passenger_mission: bool
    expires: int

    def __init__(self, mission_id: int, name: str, passenger_mission: bool, expires: int) -> None:
        self.mission_id = mission_id
        self.name = name
        self.passenger_mission = passenger_mission
        self.expires = expires

    @staticmethod
    def fromDict(obj: Any) -> 'Mission':
        assert isinstance(obj, dict)
        mission_id = Helper.fromInteger(obj.get("MissionID", 0))
        name = Helper.fromString(obj.get("Name", ""))
        passenger_mission = Helper.fromBool(obj.get("PassengerMission", False))
        expires = Helper.fromInteger(obj.get("Expires", 0))
        return Mission(mission_id, name, passenger_mission, expires)

class Missions:
    timestamp: datetime
    event: str
    active: List[Mission]
    failed: List[Mission]
    complete: List[Mission]

    def __init__(self, timestamp: datetime, event: str, active: List[Mission], failed: List[Mission], complete: List[Mission]) -> None:
        self.timestamp = timestamp
        self.event = event
        self.active = active
        self.failed = failed
        self.complete = complete

    @staticmethod
    def fromDict(obj: Any) -> 'Missions':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        active = Helper.fromList(Mission.fromDict, obj.get("Active", []))
        failed = Helper.fromList(Mission.fromDict, obj.get("Failed", []))
        complete = Helper.fromList(Mission.fromDict, obj.get("Complete", []))
        return Missions(timestamp, event, active, failed, complete)
