# Module path: mcards.gdefs

import mcards.gvars as gvars

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
	gvars.ENGINE.register_spell(name, building)
