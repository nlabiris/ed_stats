from datetime import datetime
from typing import Any
from helper import Helper


class LoadGame:
    timestamp: datetime
    event: str
    fid: str
    commander: str
    horizons: bool
    odyssey: bool
    ship: str
    ship_localised: str
    ship_id: int
    ship_name: str
    ship_ident: str
    fuel_level: float
    fuel_capacity: float
    start_landed: bool
    start_dead: bool
    group: str
    game_mode: str
    credits: int
    loan: int

    def __init__(self, timestamp: datetime, event: str, fid: str, commander: str, horizons: bool, odyssey: bool, ship: str, ship_localised: str, ship_id: int, ship_name: str, ship_ident: str, fuel_level: float, fuel_capacity: float, start_landed: bool, start_dead: bool, group: str, game_mode: str, credits: int, loan: int, language: str, gameversion: str, build: str) -> None:
        self.timestamp = timestamp
        self.event = event
        self.fid = fid
        self.commander = commander
        self.horizons = horizons
        self.odyssey = odyssey
        self.ship = ship
        self.ship_localised = ship_localised
        self.ship_id = ship_id
        self.ship_name = ship_name
        self.ship_ident = ship_ident
        self.fuel_level = fuel_level
        self.fuel_capacity = fuel_capacity
        self.start_landed = start_landed
        self.start_dead = start_dead
        self.game_mode = game_mode
        self.group = group
        self.credits = credits
        self.loan = loan
        self.language = language
        self.gameversion = gameversion
        self.build = build

    @staticmethod
    def fromDict(obj: Any) -> 'LoadGame':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        fid = Helper.fromString(obj.get("FID", ""))
        commander = Helper.fromString(obj.get("Commander", ""))
        horizons = Helper.fromBool(obj.get("Horizons", False))
        odyssey = Helper.fromBool(obj.get("Odyssey", False))
        ship = Helper.fromString(obj.get("Ship", ""))
        ship_localised = Helper.fromString(obj.get("Ship_Localised", ""))
        ship_id = Helper.fromInteger(obj.get("ShipID", 0))
        ship_name = Helper.fromString(obj.get("ShipName", ""))
        ship_ident = Helper.fromString(obj.get("ShipIdent", ""))
        fuel_level = Helper.fromFloat(obj.get("FuelLevel"))
        fuel_capacity = Helper.fromFloat(obj.get("FuelCapacity"))
        start_landed = Helper.fromBool(obj.get("StartLanded", False))
        start_dead = Helper.fromBool(obj.get("StartDead", False))
        game_mode = Helper.fromString(obj.get("GameMode", ""))
        group = Helper.fromString(obj.get("Group", ""))
        credits = Helper.fromInteger(obj.get("Credits", 0))
        loan = Helper.fromInteger(obj.get("Loan", 0))
        language = Helper.fromString(obj.get("language", ""))
        gameversion = Helper.fromString(obj.get("gameversion", ""))
        build = Helper.fromString(obj.get("build", ""))
        return LoadGame(timestamp, event, fid, commander, horizons, odyssey, ship, ship_localised, ship_id, ship_name, ship_ident, fuel_level, fuel_capacity, start_landed, start_dead, game_mode, group, credits, loan, language, gameversion, build)
