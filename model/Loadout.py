from datetime import datetime
from typing import Any, List
from helper import Helper


class FuelCapacity:
    main: float
    reserve: float

    def __init__(self, main: float, reserve: float) -> None:
        self.main = main
        self.reserve = reserve

    @staticmethod
    def fromDict(obj: Any) -> 'FuelCapacity':
        assert isinstance(obj, dict)
        main = Helper.fromFloat(obj.get("Main", 0))
        reserve = Helper.fromFloat(obj.get("Reserve", 0))
        return FuelCapacity(main, reserve)


class Module:
    slot: str
    item: str
    on: bool
    priority: int
    health: float

    def __init__(self, slot: str, item: str, on: bool, priority: int, health: float) -> None:
        self.slot = slot
        self.item = item
        self.on = on
        self.priority = priority
        self.health = health

    @staticmethod
    def fromDict(obj: Any) -> 'Module':
        assert isinstance(obj, dict)
        slot = Helper.fromString(obj.get("Slot", ""))
        item = Helper.fromString(obj.get("Item", ""))
        on = Helper.fromBool(obj.get("On", False))
        priority = Helper.fromInteger(obj.get("Priority", 0))
        health = Helper.fromFloat(obj.get("Health", 0))
        return Module(slot, item, on, priority, health)


class Loadout:
    timestamp: datetime
    event: str
    ship: str
    ship_id: int
    ship_name: str
    ship_ident: str
    hull_value: int
    modules_value: int
    hull_health: float
    unladen_mass: float
    cargo_capacity: int
    max_jump_range: float
    fuel_capacity: FuelCapacity
    rebuy: int
    hot: bool
    modules: List[Module]

    def __init__(self, timestamp: datetime, event: str, ship: str, ship_id: int, ship_name: str, ship_ident: str, hull_value: int, modules_value: int, hull_health: float, unladen_mass: float, cargo_capacity: int, max_jump_range: float, fuel_capacity: FuelCapacity, rebuy: int, hot: bool, modules: List[Module]) -> None:
        self.timestamp = timestamp
        self.event = event
        self.ship = ship
        self.ship_id = ship_id
        self.ship_name = ship_name
        self.ship_ident = ship_ident
        self.hull_value = hull_value
        self.modules_value = modules_value
        self.hull_health = hull_health
        self.unladen_mass = unladen_mass
        self.cargo_capacity = cargo_capacity
        self.max_jump_range = max_jump_range
        self.fuel_capacity = fuel_capacity
        self.rebuy = rebuy
        self.hot = hot
        self.modules = modules

    @staticmethod
    def fromDict(obj: Any) -> 'Loadout':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        ship = Helper.fromString(obj.get("Ship", ""))
        ship_id = Helper.fromInteger(obj.get("ShipID", 0))
        ship_name = Helper.fromString(obj.get("ShipName", ""))
        ship_ident = Helper.fromString(obj.get("ShipIdent", ""))
        hull_value = Helper.fromInteger(obj.get("HullValue", 0))
        modules_value = Helper.fromInteger(obj.get("ModulesValue", 0))
        hull_health = Helper.fromFloat(obj.get("HullHealth", 0))
        unladen_mass = Helper.fromFloat(obj.get("UnladenMass", 0))
        cargo_capacity = Helper.fromInteger(obj.get("CargoCapacity", 0))
        max_jump_range = Helper.fromFloat(obj.get("MaxJumpRange", 0))
        fuel_capacity = FuelCapacity.fromDict(obj.get("FuelCapacity", {}))
        rebuy = Helper.fromInteger(obj.get("Rebuy", 0))
        hot = Helper.fromBool(obj.get("Hot", False))
        modules = Helper.fromList(Module.fromDict, obj.get("Modules", []))
        return Loadout(timestamp, event, ship, ship_id, ship_name, ship_ident, hull_value, modules_value, hull_health, unladen_mass, cargo_capacity, max_jump_range, fuel_capacity, rebuy, hot, modules)
