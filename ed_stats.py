import matplotlib.pyplot as plt
import numpy as np
import json
import os
import argparse
from typing import List
from ast import For
from datetime import datetime,timedelta
from pkgutil import extend_path
from matplotlib.transforms import Bbox
from matplotlib.cbook import get_sample_data
from matplotlib._png import read_png
from mpl_toolkits import mplot3d
from helper import Helper
from timing import Timing
from model.ApproachBody import ApproachBody
from model.BuyExplorationData import BuyExplorationData
from model.Cargo import Cargo
from model.CodexEntry import CodexEntry
from model.Commander import Commander
from model.DiscoveryScan import DiscoveryScan
from model.Docked import Docked
from model.DockingCancelled import DockingCancelled
from model.DockingDenied import DockingDenied
from model.DockingGranted import DockingGranted
from model.DockingRequested import DockingRequested
from model.DockingTimeout import DockingTimeout
from model.Fileheader import Fileheader
from model.FSDJump import FSDJump
from model.FSDJumpConflicts import FSDJumpConflicts
from model.FSDJumpConflictsFaction import FSDJumpConflictsFaction
from model.FSDJumpFactions import FSDJumpFactions
from model.FSDJumpSystemFaction import FSDJumpSystemFaction
from model.FSDTarget import FSDTarget
from model.FSSAllBodiesFound import FSSAllBodiesFound
from model.FSSDiscoveryScan import FSSDiscoveryScan
from model.FSSSignalDiscovered import FSSSignalDiscovered
from model.LeaveBody import LeaveBody
from model.Liftoff import Liftoff
from model.LoadGame import LoadGame
from model.Loadout import Loadout
from model.Location import Location
from model.MaterialCollected import MaterialCollected
from model.MaterialDiscarded import MaterialDiscarded
from model.MaterialDiscovered import MaterialDiscovered
from model.Materials import Materials
from model.Missions import Missions
from model.MultiSellExplorationData import MultiSellExplorationData
from model.NavBeaconScan import NavBeaconScan
from model.NavRoute import NavRoute
from model.NewCommander import NewCommander
from model.Passengers import Passengers
from model.Powerplay import Powerplay
from model.Progress import Progress
from model.Rank import Rank
from model.Reputation import Reputation
from model.SAAScanComplete import SAAScanComplete
from model.SAASignalsFound import SAASignalsFound
from model.Scan import Scan
from model.SellExplorationData import SellExplorationData
from model.StartJump import StartJump
from model.Statistics import Statistics
from model.SupercruiseEntry import SupercruiseEntry
from model.SupercruiseExit import SupercruiseExit
from model.Touchdown import Touchdown
from model.Undocked import Undocked
from model.Music import Music


