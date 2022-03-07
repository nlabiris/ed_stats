from datetime import datetime
from typing import Any
from helper import Helper


class BankAccount:
    current_wealth: int
    spent_on_ships: int
    spent_on_outfitting: int
    spent_on_repairs: int
    spent_on_fuel: int
    spent_on_ammo_consumables: int
    insurance_claims: int
    spent_on_insurance: int

    def __init__(self, current_wealth: int, spent_on_ships: int, spent_on_outfitting: int, spent_on_repairs: int, spent_on_fuel: int, spent_on_ammo_consumables: int, insurance_claims: int, spent_on_insurance: int) -> None:
        self.current_wealth = current_wealth
        self.spent_on_ships = spent_on_ships
        self.spent_on_outfitting = spent_on_outfitting
        self.spent_on_repairs = spent_on_repairs
        self.spent_on_fuel = spent_on_fuel
        self.spent_on_ammo_consumables = spent_on_ammo_consumables
        self.insurance_claims = insurance_claims
        self.spent_on_insurance = spent_on_insurance

    @staticmethod
    def fromDict(obj: Any) -> 'Combat':
        assert isinstance(obj, dict)
        current_wealth = Helper.fromInteger(obj.get("Current_Wealth", 0))
        spent_on_ships = Helper.fromInteger(obj.get("Spent_On_Ships", 0))
        spent_on_outfitting = Helper.fromInteger(obj.get("Spent_On_Outfitting", 0))
        spent_on_repairs = Helper.fromInteger(obj.get("Spent_On_Repairs", 0))
        spent_on_fuel = Helper.fromInteger(obj.get("Spent_On_Fuel", 0))
        spent_on_ammo_consumables = Helper.fromInteger(obj.get("Spent_On_Ammo_Consumables", 0))
        insurance_claims = Helper.fromInteger(obj.get("Insurance_Claims", 0))
        spent_on_insurance = Helper.fromInteger(obj.get("Spent_On_Insurance", 0))
        return Combat(current_wealth, spent_on_ships, spent_on_outfitting, spent_on_repairs, spent_on_fuel, spent_on_ammo_consumables, insurance_claims, spent_on_insurance)

class Combat:
    bounties_claimed: int
    bounty_hunting_profit: int
    combat_bonds: int
    combat_bond_profits: int
    assassinations: int
    assassination_profits: int
    highest_single_reward: int
    skimmers_killed: int

    def __init__(self, bounties_claimed: int, bounty_hunting_profit: int, combat_bonds: int, combat_bond_profits: int, assassinations: int, assassination_profits: int, highest_single_reward: int, skimmers_killed: int) -> None:
        self.bounties_claimed = bounties_claimed
        self.bounty_hunting_profit = bounty_hunting_profit
        self.combat_bonds = combat_bonds
        self.combat_bond_profits = combat_bond_profits
        self.assassinations = assassinations
        self.assassination_profits = assassination_profits
        self.highest_single_reward = highest_single_reward
        self.skimmers_killed = skimmers_killed

    @staticmethod
    def fromDict(obj: Any) -> 'Combat':
        assert isinstance(obj, dict)
        bounties_claimed = Helper.fromInteger(obj.get("Bounties_Claimed", 0))
        bounty_hunting_profit = Helper.fromInteger(obj.get("Bounty_Hunting_Profit", 0))
        combat_bonds = Helper.fromInteger(obj.get("Combat_Bonds", 0))
        combat_bond_profits = Helper.fromInteger(obj.get("Combat_Bond_Profits", 0))
        assassinations = Helper.fromInteger(obj.get("Assassinations", 0))
        assassination_profits = Helper.fromInteger(obj.get("Assassination_Profits", 0))
        highest_single_reward = Helper.fromInteger(obj.get("Highest_Single_Reward", 0))
        skimmers_killed = Helper.fromInteger(obj.get("Skimmers_Killed", 0))
        return Combat(bounties_claimed, bounty_hunting_profit, combat_bonds, combat_bond_profits, assassinations, assassination_profits, highest_single_reward, skimmers_killed)

