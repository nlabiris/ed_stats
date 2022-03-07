from datetime import datetime
from typing import Any
from helper import Helper


class Liftoff:
    timestamp: datetime
    event: str
    player_controlled: bool
    latitude: float
    longitude: float
    nearest_destination: str
    nearest_destination_localised: str
    star_system: str
    system_address: int
    body: str
    body_id: int
    on_station: bool
    on_planet: bool

    def __init__(self, timestamp: datetime, event: str, player_controlled: bool, latitude: float, longitude: float, nearest_destination: str, nearest_destination_localised: str, star_system: str, system_address: int, body: str, body_id: int, on_station: bool, on_planet: bool) -> None:
        self.timestamp = timestamp
        self.event = event
        self.player_controlled = player_controlled
        self.latitude = latitude
        self.longitude = longitude
        self.nearest_destination = nearest_destination
        self.nearest_destination_localised = nearest_destination_localised
        self.star_system = star_system
        self.system_address = system_address
        self.body = body
        self.body_id = body_id
        self.on_station = on_station
        self.on_planet = on_planet

    @staticmethod
    def fromDict(obj: Any) -> 'Liftoff':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        player_controlled = Helper.fromBool(obj.get("PlayerControlled", False))
        latitude = Helper.fromFloat(obj.get("Latitude", False))
        longitude = Helper.fromFloat(obj.get("Longitude", False))
        nearest_destination = Helper.fromString(obj.get("NearestDestination", ""))
        nearest_destination_localised = Helper.fromString(obj.get("NearestDestination_Localised", ""))
        star_system = Helper.fromString(obj.get("StarSystem", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        body = Helper.fromString(obj.get("Body", ""))
        body_id = Helper.fromInteger(obj.get("BodyID", 0))
        on_station = Helper.fromString(obj.get("OnStation", ""))
        on_planet = Helper.fromInteger(obj.get("OnPlanet", 0))
        return Liftoff(timestamp, event, player_controlled, latitude, longitude, nearest_destination, nearest_destination_localised, star_system, system_address, body, body_id, on_station, on_planet)