class ED:
    def __init__(self):
        '''
        Constructor
        '''

        with open("config.json", "r") as config_file:
            config = json.load(config_file)
        self.journals_path = config.get("journals_path")
        self.green_system_materials = {
            "basic": [
                "carbon",
                "vanadium",
                "germanium",
            ],
            "standard": [
                "carbon",
                "vanadium",
                "germanium",
                "cadmium",
                "niobium",
            ],
            "premium": [
                "carbon",
                "germanium",
                "niobium",
                "arsenic",
                "yttrium",
                "polonium",
            ]
        }

        self.timing = Timing()

    def parseArgs(self):
        '''
        Parse command line arguments
        '''

        # Initiate the parser
        parser = argparse.ArgumentParser()

        # Add possible arguments
        parser.add_argument("--all-events", help="Handle all journal event types", action="store_true")
        parser.add_argument("--all-journals", help="Parse all journal files", action="store_true")
        parser.add_argument("--events", help="Journal event types, separated by comma (,)")
        parser.add_argument("--journal-from", help="Journal timestamp from")
        parser.add_argument("--journal-to", help="Journal timestamp to. If ommited, assume current datetime")
        parser.add_argument("--scan-type", help="For event type 'Scan' - Scan type can be Basic, Detailed, NavBeacon, NavBeaconDetail, AutoScan")
        parser.add_argument("--materials", help="For event type 'Scan' - Materials, separated by comma (,)")
        parser.add_argument("--landable", help="For event type 'Scan' - If the body is landable or not", action="store_true")
        parser.add_argument("--was-mapped", help="For event type 'Scan' - If the body was mapped", action="store_true")
        parser.add_argument("--was-discovered", help="For event type 'Scan' - If the body was discovered", action="store_true")
        parser.add_argument("--green-systems", help="For event type 'Scan' - Filter 'green' systems (systems where you can find materials for FSD injections)", action="store_true")
        parser.add_argument("--total-earnings", help="For event types 'SellExplorationData', 'MultiSellExplorationData' - Get total earnings", action="store_true")

        # Read arguments from the command line
        self.args = parser.parse_args()

        if (self.args.all_events):
            self.args.events = []
        else:
            if (self.args.events):
                self.args.events = [event.strip() for event in self.args.events.split(",")]
            else:
                raise Exception("Provide at least one journal event type by using the '--events' option or use '--all-events' option")

        if (not self.args.all_journals):
            if (self.args.journal_from):
                self.args.journal_from = datetime.strptime(self.args.journal_from, "%Y-%m-%d")
            else:
                raise Exception("Provide a 'from' timestamp to start filtering for journals using the '--journal-from' option  (format: YYYY-mm-dd)")

            if (self.args.journal_to):
                self.args.journal_to = datetime.strptime(self.args.journal_to, "%Y-%m-%d")

        return self.args

    def createObjectByEvent(self, line):
        e = line.get("event")
        switch = {
            "ApproachBody": ApproachBody,
            "BuyExplorationData": BuyExplorationData,
            "Cargo": Cargo,
            "CodexEntry": CodexEntry,
            "Commander": Commander,
            "DiscoveryScan": DiscoveryScan,
            "Docked": Docked,
            "DockingCancelled": DockingCancelled,
            "DockingDenied": DockingDenied,
            "DockingGranted": DockingGranted,
            "DockingRequested": DockingRequested,
            "DockingTimeout": DockingTimeout,
            "Fileheader": Fileheader,
            "FSDJump": FSDJump,
            "FSDJumpConflicts": FSDJumpConflicts,
            "FSDJumpConflictsFaction": FSDJumpConflictsFaction,
            "FSDJumpFactions": FSDJumpFactions,
            "FSDJumpSystemFaction": FSDJumpSystemFaction,
            "FSDTarget": FSDTarget,
            "FSSAllBodiesFound": FSSAllBodiesFound,
            "FSSDiscoveryScan": FSSDiscoveryScan,
            "FSSSignalDiscovered": FSSSignalDiscovered,
            "LeaveBody": LeaveBody,
            "Liftoff": Liftoff,
            "LoadGame": LoadGame,
            "Loadout": Loadout,
            "Location": Location,
            "MaterialCollected": MaterialCollected,
            "MaterialDiscarded": MaterialDiscarded,
            "MaterialDiscovered": MaterialDiscovered,
            "Materials": Materials,
            "Missions": Missions,
            "MultiSellExplorationData": MultiSellExplorationData,
            "NavBeaconScan": NavBeaconScan,
            "NavRoute": NavRoute,
            "NewCommander": NewCommander,
            "Passengers": Passengers,
            "Powerplay": Powerplay,
            "Progress": Progress,
            "Rank": Rank,
            "Reputation": Reputation,
            "SAAScanComplete": SAAScanComplete,
            "SAASignalsFound": SAASignalsFound,
            "Scan": Scan,
            "SellExplorationData": SellExplorationData,
            "StartJump": StartJump,
            "Statistics": Statistics,
            "SupercruiseEntry": SupercruiseEntry,
            "SupercruiseExit": SupercruiseExit,
            "Touchdown": Touchdown,
            "Undocked": Undocked,
            "Music": Music
        }
        classname = switch.get(e, None)
        if (classname != None):
            method = getattr(classname, 'fromDict')
            val = method(line)
            return val
        return None

    def parseJournalsData(self):
        # TODO: Probably merge all the function in order to avoid repetitive loops
        self.timing.startTimingExecution()
        journal_file_names = self.filerJournalsByTimestamp()
        journals_data_lines = self.loadJournalLines(journal_file_names)
        self.journals = self.parseJournalLines(journals_data_lines)
        self.timing.stopTimingExecution()

    def filerJournalsByTimestamp(self):
        files = os.listdir(self.journals_path)
        journal_file_names = []
        for file in files:
            parts = file.split(".")
            if (parts[0] == "Journal"):
                journal_date = datetime.strptime(parts[1][0:6], "%y%m%d")
                if (
                    self.args.all_journals or
                    (self.args.journal_to is None and journal_date >= self.args.journal_from) or
                    (journal_date >= self.args.journal_from and self.args.journal_to >= journal_date)
                ):
                    journal_file_names.append(file)
        return journal_file_names

    def loadJournalLines(self, journal_file_names):
        journals_data_lines = []
        for filename in journal_file_names:
            with open("{}\\{}".format(self.journals_path, filename), "r", encoding="utf8") as json_file:
                lines = json_file.readlines()
                for l in lines:
                    line = json.loads(l)
                    if (not self.args.events or (line.get("event") in self.args.events)):
                        journals_data_lines.append(line)
        return journals_data_lines

    def parseJournalLines(self, journals_data_lines):
        journals = []
        for line in journals_data_lines:
            obj = self.createObjectByEvent(line)
            if (obj is not None):
                journals.append(obj)
        return journals

    #region Custom methods

    def loadGreenSystems(self):
        # TODO: Create generic object in order to hold system data and details from other events
        data = []
        self.timing.startTimingExecution()
        for line in self.journals:
            if (isinstance(line, FSDJump)):
                planets = []
                has_basic_materials = False
                has_standard_materials = False
                has_premium_materials = False
                is_green_system = False
                # TODO: 30ms at each loop
                scan_data = [l for l in self.journals if isinstance(l, Scan) and l.system_address == line.system_address]
                for planet in scan_data:
                    b = []
                    s = []
                    p = []
                    if (planet.landable and len(planet.materials) > 0):
                        b = [m.name for m in planet.materials if m.name in self.green_system_materials["basic"]]
                        s = [m.name for m in planet.materials if m.name in self.green_system_materials["standard"]]
                        p = [m.name for m in planet.materials if m.name in self.green_system_materials["premium"]]
                    if not has_basic_materials:
                        has_basic_materials = True if b else False
                    if not has_standard_materials:
                        has_standard_materials = True if s else False
                    if not has_premium_materials:
                        has_premium_materials = True if p else False
                    is_green_system = has_basic_materials and has_standard_materials and has_premium_materials
                    p = {
                        "system_address": planet.system_address,
                        "body_name": planet.body_name,
                        "surface_gravity": planet.surface_gravity,
                        "has_basic_materials": has_basic_materials,
                        "has_standard_materials": has_standard_materials,
                        "has_premium_materials": has_premium_materials,
                        "materials": {
                            "basic": b,
                            "standard": s,
                            "premium": p
                        }
                    }
                    planets.append(p)
                data.append({
                    "system": {
                        "name": line.star_system,
                        "address": line.system_address,
                        "star_pos": line.star_pos,
                        "is_green_system": is_green_system,
                        "planets": planets
                    }
                })
        self.timing.stopTimingExecution()
        return {
            "type": "green_systems",
            "data": data
        }

    def loadSystemCoordinates(self):
        coordinates = []
        for line in self.journals:
            if (isinstance(line, FSDJump)):
                if (len(line.star_pos) > 0):
                    coordinates.append(line.star_pos)
        return {
            "type": "coordinates",
            "data": np.array(coordinates).T
        }

    def getTotalEarnings(self):
        total_earnings = 0
        for line in self.journals:
            if (isinstance(line, SellExplorationData) or isinstance(line, MultiSellExplorationData)):
                total_earnings += line.total_earnings 
        print("Total earnings: {0:,} CR".format(total_earnings))
        return {
            "type": "total_earnings",
            "data": total_earnings
        }

    #endregion

