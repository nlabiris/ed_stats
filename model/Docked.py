from typing import Any, List
from datetime import datetime
from helper import Helper


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
        name = Helper.fromString(obj.get("Name", ""))
        name_localised = Helper.fromString(obj.get("Name_Localised", ""))
        proportion = Helper.fromFloat(obj.get("Proportion", 0))
        return StationEconomy(name, name_localised, proportion)

class StationFaction:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def fromDict(obj: Any) -> 'StationFaction':
        assert isinstance(obj, dict)
        name = Helper.fromString(obj.get("Name", ""))
        return StationFaction(name)

class Docked:
    timestamp: datetime
    event: str
    station_name: str
    station_type: str
    star_system: str
    system_address: int
    market_id: int
    station_faction: StationFaction
    station_government: str
    station_government_localised: str
    station_allegiance: str
    station_services: List[str]
    station_economy: str
    station_economy_localised: str
    station_economies: List[StationEconomy]
    dist_from_star_ls: float

    def __init__(self, timestamp: datetime, event: str, station_name: str, station_type: str, star_system: str, system_address: int, market_id: int, station_faction: StationFaction, station_government: str, station_government_localised: str, station_allegiance: str, station_services: List[str], station_economy: str, station_economy_localised: str, station_economies: List[StationEconomy], dist_from_star_ls: float) -> None:
        self.timestamp = timestamp
        self.event = event
        self.station_name = station_name
        self.station_type = station_type
        self.star_system = star_system
        self.system_address = system_address
        self.market_id = market_id
        self.station_faction = station_faction
        self.station_government = station_government
        self.station_government_localised = station_government_localised
        self.station_allegiance = station_allegiance
        self.station_services = station_services
        self.station_economy = station_economy
        self.station_economy_localised = station_economy_localised
        self.station_economies = station_economies
        self.dist_from_star_ls = dist_from_star_ls

    @staticmethod
    def fromDict(obj: Any) -> 'Docked':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        station_name = Helper.fromString(obj.get("StationName", ""))
        station_type = Helper.fromString(obj.get("StationType", ""))
        star_system = Helper.fromString(obj.get("StarSystem", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        market_id = Helper.fromInteger(obj.get("MarketID", 0))
        station_faction = StationFaction.fromDict(obj.get("StationFaction", {}))
        station_government = Helper.fromString(obj.get("StationGovernment", ""))
        station_government_localised = Helper.fromString(obj.get("StationGovernment_Localised", ""))
        station_allegiance = Helper.fromString(obj.get("StationAllegiance", ""))
        station_services = Helper.fromList(Helper.fromString, obj.get("StationServices", []))
        station_economy = Helper.fromString(obj.get("StationEconomy", ""))
        station_economy_localised = Helper.fromString(obj.get("StationEconomy_Localised", ""))
        station_economies = Helper.fromList(StationEconomy.fromDict, obj.get("StationEconomies", []))
        dist_from_star_ls = Helper.fromFloat(obj.get("DistFromStarLS", 0))
        return Docked(timestamp, event, station_name, station_type, star_system, system_address, market_id, station_faction, station_government, station_government_localised, station_allegiance, station_services, station_economy, station_economy_localised, station_economies, dist_from_star_ls)
