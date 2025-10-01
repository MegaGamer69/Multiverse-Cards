# Module path: mcards.gameplay.game_state

import pygame

import mcards.gdefs as gdefs

from mcards.gameplay.player import Player

from mcards.gameplay.factory.card_factory import *

CHANGE_STATE = pygame.USEREVENT + 1

MENU_STATE_ELEMENTS = pygame.sprite.Group()
PLAY_STATE_ELEMENTS = pygame.sprite.Group()

class GameState:
	"""
	Base class for every game states.
	
	Fields:
	---------------------------------------------------------------------
	1. __manager (StateManager) - the state manager instance.
	2. __elements (list[]) - the element sprite group.
	3. __surface (Surface) - the state surface background.
	---------------------------------------------------------------------
	"""
	
	def __init__(self, manager, elements):
		"""
		Create a new instance of the game state.
		"""
		
		self.__manager = manager
		self.__elements = elements
		
		self.__surface = pygame.Surface((720, 1280))
	
	def handle_events(self, events, mobile):
		pass
	
	def get_surface(self):
		return self.__surface
	
	def draw(self, surface: pygame.Surface):
		surface.blit(self.__surface, (0, 0))
		self.__elements.draw(surface)
	
	def flip(self, delta_time: float):
		pass
	
	def add_sprite(self, sprite: pygame.sprite.Sprite):
		pass

class MenuState(GameState):
	"""
	The starting menu of the game.
	"""
	
	def __init__(self, manager):
		super().__init__(manager, MENU_STATE_ELEMENTS)
		
		self.get_surface().fill((200, 200, 200))
	
	def handle_events(self, events, mobile):
		for e in events:
			if mobile:
				if e.type == pygame.FINGERDOWN:
					touch_position = pygame.math.Vector2(e.x, e.y)
			else:
				if e.type == pygame.MOUSEBUTTONDOWN:
					mouse_position = pygame.mouse.get_pos()

class PlayState(GameState):
	"""
	The gameplay state of the game.
	"""
	
	def __init__(self, manager):
		super().__init__(manager, PLAY_STATE_ELEMENTS)
		
		self.get_surface().fill((0, 100, 255))
	
	def add_sprite_card(self, reg_id: str):
		self.add_sprite(gdefs.get_registered_card(sprite))
	
	def handle_events(self, events, mobile):
		for e in events:
			if mobile:
				if e.type == pygame.FINGERDOWN:
					touch_position = pygame.math.Vector2(e.x, e.y)
			else:
				if e.type == pygame.MOUSEBUTTONDOWN:
					mouse_position = pygame.mouse.get_pos()

class GameManager:
	"""
	Base class for every game states.
	
	Fields:
	---------------------------------------------------------------------
	1. __player (Player) - the player instance.
	2. __states (dict[str, GameState]) - the state dictionary.
	3. __current_state (GameState) - the current state instance.
	---------------------------------------------------------------------
	"""
	
	def __init__(self, player: Player):
		self.__player = player
		
		self.__states = {
			"menu_state": MenuState(self),
			"play_state": PlayState(self),
		}
		self.__current_state = self.__states["play_state"]
		
		for reg_id in player.get_collected_cards_reg_ids():
			if hasattr(self.__current_state, "add_sprite_reg_id"):
				 self.__current_state.add_sprite_red_id(reg_id)
	
	def get_player(self):
		return self.__player
	
	def get_current_state(self):
		return self.__current_state
	
	def set_state(self, state_name: str):
		if state_name in self.__states:
			self.__current_state = self.__states[state_name]
	
	def draw(self, surface):
		self.__current_state.draw(surface)