class Crime:
    fines: int
    total_fines: int
    bounties_received: int
    total_bounties: int
    highest_bounty: int

    def __init__(self, fines: int, total_fines: int, bounties_received: int, total_bounties: int, highest_bounty: int) -> None:
        self.fines = fines
        self.total_fines = total_fines
        self.bounties_received = bounties_received
        self.total_bounties = total_bounties
        self.highest_bounty = highest_bounty

    @staticmethod
    def fromDict(obj: Any) -> 'Crime':
        assert isinstance(obj, dict)
        fines = Helper.fromInteger(obj.get("Fines", 0))
        total_fines = Helper.fromInteger(obj.get("Total_Fines", 0))
        bounties_received = Helper.fromInteger(obj.get("Bounties_Received", 0))
        total_bounties = Helper.fromInteger(obj.get("Total_Bounties", 0))
        highest_bounty = Helper.fromInteger(obj.get("Highest_Bounty", 0))
        return Crime(fines, total_fines, bounties_received, total_bounties, highest_bounty)

class Smuggling:
    black_markets_traded_with: int
    black_markets_profits: int
    resources_smuggled: int
    average_profit: int
    highest_single_transaction: int

    def __init__(self, black_markets_traded_with: int, black_markets_profits: int, resources_smuggled: int, average_profit: int, highest_single_transaction: int) -> None:
        self.black_markets_traded_with = black_markets_traded_with
        self.black_markets_profits = black_markets_profits
        self.resources_smuggled = resources_smuggled
        self.average_profit = average_profit
        self.highest_single_transaction = highest_single_transaction

    @staticmethod
    def fromDict(obj: Any) -> 'Smuggling':
        assert isinstance(obj, dict)
        black_markets_traded_with = Helper.fromInteger(obj.get("Black_Markets_Traded_With", 0))
        black_markets_profits = Helper.fromInteger(obj.get("Black_Markets_Profits", 0))
        resources_smuggled = Helper.fromInteger(obj.get("Resources_Smuggled", 0))
        average_profit = Helper.fromFloat(obj.get("Average_Profit", 0))
        highest_single_transaction = Helper.fromInteger(obj.get("Highest_Single_Transaction", 0))
        return Smuggling(black_markets_traded_with, black_markets_profits, resources_smuggled, average_profit, highest_single_transaction)

class Trading:
    markets_traded_with: int
    market_profits: int
    resources_traded: int
    average_profit: int
    highest_single_transaction: int

    def __init__(self, markets_traded_with: int, market_profits: int, resources_traded: int, average_profit: int, highest_single_transaction: int) -> None:
        self.markets_traded_with = markets_traded_with
        self.market_profits = market_profits
        self.resources_traded = resources_traded
        self.average_profit = average_profit
        self.highest_single_transaction = highest_single_transaction

    @staticmethod
    def fromDict(obj: Any) -> 'Trading':
        assert isinstance(obj, dict)
        markets_traded_with = Helper.fromInteger(obj.get("Markets_Traded_With", 0))
        market_profits = Helper.fromInteger(obj.get("Market_Profits", 0))
        resources_traded = Helper.fromInteger(obj.get("Resources_Traded", 0))
        average_profit = Helper.fromFloat(obj.get("Average_Profit", 0))
        highest_single_transaction = Helper.fromInteger(obj.get("Highest_Single_Transaction", 0))
        return Trading(markets_traded_with, market_profits, resources_traded, average_profit, highest_single_transaction)

