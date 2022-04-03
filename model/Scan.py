from datetime import datetime
from typing import Any, Optional, List
from helper import Helper


class Material:
    name: str
    percent: float

    def __init__(self, name: str, percent: float) -> None:
        self.name = name
        self.percent = percent

    @staticmethod
    def fromDict(obj: Any) -> 'Material':
        assert isinstance(obj, dict)
        name = Helper.fromString(obj.get("Name", ""))
        percent = Helper.fromFloat(obj.get("Percent", 0))
        return Material(name, percent)

class AtmosphereComposition:
    name: str
    percent: float

    def __init__(self, name: str, percent: float) -> None:
        self.name = name
        self.percent = percent

    @staticmethod
    def fromDict(obj: Any) -> 'AtmosphereComposition':
        assert isinstance(obj, dict)
        name = Helper.fromString(obj.get("Name", ""))
        percent = Helper.fromFloat(obj.get("Percent", 0))
        return AtmosphereComposition(name, percent)

class Composition:
    ice: float
    rock: float
    metal: float

    def __init__(self, ice: float, rock: float, metal: float) -> None:
        self.ice = ice
        self.rock = rock
        self.metal = metal

    @staticmethod
    def fromDict(obj: Any) -> 'Composition':
        assert isinstance(obj, dict)
        ice = Helper.fromFloat(obj.get("Ice", 0))
        rock = Helper.fromFloat(obj.get("Rock", 0))
        metal = Helper.fromFloat(obj.get("Metal", 0))
        return Composition(ice, rock, metal)

class Parent:
    planet: Optional[int]
    star: Optional[int]

    def __init__(self, planet: Optional[int], star: Optional[int]) -> None:
        self.planet = planet
        self.star = star

    @staticmethod
    def fromDict(obj: Any) -> 'Parent':
        assert isinstance(obj, dict)
        planet = Helper.fromUnion([Helper.fromInteger, Helper.fromNone], obj.get("Planet", 0))
        star = Helper.fromUnion([Helper.fromInteger, Helper.fromNone], obj.get("Star", 0))
        return Parent(planet, star)

class Ring:
    name: str
    ring_class: str
    mass_mt: float
    inner_rad: float
    outer_rad: float

    def __init__(self, name: str, ring_class: str, mass_mt: float, inner_rad: float, outer_rad: float) -> None:
        self.name = name
        self.ring_class = ring_class
        self.mass_mt = mass_mt
        self.inner_rad = inner_rad
        self.outer_rad = outer_rad

    @staticmethod
    def fromDict(obj: Any) -> 'Ring':
        assert isinstance(obj, dict)
        name = Helper.fromString(obj.get("Name", ""))
        ring_class = Helper.fromString(obj.get("RingClass", ""))
        mass_mt = Helper.fromFloat(obj.get("MassMT", 0))
        inner_rad = Helper.fromFloat(obj.get("InnerRad", 0))
        outer_rad = Helper.fromFloat(obj.get("OuterRad", 0))
        return Ring(name, ring_class, mass_mt, inner_rad, outer_rad)

