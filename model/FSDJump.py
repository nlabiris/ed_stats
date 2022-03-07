from typing import Any, List, TypeVar, Callable, Type, cast
from datetime import datetime
from helper import Helper


class Faction:
    name: str
    faction_state: str
    government: str
    influence: float
    allegiance: str
    happiness: str
    happiness_localised: str
    my_reputation: float

    def __init__(self, name: str, faction_state: str, government: str, influence: float, allegiance: str, happiness: str, happiness_localised: str, my_reputation: float) -> None:
        self.name = name
        self.faction_state = faction_state
        self.government = government
        self.influence = influence
        self.allegiance = allegiance
        self.happiness = happiness
        self.happiness_localised = happiness_localised
        self.my_reputation = my_reputation

    @staticmethod
    def fromDict(obj: Any) -> 'Faction':
        assert isinstance(obj, dict)
        name = Helper.fromString(obj.get("Name", ""))
        faction_state = Helper.fromString(obj.get("FactionState", ""))
        government = Helper.fromString(obj.get("Government", ""))
        influence = Helper.fromFloat(obj.get("Influence", 0))
        allegiance = Helper.fromString(obj.get("Allegiance", ""))
        happiness = Helper.fromString(obj.get("Happiness", ""))
        happiness_localised = Helper.fromString(obj.get("Happiness_Localised", ""))
        my_reputation = Helper.fromFloat(obj.get("MyReputation", 0))
        return Faction(name, faction_state, government, influence, allegiance, happiness, happiness_localised, my_reputation)


class SystemFaction:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def fromDict(obj: Any) -> 'SystemFaction':
        assert isinstance(obj, dict)
        name = Helper.fromString(obj.get("Name", ""))
        return SystemFaction(name)


class FSDJump:
    timestamp: datetime
    event: str
    star_system: str
    system_address: int
    star_pos: List[float]
    system_allegiance: str
    system_economy: str
    system_economy_localised: str
    system_second_economy: str
    system_second_economy_localised: str
    system_government: str
    system_government_localised: str
    system_security: str
    system_security_localised: str
    population: int
    body: str
    body_id: int
    body_type: str
    jump_dist: float
    fuel_used: float
    fuel_level: float
    factions: List[Faction]
    system_faction: SystemFaction

    def __init__(self, timestamp: datetime, event: str, star_system: str, system_address: int, star_pos: List[float], system_allegiance: str, system_economy: str, system_economy_localised: str, system_second_economy: str, system_second_economy_localised: str, system_government: str, system_government_localised: str, system_security: str, system_security_localised: str, population: int, body: str, body_id: int, body_type: str, jump_dist: float, fuel_used: float, fuel_level: float, factions: List[Faction], system_faction: SystemFaction) -> None:
        self.timestamp = timestamp
        self.event = event
        self.star_system = star_system
        self.system_address = system_address
        self.star_pos = star_pos
        self.system_allegiance = system_allegiance
        self.system_economy = system_economy
        self.system_economy_localised = system_economy_localised
        self.system_second_economy = system_second_economy
        self.system_second_economy_localised = system_second_economy_localised
        self.system_government = system_government
        self.system_government_localised = system_government_localised
        self.system_security = system_security
        self.system_security_localised = system_security_localised
        self.population = population
        self.body = body
        self.body_id = body_id
        self.body_type = body_type
        self.jump_dist = jump_dist
        self.fuel_used = fuel_used
        self.fuel_level = fuel_level
        self.factions = factions
        self.system_faction = system_faction

    @staticmethod
    def fromDict(obj: Any) -> 'FSDJump':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        star_system = Helper.fromString(obj.get("StarSystem", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        star_pos = Helper.fromList(Helper.fromFloat, obj.get("StarPos", []))
        system_allegiance = Helper.fromString(obj.get("SystemAllegiance", ""))
        system_economy = Helper.fromString(obj.get("SystemEconomy", ""))
        system_economy_localised = Helper.fromString(obj.get("SystemEconomy_Localised", ""))
        system_second_economy = Helper.fromString(obj.get("SystemSecondEconomy", ""))
        system_second_economy_localised = Helper.fromString(obj.get("SystemSecondEconomy_Localised", ""))
        system_government = Helper.fromString(obj.get("SystemGovernment", ""))
        system_government_localised = Helper.fromString(obj.get("SystemGovernment_Localised", ""))
        system_security = Helper.fromString(obj.get("SystemSecurity", ""))
        system_security_localised = Helper.fromString(obj.get("SystemSecurity_Localised", ""))
        population = Helper.fromInteger(obj.get("Population", 0))
        body = Helper.fromString(obj.get("Body", ""))
        body_id = Helper.fromInteger(obj.get("BodyID", 0))
        body_type = Helper.fromString(obj.get("BodyType", ""))
        jump_dist = Helper.fromFloat(obj.get("JumpDist", 0))
        fuel_used = Helper.fromFloat(obj.get("FuelUsed", 0))
        fuel_level = Helper.fromFloat(obj.get("FuelLevel", 0))
        factions = Helper.fromList(Faction.fromDict, obj.get("Factions", []))
        system_faction = SystemFaction.fromDict(obj.get("SystemFaction", {}))
        return FSDJump(timestamp, event, star_system, system_address, star_pos, system_allegiance, system_economy, system_economy_localised, system_second_economy, system_second_economy_localised, system_government, system_government_localised, system_security, system_security_localised, population, body, body_id, body_type, jump_dist, fuel_used, fuel_level, factions, system_faction)
