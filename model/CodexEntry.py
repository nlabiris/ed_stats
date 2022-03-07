from datetime import datetime
from typing import Any
from helper import Helper


class CodexEntry:
    timestamp: datetime
    event: str
    entry_id: int
    name: str
    name_localised: str
    sub_category: str
    sub_category_localised: str
    category: str
    category_localised: str
    region: str
    region_localised: str
    system: str
    system_address: int
    is_new_entry: bool

    def __init__(self, timestamp: datetime, event: str, entry_id: int, name: str, name_localised: str, sub_category: str, sub_category_localised: str, category: str, category_localised: str, region: str, region_localised: str, system: str, system_address: int, is_new_entry: bool) -> None:
        self.timestamp = timestamp
        self.event = event
        self.entry_id = entry_id
        self.name = name
        self.name_localised = name_localised
        self.sub_category = sub_category
        self.sub_category_localised = sub_category_localised
        self.category = category
        self.category_localised = category_localised
        self.region = region
        self.region_localised = region_localised
        self.system = system
        self.system_address = system_address
        self.is_new_entry = is_new_entry

    @staticmethod
    def fromDict(obj: Any) -> 'CodexEntry':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        entry_id = Helper.fromInteger(obj.get("EntryID", 0))
        name = Helper.fromString(obj.get("Name", ""))
        name_localised = Helper.fromString(obj.get("Name_Localised", ""))
        sub_category = Helper.fromString(obj.get("SubCategory", ""))
        sub_category_localised = Helper.fromString(obj.get("SubCategory_Localised", ""))
        category = Helper.fromString(obj.get("Category", ""))
        category_localised = Helper.fromString(obj.get("Category_Localised", ""))
        region = Helper.fromString(obj.get("Region", ""))
        region_localised = Helper.fromString(obj.get("Region_Localised", ""))
        system = Helper.fromString(obj.get("System", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        is_new_entry = Helper.fromBool(obj.get("IsNewEntry", False))
        return CodexEntry(timestamp, event, entry_id, name, name_localised, sub_category, sub_category_localised, category, category_localised, region, region_localised, system, system_address, is_new_entry)