class Scan:
    timestamp: datetime
    event: str
    scan_type: str
    body_name: str
    body_id: int
    parents: List[Parent]
    star_system: str
    system_address: int
    distance_from_arrival_ls: float
    star_type: str
    subclass: int
    stellar_mass: float
    tidal_lock: bool
    terraform_state: str
    planet_class: str
    atmosphere: str
    atmosphere_type: str
    volcanism: str
    mass_em: float
    radius: float
    absolute_magnitude: float
    surface_gravity: float
    surface_temperature: float
    surface_pressure: float
    luminosity: str
    age_my: int
    landable: bool
    materials: List[Material]
    composition: Composition
    atmosphere_composition: List[AtmosphereComposition]
    semi_major_axis: float
    eccentricity: float
    orbital_inclination: float
    periapsis: float
    orbital_period: float
    rotation_period: float
    axial_tilt: float
    rings: List[Ring]
    reserve_level: str
    was_discovered: bool
    was_mapped: bool

    def __init__(self, timestamp: datetime, event: str, scan_type: str, body_name: str, body_id: int, parents: List[Parent], star_system: str, system_address: int, distance_from_arrival_ls: float, star_type: str, subclass: int, stellar_mass: float, tidal_lock: bool, terraform_state: str, planet_class: str, atmosphere: str, atmosphere_type: str, volcanism: str, mass_em: float, radius: float, absolute_magnitude: float, surface_gravity: float, surface_temperature: float, surface_pressure: float, luminosity: str, age_my: int, landable: bool, materials: List[Material], composition: Composition, atmosphere_composition: List[AtmosphereComposition], semi_major_axis: float, eccentricity: float, orbital_inclination: float, periapsis: float, orbital_period: float, rotation_period: float, axial_tilt: float, rings: List[Ring], reserve_level: str, was_discovered: bool, was_mapped: bool) -> None:
        self.timestamp = timestamp
        self.event = event
        self.scan_type = scan_type
        self.body_name = body_name
        self.body_id = body_id
        self.parents = parents
        self.star_system = star_system
        self.system_address = system_address
        self.distance_from_arrival_ls = distance_from_arrival_ls
        self.star_type = star_type
        self.subclass = subclass
        self.stellar_mass = stellar_mass
        self.tidal_lock = tidal_lock
        self.terraform_state = terraform_state
        self.planet_class = planet_class
        self.atmosphere = atmosphere
        self.atmosphere_type = atmosphere_type
        self.volcanism = volcanism
        self.mass_em = mass_em
        self.radius = radius
        self.absolute_magnitude = absolute_magnitude
        self.surface_gravity = surface_gravity
        self.surface_temperature = surface_temperature
        self.surface_pressure = surface_pressure
        self.luminosity = luminosity
        self.age_my = age_my
        self.landable = landable
        self.materials = materials
        self.composition = composition
        self.atmosphere_composition = atmosphere_composition
        self.semi_major_axis = semi_major_axis
        self.eccentricity = eccentricity
        self.orbital_inclination = orbital_inclination
        self.periapsis = periapsis
        self.orbital_period = orbital_period
        self.rotation_period = rotation_period
        self.axial_tilt = axial_tilt
        self.rings = rings
        self.reserve_level = reserve_level
        self.was_discovered = was_discovered
        self.was_mapped = was_mapped

    @staticmethod
    def fromDict(obj: Any) -> 'Scan':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        scan_type = Helper.fromString(obj.get("ScanType", ""))
        body_name = Helper.fromString(obj.get("BodyName", ""))
        body_id = Helper.fromInteger(obj.get("BodyID", 0))
        parents = Helper.fromList(Parent.fromDict, obj.get("Parents", []))
        star_system = Helper.fromString(obj.get("StarSystem", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        distance_from_arrival_ls = Helper.fromFloat(obj.get("DistanceFromArrivalLS", 0))
        star_type = Helper.fromString(obj.get("StarType", ""))
        subclass = Helper.fromInteger(obj.get("Subclass", 0))
        stellar_mass = Helper.fromFloat(obj.get("StellarMass", 0))
        tidal_lock = Helper.fromBool(obj.get("TidalLock", False))
        terraform_state = Helper.fromString(obj.get("TerraformState", ""))
        planet_class = Helper.fromString(obj.get("PlanetClass", ""))
        atmosphere = Helper.fromString(obj.get("Atmosphere", ""))
        atmosphere_type = Helper.fromString(obj.get("AtmosphereType", ""))
        volcanism = Helper.fromString(obj.get("Volcanism", ""))
        mass_em = Helper.fromFloat(obj.get("MassEM", 0))
        radius = Helper.fromFloat(obj.get("Radius", 0))
        absolute_magnitude = Helper.fromFloat(obj.get("AbsoluteMagnitude", 0))
        surface_gravity = Helper.fromFloat(obj.get("SurfaceGravity", 0))
        surface_temperature = Helper.fromFloat(obj.get("SurfaceTemperature", 0))
        surface_pressure = Helper.fromFloat(obj.get("SurfacePressure", 0))
        luminosity = Helper.fromString(obj.get("Luminosity", ""))
        age_my = Helper.fromInteger(obj.get("Age_MY", 0))
        landable = Helper.fromBool(obj.get("Landable", False))
        materials = Helper.fromList(Material.fromDict, obj.get("Materials", []))
        composition = Composition.fromDict(obj.get("Composition", {}))
        atmosphere_composition = Helper.fromList(AtmosphereComposition.fromDict, obj.get("AtmosphereComposition", []))
        semi_major_axis = Helper.fromFloat(obj.get("SemiMajorAxis", 0))
        eccentricity = Helper.fromFloat(obj.get("Eccentricity", 0))
        orbital_inclination = Helper.fromFloat(obj.get("OrbitalInclination", 0))
        periapsis = Helper.fromFloat(obj.get("Periapsis", 0))
        orbital_period = Helper.fromFloat(obj.get("OrbitalPeriod", 0))
        rotation_period = Helper.fromFloat(obj.get("RotationPeriod", 0))
        axial_tilt = Helper.fromFloat(obj.get("AxialTilt", 0))
        rings = Helper.fromList(Ring.fromDict, obj.get("Rings", []))
        reserve_level = Helper.fromString(obj.get("ReserveLevel", ""))
        was_discovered = Helper.fromBool(obj.get("WasDiscovered", False))
        was_mapped = Helper.fromBool(obj.get("WasMapped", False))
        return Scan(timestamp, event, scan_type, body_name, body_id, parents, star_system, system_address, distance_from_arrival_ls, star_type, subclass, stellar_mass, tidal_lock, terraform_state, planet_class, atmosphere, atmosphere_type, volcanism, mass_em, radius, absolute_magnitude, surface_gravity, surface_temperature, surface_pressure, luminosity, age_my, landable, materials, composition, atmosphere_composition, semi_major_axis, eccentricity, orbital_inclination, periapsis, orbital_period, rotation_period, axial_tilt, rings, reserve_level, was_discovered, was_mapped)