class EDStats:
    filter_types: List[str]

    def __init__(self) -> None:
        self.filter_types = [
            "coordinates",
            "green_systems",
            "total_earnings"
        ]

    # TODO: initData can contain anything not just coordinates.
    # Probably pass event type as well
    def initData(self, data):
        if (data["type"] in self.filter_types):
            if (data["type"] == "coordinates"):
                self.x = data["data"][0]
                self.y = data["data"][1]
                self.z = data["data"][2]
            elif (data["type"] == "green_systems"):
                self.x = [m["system"]["star_pos"][0] for m in data["data"] if m["system"]["is_green_system"]]
                self.y = [m["system"]["star_pos"][1] for m in data["data"] if m["system"]["is_green_system"]]
                self.z = [m["system"]["star_pos"][2] for m in data["data"] if m["system"]["is_green_system"]]

    def initialize2DPlot(self):
        self.im = plt.imread("milky_way_ed_9000px.jpg")
        self.fig, self.ax = plt.subplots(figsize=(20, 20))
        self.fig.tight_layout()
        self.ax.imshow(self.im, extent=[-45000, 45000, -20000, 70000])

    def initialize3DPlot(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        # self.fig, self.ax = plt.subplots(subplot_kw=dict(projection="3d"))
        self.fig.tight_layout()
        self.ax.axes.set_xlim3d(left=-45000, right=45000)
        self.ax.axes.set_ylim3d(bottom=-20000, top=70000)
        self.ax.axes.set_zlim3d(bottom=-25000, top=25000)
        # self.ax.set(xlabel="X axis", ylabel="Y axis", title="test plot")

    def plot2DData(self):
        self.ax.plot(self.x, self.z)

    def scatter2DData(self):
        self.ax.scatter(self.x, self.z)

    def plot3DData(self):
        # inverted Y <-> Z axes
        self.ax.plot3D(self.x, self.z, self.y)

    def scatter3DData(self):
        self.im = plt.imread("milky_way_ed_9000px.jpg")
        # inverted Y <-> Z axes
        self.ax.scatter3D(self.x, self.z, self.y)

    def savePlotToFile(self):
        # self.fig.savefig("plot_{}.png".format(datetime.now().replace(microsecond=0).strftime("%Y-%m-%d_%H-%M-%S")), bbox_inches="tight")
        self.fig.savefig("plot.png", bbox_inches="tight")

    def showPlot(self):
        plt.show()


if __name__ == "__main__":
    # journal_date_from = datetime(2021, 1, 29)
    # journal_date_to = datetime(2023, 6, 1)

    ed = ED()
    ed.parseArgs()
    ed.parseJournalsData()
    data = ed.loadSystemCoordinates()
    # ed.getTotalEarnings()
    stats = EDStats()
    stats.initData(data)
    stats.initialize2DPlot()
    stats.scatter2DData()
    # stats.initialize3DPlot()
    # stats.scatter3DData()
    # stats.savePlotToFile()
    stats.showPlot()


