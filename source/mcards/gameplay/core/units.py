# Module path: mcards.gameplay.core.units

import pygame

class Unit(pygame.sprite.Sprite):
	"""
	Represents the main unit system, with the minimal resources.

	Fields:
	------------------------------------------------------------------------------------------
	1. __offset (pygame.math.Vector2) - the relative deploy offset (after summoning the unit).
	2. __deploy_time (int) - the deploy time (in ticks).
	------------------------------------------------------------------------------------------
	"""
	
	def __init__(self, blue_team: bool, offset: pygame.math.Vector2, deploy_time: int):
		"""
		Initialize the troop system.
		"""
		
		super().__init__()
		
		self.__blue_team = blue_team
		self.__offset = offset
		self.__deploy_time = deploy_time
	
	def get_offset(self):
		return self.__offset
	
	def get_deploy_time(self):
		return self.__deploy_time

class Hero(Unit):
	"""
	Represents the hero - the most important unit to the entire match, including defense system and more.
	
	Fields:
	----------------------------------------------------------------------------
	1. __hitpoints (int) - the troop's hitpoints.
	2. __damage (int) - the troops's damage.
	3. __first_attack_delay (int) - the first attack delay (in ticks).
	4. __attack_delay (int) - the sequential attack delay (after the first one).
	5. __attack_range (int) - the attack range (in tiles).
	----------------------------------------------------------------------------
	"""
	
	def __init__(self, hitpoints: int, damage: int, first_attack_delay: int,
				attack_delay: int, attack_range: int):
		"""
		Initialize the troop system.
		"""
		
		super().__init__(pygame.math.Vector2(0, 0), 0)
		
		self.__hitpoints = hitpoints
		self.__damage = damage
		self.__first_attack_delay = first_attack_delay
		self.__attack_delay = attack_delay
		self.__attack_range = attack_range

class Troop(Unit):
	"""
	Represents the troop, including movement system and more.

	Fields:
	----------------------------------------------------------------------------
	1. __hitpoints (int) - the troop's hitpoints.
	2. __damage (int) - the troops's damage.
	3. __first_attack_delay (int) - the first attack delay (in ticks).
	4. __attack_delay (int) - the sequential attack delay (after the first one).
	5. __move_speed (int) - the movement speed (in tiles per tick).
	6. __movement_type (str) - the troop's movement type (from the enum).
	7. __targets (str) - the troop's target type (from the enum).
	----------------------------------------------------------------------------
	"""
	
	def __init__(self, blue_team, offset: pygame.math.Vector2, deploy_time: int,
				hitpoints: int, damage: int, first_attack_delay: int,
				attack_delay: int, attack_range: int, move_speed: int, movement_type: str, targets: str):
		"""
		Initialize the troop system.
		"""
		
		super().__init__(blue_team, offset, deploy_time)
		
		self.__hitpoints = hitpoints
		self.__damage = damage
		self.__first_attack_delay = first_attack_delay
		self.__attack_delay = attack_delay
		self.__move_speed = move_speed
		self.__attack_range = attack_range
		self.__movement_type = movement_type
		self.__targets = targets

class Spell(Unit):
	"""
	Represents the spell, including attacks and immediate effects.

	Fields:
	----------------------------------------------------------------------------
	1. __damage (int) - the spell's damage.
	2. __first_attack_delay (int) - the first attack delay (in ticks).
	3. __attack_delay (int) - the sequential attack delay (after the first one).
	4. __effect_area (int) - the effect's area (in tiles).
	5. __ticks_to_end (int) - the maximun ticks to end the effect (in ticks).
	----------------------------------------------------------------------------
	"""
	
	def __init__(self, offset: pygame.math.Vector2, deploy_time: int,
				damage: int, first_attack_delay: int, attack_delay: int, effect_area: int, ticks_to_end: int):
		"""
		Initialize the spell system.
		"""
		
		super().__init__(offset, deploy_time)
		
		self.__damage = damage
		self.__first_attack_delay = first_attack_delay
		self.__attack_delay = attack_delay
		self.__effect_area = effect_area
		self.__ticks_to_end = ticks_to_end

class Building(Unit):
	"""
	Represents the building, including static state system and more.

	Fields:
	----------------------------------------------------------------------------
	1. __hitpoints (int) - the troop's hitpoints.
	2. __damage (int) - the troops's damage.
	3. __first_attack_delay (int) - the first attack delay (in ticks).
	4. __attack_delay (int) - the sequential attack delay (after the first one).
	5. __ticks_to_end (int) - the maximun ticks to end the effect (in ticks).
	6. __targets (str) - the troop's target type (from the enum).
	----------------------------------------------------------------------------
	"""
	
	def __init__(self, offset: pygame.math.Vector2, deploy_time: int,
				hitpoints: int, damage: int, first_attack_delay: int, attack_delay: int,
				attack_range: int, ticks_to_end: int, targets: str):
		"""
		Initialize the building system.
		"""
		
		super().__init__(offset, deploy_time)
		
		self.__hitpoints = hitpoints
		self.__damage = damage
		self.__first_attack_delay = first_attack_delay
		self.__attack_delay = attack_delay
		self.__ticks_to_end = ticks_to_end
		self.__targets = targets
		self.__attack_range = attack_range
		self.__targets = targets