class Mining:
    mining_profits: int
    quantity_mined: int
    materials_collected: int

    def __init__(self, mining_profits: int, quantity_mined: int, materials_collected: int) -> None:
        self.mining_profits = mining_profits
        self.quantity_mined = quantity_mined
        self.materials_collected = materials_collected

    @staticmethod
    def fromDict(obj: Any) -> 'Mining':
        assert isinstance(obj, dict)
        mining_profits = Helper.fromInteger(obj.get("Mining_Profits", 0))
        quantity_mined = Helper.fromInteger(obj.get("Quantity_Mined", 0))
        materials_collected = Helper.fromInteger(obj.get("Materials_Collected", 0))
        return Mining(mining_profits, quantity_mined, materials_collected)

class Exploration:
    systems_visited: int
    fuel_scooped: int
    fuel_purchased: int
    exploration_profits: int
    planets_scanned_to_level_2: int
    planets_scanned_to_level_3: int
    highest_payout: int
    total_hyperspace_distance:int
    total_hyperspace_jumps: int
    greatest_distance_from_start: float
    time_played: int

    def __init__(self, systems_visited: int, fuel_scooped: int, fuel_purchased: int, exploration_profits: int, planets_scanned_to_level_2: int, planets_scanned_to_level_3: int, highest_payout: int, total_hyperspace_distance: int, total_hyperspace_jumps: int, greatest_distance_from_start: float, time_played: int) -> None:
        self.systems_visited = systems_visited
        self.fuel_scooped = fuel_scooped
        self.fuel_purchased = fuel_purchased
        self.exploration_profits = exploration_profits
        self.planets_scanned_to_level_2 = planets_scanned_to_level_2
        self.planets_scanned_to_level_3 = planets_scanned_to_level_3
        self.highest_payout = highest_payout
        self.total_hyperspace_distance = total_hyperspace_distance
        self.total_hyperspace_jumps = total_hyperspace_jumps
        self.greatest_distance_from_start = greatest_distance_from_start
        self.time_played = time_played

    @staticmethod
    def fromDict(obj: Any) -> 'Exploration':
        assert isinstance(obj, dict)
        systems_visited = Helper.fromInteger(obj.get("Systems_Visited", 0))
        fuel_scooped = Helper.fromInteger(obj.get("Fuel_Scooped", 0))
        fuel_purchased = Helper.fromInteger(obj.get("Fuel_Purchased", 0))
        exploration_profits = Helper.fromInteger(obj.get("Exploration_Profits", 0))
        planets_scanned_to_level_2 = Helper.fromInteger(obj.get("Planets_Scanned_To_Level_2", 0))
        planets_scanned_to_level_3 = Helper.fromInteger(obj.get("Planets_Scanned_To_Level_3", 0))
        highest_payout = Helper.fromInteger(obj.get("Highest_Payout", 0))
        total_hyperspace_distance = Helper.fromInteger(obj.get("Total_Hyperspace_Distance", 0))
        total_hyperspace_jumps = Helper.fromInteger(obj.get("Total_Hyperspace_Jumps", 0))
        greatest_distance_from_start = Helper.fromFloat(obj.get("Time_Played", 0))
        time_played = Helper.fromInteger(obj.get("Total_Hyperspace_Jumps", 0))
        return Exploration(systems_visited, fuel_scooped, fuel_purchased, exploration_profits, planets_scanned_to_level_2, planets_scanned_to_level_3, highest_payout, total_hyperspace_distance, total_hyperspace_jumps, greatest_distance_from_start, time_played)

class Passengers:
    passengers_missions_bulk: int
    passengers_missions_vip: int
    passengers_missions_delivered: int
    passengers_missions_ejected: int

    def __init__(self, passengers_missions_bulk: int, passengers_missions_vip: int, passengers_missions_delivered: int, passengers_missions_ejected: int) -> None:
        self.passengers_missions_bulk = passengers_missions_bulk
        self.passengers_missions_vip = passengers_missions_vip
        self.passengers_missions_delivered = passengers_missions_delivered
        self.passengers_missions_ejected = passengers_missions_ejected

    @staticmethod
    def fromDict(obj: Any) -> 'Passengers':
        assert isinstance(obj, dict)
        passengers_missions_bulk = Helper.fromInteger(obj.get("Passengers_Missions_Bulk", 0))
        passengers_missions_vip = Helper.fromInteger(obj.get("Passengers_Missions_VIP", 0))
        passengers_missions_delivered = Helper.fromInteger(obj.get("Passengers_Missions_Delivered", 0))
        passengers_missions_ejected = Helper.fromInteger(obj.get("Passengers_Missions_Ejected", 0))
        return Passengers(passengers_missions_bulk, passengers_missions_vip, passengers_missions_delivered, passengers_missions_ejected)

