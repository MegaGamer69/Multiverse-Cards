# Module path: mcards.engine

import pygame

from .gvars import *

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
	
	def initialize(self, mobile):
		"""
		Initializes the engine functions.
		"""
		
		ENGINE = Engine()
		
		pygame.init()
		
		initialize_units()
		initialize_cards()
		
		player = Player()
		game_manager = GameManager(player)
		running = True
		clock = pygame.time.Clock()
		
		if mobile:
			# Fixed size if the OS is a Android or iOS system.
			
			WINDOW_SIZE = (720, 1280)
		
		window = pygame.display.set_mode(WINDOW_SIZE)
		
		while running:
			# Difines the delta time.
			
			delta_time = clock.tick(60)
			
			for e in pygame.event.get():
				# When the QUIT event is called:
				
				if e.type == pygame.QUIT:
					running = False
			
			window.fill(pygame.Color(255, 255, 255))
			game_manager.draw(window)
			
			pygame.display.flip()
		
		pygame.quit()

