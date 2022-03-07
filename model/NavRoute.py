from datetime import datetime
from typing import Any, List
from helper import Helper


class NavRoute:
    star_system: int
    star_pos: List[float]
    star_class: str
    system_address: int

    def __init__(self, star_system: int, star_pos: List[float], star_class: str, system_address: int) -> None:
        self.star_system = star_system
        self.star_pos = star_pos
        self.star_class = star_class
        self.system_address = system_address

    @staticmethod
    def fromDict(obj: Any) -> 'NavRoute':
        assert isinstance(obj, dict)
        star_system = Helper.fromInteger(obj.get("StarSystem", 0))
        star_pos = Helper.fromList(Helper.fromFloat, obj.get("StarPos", []))
        star_class = Helper.fromString(obj.get("StarClass", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        return NavRoute(star_system, star_pos, star_class, system_address)