class SearchAndRescue:
    search_rescue_traded: int
    search_rescue_profit: int
    search_rescue_count: int

    def __init__(self, search_rescue_traded: int, search_rescue_profit: int, search_rescue_count: int) -> None:
        self.search_rescue_traded = search_rescue_traded
        self.search_rescue_profit = search_rescue_profit
        self.search_rescue_count = search_rescue_count

    @staticmethod
    def fromDict(obj: Any) -> 'SearchAndRescue':
        assert isinstance(obj, dict)
        search_rescue_traded = Helper.fromInteger(obj.get("SearchRescue_Traded", 0))
        search_rescue_profit = Helper.fromInteger(obj.get("SearchRescue_Profit", 0))
        search_rescue_count = Helper.fromInteger(obj.get("SearchRescue_Count", 0))
        return SearchAndRescue(search_rescue_traded, search_rescue_profit, search_rescue_count)

class Crafting:
    spent_on_crafting: int
    count_of_used_engineers: int
    recipes_generated: int
    recipes_generated_rank_1: int
    recipes_generated_rank_2: int
    recipes_generated_rank_3: int
    recipes_generated_rank_4: int
    recipes_generated_rank_5: int
    recipes_applied: int
    recipes_applied_rank_1: int
    recipes_applied_rank_2: int
    recipes_applied_rank_3: int
    recipes_applied_rank_4: int
    recipes_applied_rank_5: int
    recipes_applied_on_previously_modified_modules: int

    def __init__(self, spent_on_crafting: int, count_of_used_engineers: int, recipes_generated: int, recipes_generated_rank_1: int, recipes_generated_rank_2: int, recipes_generated_rank_3: int, recipes_generated_rank_4: int, recipes_generated_rank_5: int, recipes_applied: int, recipes_applied_rank_1: int, recipes_applied_rank_2: int, recipes_applied_rank_3, recipes_applied_rank_4: int, recipes_applied_rank_5: int, recipes_applied_on_previously_modified_modules: int) -> None:
        self.spent_on_crafting = spent_on_crafting
        self.count_of_used_engineers = count_of_used_engineers
        self.recipes_generated = recipes_generated
        self.recipes_generated_rank_1 = recipes_generated_rank_1
        self.recipes_generated_rank_2 = recipes_generated_rank_2
        self.recipes_generated_rank_3 = recipes_generated_rank_3
        self.recipes_generated_rank_4 = recipes_generated_rank_4
        self.recipes_generated_rank_5 = recipes_generated_rank_5
        self.recipes_applied = recipes_applied
        self.recipes_applied_rank_1 = recipes_applied_rank_1
        self.recipes_applied_rank_2 = recipes_applied_rank_2
        self.recipes_applied_rank_3 = recipes_applied_rank_3
        self.recipes_applied_rank_4 = recipes_applied_rank_4
        self.recipes_applied_rank_5 = recipes_applied_rank_5
        self.recipes_applied_on_previously_modified_modules = recipes_applied_on_previously_modified_modules

    @staticmethod
    def fromDict(obj: Any) -> 'Crafting':
        assert isinstance(obj, dict)
        spent_on_crafting = Helper.fromInteger(obj.get("SearchRescue_Traded", 0))
        count_of_used_engineers = Helper.fromInteger(obj.get("SearchRescue_Profit", 0))
        recipes_generated = Helper.fromInteger(obj.get("SearchRescue_Count", 0))
        recipes_generated_rank_1 = Helper.fromInteger(obj.get("Recipes_Generated_Rank_1", 0))
        recipes_generated_rank_2 = Helper.fromInteger(obj.get("Recipes_Generated_Rank_2", 0))
        recipes_generated_rank_3 = Helper.fromInteger(obj.get("Recipes_Generated_Rank_3", 0))
        recipes_generated_rank_4 = Helper.fromInteger(obj.get("Recipes_Generated_Rank_4", 0))
        recipes_generated_rank_5 = Helper.fromInteger(obj.get("Recipes_Generated_Rank_5", 0))
        recipes_applied = Helper.fromInteger(obj.get("Recipes_Applied", 0))
        recipes_applied_rank_1 = Helper.fromInteger(obj.get("Recipes_Applied_Rank_1", 0))
        recipes_applied_rank_2 = Helper.fromInteger(obj.get("Recipes_Applied_Rank_2", 0))
        recipes_applied_rank_3 = Helper.fromInteger(obj.get("Recipes_Applied_Rank_3", 0))
        recipes_applied_rank_4 = Helper.fromInteger(obj.get("Recipes_Applied_Rank_4", 0))
        recipes_applied_rank_5 = Helper.fromInteger(obj.get("Recipes_Applied_Rank_5", 0))
        recipes_applied_on_previously_modified_modules = Helper.fromInteger(obj.get("Recipes_Applied_On_Previously_Modified_Modules", 0))
        return Crafting(spent_on_crafting, count_of_used_engineers, recipes_generated, recipes_generated_rank_1, recipes_generated_rank_2, recipes_generated_rank_3, recipes_generated_rank_4, recipes_generated_rank_5, recipes_applied, recipes_applied_rank_1, recipes_applied_rank_2, recipes_applied_rank_3, recipes_applied_rank_4, recipes_applied_rank_5, recipes_applied_on_previously_modified_modules)

