# Module path: mcards.gdefs

import mcards.gvars as gvars

from .gameplay.player import Player
from .gameplay.core.cards import *
from .gameplay.core.units import *

def register_card(name: str, card: type[Card]):
	gvars.ENGINE.register_card(name, card)

def register_hero(name: str, hero: type[Hero]):
	gvars.ENGINE.register_hero(name, hero)

def register_troop(name: str, troop: type[Troop]):
	gvars.ENGINE.register_troop(name, troop)

def register_spell(name: str, spell: type[Spell]):
	gvars.ENGINE.register_spell(name, spell)

def register_building(name: str, building: type[Building]):
	gvars.ENGINE.register_building(name, building)

def get_registered_card(name: str) -> type[Card]:
	return gvars.ENGINE.get_registered_card(name)

def get_registered_hero(name: str) -> type[Hero]:
	return gvars.ENGINE.get_registered_hero(name)

def get_registered_troop(name: str) -> type[Troop]:
	return gvars.ENGINE.get_registered_troop(name)

def get_registered_spell(name: str) -> type[Spell]:
	return gvars.ENGINE.get_registered_spell(name)

def get_registered_building(name: str) -> type[Building]:
	return gvars.ENGINE.get_registered_building(name)

def add_player(blue_team: bool, player: Player):
	gvars.ENGINE.add_player(blue_team, player)

def get_player(blue_team: bool) -> Player:
	return gvars.ENGINE.get_player(blue_team)
