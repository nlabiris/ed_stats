from datetime import datetime
from typing import Any, List
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

class StationEconomy:
    name: str
    name_localised: str
    proportion: float

    def __init__(self, name: str, name_localised: str, proportion: float) -> None:
        self.name = name
        self.name_localised = name_localised
        self.proportion = proportion

    @staticmethod
    def fromDict(obj: Any) -> 'StationEconomy':
        assert isinstance(obj, dict)
        name = Helper.fromString(obj.get("Name",""))
        name_localised = Helper.fromString(obj.get("Name_Localised",""))
        proportion = Helper.fromFloat(obj.get("Proportion", 0))
        return StationEconomy(name, name_localised, proportion)


class StationFactionClass:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def fromDict(obj: Any) -> 'StationFactionClass':
        assert isinstance(obj, dict)
        name = Helper.fromString(obj.get("Name", ""))
        return StationFactionClass(name)

class Location:
    timestamp: datetime
    event: str
    docked: bool
    station_name: str
    station_type: str
    market_id: int
    station_faction: StationFactionClass
    station_government: str
    station_government_localised: str
    station_allegiance: str
    station_services: List[str]
    station_economy: str
    station_economy_localised: str
    station_economies: List[StationEconomy]
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
    factions: List[Faction]
    system_faction: StationFactionClass

    def __init__(self, timestamp: datetime, event: str, docked: bool, station_name: str, station_type: str, market_id: int, station_faction: StationFactionClass, station_government: str, station_government_localised: str, station_allegiance: str, station_services: List[str], station_economy: str, station_economy_localised: str, station_economies: List[StationEconomy], star_system: str, system_address: int, star_pos: List[float], system_allegiance: str, system_economy: str, system_economy_localised: str, system_second_economy: str, system_second_economy_localised: str, system_government: str, system_government_localised: str, system_security: str, system_security_localised: str, population: int, body: str, body_id: int, body_type: str, factions: List[Faction], system_faction: StationFactionClass) -> None:
        self.timestamp = timestamp
        self.event = event
        self.docked = docked
        self.station_name = station_name
        self.station_type = station_type
        self.market_id = market_id
        self.station_faction = station_faction
        self.station_government = station_government
        self.station_government_localised = station_government_localised
        self.station_allegiance = station_allegiance
        self.station_services = station_services
        self.station_economy = station_economy
        self.station_economy_localised = station_economy_localised
        self.station_economies = station_economies
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
        self.factions = factions
        self.system_faction = system_faction

    @staticmethod
    def fromDict(obj: Any) -> 'Location':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        docked = Helper.fromBool(obj.get("Docked", False))
        station_name = Helper.fromString(obj.get("StationName", ""))
        station_type = Helper.fromString(obj.get("StationType", ""))
        market_id = Helper.fromInteger(obj.get("MarketID", 0))
        station_faction = StationFactionClass.fromDict(obj.get("StationFaction", {}))
        station_government = Helper.fromString(obj.get("StationGovernment", ""))
        station_government_localised = Helper.fromString(obj.get("StationGovernment_Localised", ""))
        station_allegiance = Helper.fromString(obj.get("StationAllegiance", ""))
        station_services = Helper.fromList(Helper.fromString, obj.get("StationServices", []))
        station_economy = Helper.fromString(obj.get("StationEconomy", ""))
        station_economy_localised = Helper.fromString(obj.get("StationEconomy_Localised", ""))
        station_economies = Helper.fromList(StationEconomy.fromDict, obj.get("StationEconomies", []))
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
        factions = Helper.fromList(Faction.fromDict, obj.get("Factions", []))
        system_faction = StationFactionClass.fromDict(obj.get("SystemFaction", {}))
        return Location(timestamp, event, docked, station_name, station_type, market_id, station_faction, station_government, station_government_localised, station_allegiance, station_services, station_economy, station_economy_localised, station_economies, star_system, system_address, star_pos, system_allegiance, system_economy, system_economy_localised, system_second_economy, system_second_economy_localised, system_government, system_government_localised, system_security, system_security_localised, population, body, body_id, body_type, factions, system_faction)
