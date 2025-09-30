# Module path: mcards.engine

import pygame

import mcards.gvars as gvars

from .gameplay.game_state import GameManager
from .gameplay.player import Player

from .gameplay.core.cards import *
from .gameplay.core.units import *

from .gameplay.factory.unit_factory import initialize_units
from .gameplay.factory.card_factory import initialize_cards

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
		
		self.__cards: dict[str, type[Card]] = {}
		self.__heroes: dict[str, type[Hero]] = {}
		self.__troops: dict[str, type[Troop]] = {}
		self.__spells: dict[str, type[Spell]] = {}
		self.__buildings: dict[str, type[Building]] = {}
		self.__players: dict[str, Player] = {}
	
	def register_card(self, name: str, card: type[Card]):
		"""
		Register the card to the dictionary.
		"""
		
		print(f"Card {name} registered!")
		
		self.__cards.update({name: card})
	
	def register_hero(self, name: str, hero: type[Hero]):
		"""
		Register the spell to the dictionary.
		"""
		
		print(f"Hero {name} registered!")
		
		self.__heroes.update({name: hero})
	
	def register_troop(self, name: str, troop: type[Troop]):
		"""
		Register the troop to the dictionary.
		"""
		
		print(f"Troop {name} registered!")
		
		self.__troops.update({name: troop})
	
	def register_spell(self, name: str, spell: type[Spell]):
		"""
		Register the spell to the dictionary.
		"""
		
		print(f"Spell {name} registered!")
		
		self.__spells.update({name: spell})
	
	def register_building(self, name: str, building: type[Building]):
		"""
		Register the building to the dictionary.
		"""
		
		print(f"Building {name} registered!")
		
		self.__buildings.update({name: building})
	
	def add_player(self, blue_team: bool, player: Player):
		"""
		Add the player to the dictionary.
		"""
		
		player_id = "blue" if blue_team else "red"
		
		player.set_blue_side(blue_team)
		
		self.__players[player_id] = player
	
	def get_registered_card(self, name: str) -> type[Card]:
		"""
		Get the card on register.
		If the card does not exists, raises a error.
		"""
		
		if not name in self.__cards:
			raise KeyError(f"No card founded with the register \"{name}\".")
		
		return self.__cards[name]
	
	def get_registered_hero(self, name: str) -> type[Hero]:
		"""
		Get the hero on register.
		If the hero does not exists, raises a error.
		"""
		
		if not name in self.__heroes:
			raise KeyError(f"No hero founded with the register \"{name}\".")
		
		return self.__heroes[name]
	
	def get_registered_troop(self, name: str) -> type[Troop]:
		"""
		Get the troop on register.
		If the troop does not exists, raises a error.
		"""
		
		if not name in self.__troops:
			raise KeyError(f"No troop founded with the register \"{name}\".")
		
		return self.__troops[name]
	
	def get_registered_spell(self, name: str) -> type[Spell]:
		"""
		Get the troop on register.
		If the troop does not exists, raises a error.
		"""
		
		if not name in self.__spells:
			raise KeyError(f"No spell founded with the register \"{name}\".")
		
		return self.__spells[name]
	
	def get_registered_building(self, name: str) -> type[Building]:
		"""
		Get the building on register.
		If the troop does not exists, raises a error.
		"""
		
		if not name in self.__buildings:
			raise KeyError(f"No building founded with the register \"{name}\".")
		
		return self.__buildings[name]
	
	def get_player(self, blue_team: bool) -> Player:
		"""
		Get the player on match.
		"""
		
		player_id = "blue" if blue_team else "red"
		
		return self.__players[player_id]
	
	def initialize(self, mobile: bool):
		"""
		Initializes the engine functions.
		"""
		
		pygame.init()
		
		initialize_units()
		initialize_cards()
		
		player = Player()
		
		self.add_player(True, player)
		
		game_manager = GameManager(player)
		running = True
		clock = pygame.time.Clock()
		
		window = pygame.display.set_mode(gvars.WINDOW_SIZE)
		
		while running:
			# Difines the delta time.
			
			delta_time = clock.tick(60)
			
			for e in pygame.event.get():
				# When the QUIT event is called:
				
				if e.type == pygame.QUIT:
					running = False
			
			window.fill(pygame.Color(255, 255, 255))
			game_manager.draw(window)
			
			for card in self.get_player(True).get_card_deck():
				card.draw(screen)
			
			pygame.display.flip()
		
		pygame.quit()