class Crew:
    npc_crew_total_wages: int
    npc_crew_hired: int
    npc_crew_fired: int
    npc_crew_died: int

    def __init__(self, npc_crew_total_wages: int, npc_crew_hired: int, npc_crew_fired: int, npc_crew_died: int) -> None:
        self.npc_crew_total_wages = npc_crew_total_wages
        self.npc_crew_hired = npc_crew_hired
        self.npc_crew_fired = npc_crew_fired
        self.npc_crew_died = npc_crew_died

    @staticmethod
    def fromDict(obj: Any) -> 'Crew':
        assert isinstance(obj, dict)
        npc_crew_total_wages = Helper.fromInteger(obj.get("NpcCrew_TotalWages", 0))
        npc_crew_hired = Helper.fromInteger(obj.get("NpcCrew_Hired", 0))
        npc_crew_fired = Helper.fromInteger(obj.get("NpcCrew_Fired", 0))
        npc_crew_died = Helper.fromInteger(obj.get("NpcCrew_Died", 0))
        return Crew(npc_crew_total_wages, npc_crew_hired, npc_crew_fired, npc_crew_died)

class Multicrew:
    multicrew_time_total: int
    multicrew_gunner_time_total: int
    multicrew_fighter_time_total: int
    multicrew_credits_total: int
    multicrew_fines_total: int

    def __init__(self, multicrew_time_total: int, multicrew_gunner_time_total: int, multicrew_fighter_time_total: int, multicrew_credits_total: int, multicrew_fines_total: int) -> None:
        self.multicrew_time_total = multicrew_time_total
        self.multicrew_gunner_time_total = multicrew_gunner_time_total
        self.multicrew_fighter_time_total = multicrew_fighter_time_total
        self.multicrew_credits_total = multicrew_credits_total
        self.multicrew_fines_total = multicrew_fines_total

    @staticmethod
    def fromDict(obj: Any) -> 'Multicrew':
        assert isinstance(obj, dict)
        multicrew_time_total = Helper.fromInteger(obj.get("Multicrew_Time_Total", 0))
        multicrew_gunner_time_total = Helper.fromInteger(obj.get("Multicrew_Gunner_Time_Total", 0))
        multicrew_fighter_time_total = Helper.fromInteger(obj.get("Multicrew_Fighter_Time_Total", 0))
        multicrew_credits_total = Helper.fromInteger(obj.get("Multicrew_Credits_Total", 0))
        multicrew_fines_total = Helper.fromInteger(obj.get("Multicrew_Fines_Total", 0))
        return Multicrew(multicrew_time_total, multicrew_gunner_time_total, multicrew_fighter_time_total, multicrew_credits_total, multicrew_fines_total)

