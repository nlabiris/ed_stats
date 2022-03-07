from datetime import datetime
from typing import Any
from helper import Helper


class FSSSignalDiscovered:
    timestamp: datetime
    event: str
    system_address: int
    signal_name: str
    signal_name_localised: str
    uss_type: str
    uss_type_localised: str
    spawning_state: str
    spawning_state_localised: str
    spawning_faction: str
    threat_level: int
    time_remaining: float
    is_station: bool

    def __init__(self, timestamp: datetime, event: str, system_address: int, signal_name: str, signal_name_localised: str, uss_type: str, uss_type_localised: str, spawning_state: str, spawning_state_localised: str, spawning_faction: str, threat_level: int, time_remaining: float, is_station: bool) -> None:
        self.timestamp = timestamp
        self.event = event
        self.system_address = system_address
        self.signal_name = signal_name
        self.signal_name_localised = signal_name_localised
        self.uss_type = uss_type
        self.uss_type_localised = uss_type_localised
        self.spawning_state = spawning_state
        self.spawning_state_localised = spawning_state_localised
        self.spawning_faction = spawning_faction
        self.threat_level = threat_level
        self.time_remaining = time_remaining
        self.is_station = is_station

    @staticmethod
    def fromDict(obj: Any) -> 'FSSSignalDiscovered':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        signal_name = Helper.fromString(obj.get("SignalName", ""))
        signal_name_localised = Helper.fromString(obj.get("SignalName_Localised", ""))
        uss_type = Helper.fromString(obj.get("USSType", ""))
        uss_type_localised = Helper.fromString(obj.get("USSType_Localised", ""))
        spawning_state = Helper.fromString(obj.get("SpawningState", ""))
        spawning_state_localised = Helper.fromString(obj.get("SpawningState_Localised", ""))
        spawning_faction = Helper.fromString(obj.get("SpawningFaction", ""))
        threat_level = Helper.fromInteger(obj.get("ThreatLevel", 0))
        time_remaining = Helper.fromFloat(obj.get("TimeRemaining", 0))
        is_station = Helper.fromBool(obj.get("IsStation", False))
        return FSSSignalDiscovered(timestamp, event, system_address, signal_name, signal_name_localised, uss_type, uss_type_localised, spawning_state, spawning_state_localised, spawning_faction, threat_level, time_remaining, is_station)
