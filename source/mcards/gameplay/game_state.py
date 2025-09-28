# Module path: mcards.gameplay.game_state

import pygame

from mcards.gameplay.player import Player

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
	---------------------------------------------------------------------
	"""
	
	def __init__(self, manager, elements):
		"""
		Create a new instance of the game state.
		"""
		
		self.__manager = manager
		self.__elements = elements
		
		self.__surface = pygame.Surface((720, 1280))
		
		self.__surface.fill(pygame.Color(200, 200, 200))
	
	def handle_events(self, events, mobile):
		pass
	
	def draw(self, surface):
		surface.blit(self.__surface, (0, 0))
	
	def flip(self, delta_time):
		pass

class MenuState(GameState):
	"""
	The starting menu of the game.
	"""
	
	def __init__(self, manager):
		super().__init__(manager, MENU_STATE_ELEMENTS)
	
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
		self.__current_state = self.__states["menu_state"]
	
	def get_player(self):
		return self.__player
	
	def get_current_state(self):
		return self.__current_state
	
	def set_state(self, state_name: str):
		if state_name in self.__states:
			self.__current_state = self.__states[state_name]
	
	def draw(self, surface):
		self.__current_state.draw(surface)