class MaterialTraderStats:
    trades_completed: int
    materials_traded: int

    def __init__(self, trades_completed: int, materials_traded: int) -> None:
        self.trades_completed = trades_completed
        self.materials_traded = materials_traded

    @staticmethod
    def fromDict(obj: Any) -> 'MaterialTraderStats':
        assert isinstance(obj, dict)
        trades_completed = Helper.fromInteger(obj.get("Trades_Completed", 0))
        materials_traded = Helper.fromInteger(obj.get("Materials_Traded", 0))
        return MaterialTraderStats(trades_completed, materials_traded)

class Statistics:
    timestamp: datetime
    event: str
    bank_account: BankAccount
    combat: Combat
    crime: Crime
    smuggling: Smuggling
    trading: Trading
    mining: Mining
    exploration: Exploration
    passengers: Passengers
    search_and_rescue: SearchAndRescue
    crafting: Crafting
    crew: Crew
    multicrew: Multicrew
    material_trader_stats: MaterialTraderStats

    def __init__(self, timestamp: datetime, event: str, bank_account: BankAccount, combat: Combat, crime: Crime, smuggling: Smuggling, trading: Trading, mining: Mining, exploration: Exploration, passengers: Passengers, search_and_rescue: SearchAndRescue, crafting: Crafting, crew: Crew, multicrew: Multicrew, material_trader_stats: MaterialTraderStats) -> None:
        self.timestamp = timestamp
        self.event = event
        self.bank_account = bank_account
        self.combat = combat
        self.crime = crime
        self.smuggling = smuggling
        self.trading = trading
        self.mining = mining
        self.exploration = exploration
        self.passengers = passengers
        self.search_and_rescue = search_and_rescue
        self.crafting = crafting
        self.crew = crew
        self.multicrew = multicrew
        self.material_trader_stats = material_trader_stats

    @staticmethod
    def fromDict(obj: Any) -> 'Statistics':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        bank_account = BankAccount.fromDict(obj.get("Bank_Account", {}))
        combat = Combat.fromDict(obj.get("Combat", {}))
        crime = Crime.fromDict(obj.get("Crime", {}))
        smuggling = Smuggling.fromDict(obj.get("Smuggling", {}))
        trading = Trading.fromDict(obj.get("Trading", {}))
        mining = Mining.fromDict(obj.get("Mining", {}))
        exploration = Exploration.fromDict(obj.get("Exploration", {}))
        passengers = Passengers.fromDict(obj.get("Passengers", {}))
        search_and_rescue = SearchAndRescue.fromDict(obj.get("Search_And_Rescue", {}))
        crafting = Crafting.fromDict(obj.get("Crafting", {}))
        crew = Crew.fromDict(obj.get("Crew", {}))
        multicrew = Multicrew.fromDict(obj.get("Multicrew", {}))
        material_trader_stats = MaterialTraderStats.fromDict(obj.get("Material_Trader_Stats", {}))
        return Statistics(timestamp, event, bank_account, combat, crime, smuggling, trading, mining, exploration, passengers, search_and_rescue, crafting, crew, multicrew, material_trader_stats)
