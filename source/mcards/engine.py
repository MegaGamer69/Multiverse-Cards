# Module path: mcards.engine

import pygame

from .gameplay.core.units import Card, Hero, Troop, Spell, Building

class Engine:
	"""
	The main gameplay Engine.
	Contains every needed functions to handle stuffs.
	
	Fields:
	---------------------------------------------------------------------
	1. __cards (dict[str, Card]) - the card dictionary.
	2. __heroes (dict[str, Hero]) - the hero dictionary.
	2. __troops (dict[str, Troop]) - the troop dictionary.
	3. __spells (dict[str, Spell]) - the spell dictionary.
	4. __buildings (dict[str, Building]) - the building dictionary.
	----------------------------------------------------------------------
	"""
	def __init__(self):
		"""
		Initialize the Engine module.
		"""
		
		self.__cards = {}
		self.__heroes = {}
		self.__troops = {}
		self.__spells = {}
		self.__buildings = {}
		
	def register_card(self, name: str, card: Card):
		"""
		Register the card to the dictionary.
		"""
		
		self.__cards.update({name: card})
		
	def register_hero(self, name: str, hero: Hero):
		"""
		Register the spell to the dictionary.
		"""
		
		self.__heroes.update({name: heroes})
	
	def register_troop(self, name: str, troop: Troop):
		"""
		Register the troop to the dictionary.
		"""
		
		self.__troops.update({name: troop})
	
	def register_spell(self, name: str, spell: Spell):
		"""
		Register the spell to the dictionary.
		"""
		
		self.__spells.update({name: spell})
	
	def register_building(self, name: str, building: Building):
		"""
		Register the building to the dictionary.
		"""
		
		self.__buildings.update({name: building})
