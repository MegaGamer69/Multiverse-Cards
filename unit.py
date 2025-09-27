import pygame

from global_variables import *

class Hero(pygame.sprite.Sprite):
	"""
	Represents the main target of every troop, the main objective to defeat (and no, Hero is not a card).

	Attributes:
		1. _hitpoints (int): the hero's hitpoints (duh).
		2. _damage (int): the hero's damage per hit.
		3. _attack_delay (float): how many seconds the hero can hit after the first one.
		4. _first_attack_delay (float): how many seconds the hero can hit the first one.
		5. _attack_range (float): the attack distance in tiles.
	"""

	def __init__(self, hitpoints, damage, attack_delay, first_attack_delay, attack_range, blue_side):
		super().__init__()

		self._hitpoints = hitpoints
		self._damage = damage
		self._attack_delay = attack_delay
		self._first_attack_delay = first_attack_delay
		self._attack_range = attack_range
		self._blue_side = blue_side

		self._image_surface = pygame.Surface([100, 100])
		self._position = pygame.math.Vector2(320, 75)

		self._image_surface.fill("green")
		
		self._state = "Idle"
	
	def get_hitpoints(self):
		return self._hitpoints
	
	def get_image_surface(self):
		return self._image_surface
	
	def get_position(self):
		return self._position
	
	def is_blue_side(self):
		return self._blue_side
	
	def apply_damage(self, damage):
		self._hitpoints -= damage
		
		if self._hitpoints <= 0:
			self._on_destroy()
	
	def _on_destroy(self):
		self._state = "Dead"

class Troop(pygame.sprite.Sprite):
	def __init__(self, hitpoints, damage, attack_delay, first_attack_delay, tiles_per_second, sight_range, attack_range, is_air_movement, target_types, blue_side):
		super().__init__()

		self._hitpoints = hitpoints
		self._damage = damage
		self._attack_delay = attack_delay
		self._first_attack_delay = first_attack_delay
		self._tiles_per_second = tiles_per_second
		self._sight_range = sight_range
		self._attack_range = attack_range
		self._is_air_movement = is_air_movement
		self._target_types = target_types
		self._blue_side = blue_side

		self._attack_cooldown = self._first_attack_delay
		self._current_target = None
		self._state = "Moving"
		self._position = pygame.math.Vector2(0, 0)
		self._image_surface = pygame.Surface([100, 100])

		self._image_surface.fill("blue")
	
	def update(self, delta_time, all_units):
		if self._state == "Dead":
			return
		
		self._current_target = self._find_target(all_units)
		
		if self._current_target:
			distance = pygame.math.Vector2.distance_to(self._position, self._current_target.get_position())
			
			if distance <= self._attack_range * GRID_SIZE:
				if self._state != "Attacking":
					self._state = "Attacking"
					self._attack_cooldown = self._first_attack_delay
			else:
				self._state = "Moving"
		
		if self._state == "Moving" and self._current_target:
			self._position = pygame.math.Vector2.move_towards(
				self._position,
				self._current_target.get_position(),
				self._tiles_per_second * delta_time * GRID_SIZE
			)
		elif self._state == "Attacking" and self._current_target:
			self._attack_target(delta_time)
	
	def _find_target(self, all_units):
		if not all_units:
			return None
		
		enemy_units = [unit for unit in all_units if not unit.is_blue_side() == self._blue_side]
		
		if not enemy_units:
			return None
		
		return min(enemy_units, key=lambda enemy: self._position.distance_to(enemy.get_position()))
	
	def _attack_target(self, delta_time):
		if self._state == "Dead":
			return
		
		if not self._current_target:
			self._state = "Moving"
			
			return
		
		distance = pygame.math.Vector2.distance_to(self._position, self._current_target.get_position())
		
		if distance > self._attack_range * GRID_SIZE:
			self._state = "Moving"
			
			return
		
		self._attack_cooldown -= delta_time
		
		if self._attack_cooldown <= 0.0:
			print("The troop is attacking!")
			
			self._current_target.apply_damage(self._damage)
			
			self._attack_cooldown = self._attack_delay
	
	def apply_damage(self, damage):
		self._hitpoints -= damage
		
		if self._hitpoints <= 0:
			self._on_destroy()
	
	def _on_destroy(self):
		self._state = "Dead"
	
	def get_hitpoints(self):
		return self._hitpoints
	
	def get_image_surface(self):
		return self._image_surface
	
	def get_position(self):
		return self._position
	
	def set_position(self, position):
		self._position = position
	
	def is_blue_side(self):
		return self._blue_side

class Building(pygame.sprite.Sprite):
	def __init__(self, hitpoints, damage, attack_delay, first_attack_delay, attack_range, life_time, target_types):
		super().__init__()

		self._hitpoints = hitpoints
		self._damage = damage
		self._attack_delay = attack_delay
		self._first_attack_delay = first_attack_delay
		self._attack_range = attack_range
		self._life_time = life_time
		self._target_types = target_types

		self._image_surface = pygame.Surface([100, 100])

		self._image_surface.fill("purple")
	
	def apply_damage(self, damage):
		self._hitpoints -= damage
		
		if self._hitpoints <= 0:
			self._on_destroy()
	
	def _on_destroy(self):
		self._state = "Dead"
	
	def get_image_surface(self):
		return self._image_surface
	
	def get_position(self):
		return self._position
	
	def set_position(self, position):
		self._position = position

class Spell(pygame.sprite.Sprite):
	def __init__(self, damage_per_tick, tick_speed, max_ticks, effect_range, affects_air):
		super().__init__()

		self._damage_per_tick = damage_per_tick
		self._tick_speed = tick_speed
		self._max_ticks = max_ticks
		self._effect_range = effect_range
		self._affects_air = affects_air

		self._image_surface = pygame.Surface([100, 100])

		self._image_surface.fill("green")
	
	def get_image_surface(self):
		return self._image_surface
	
	def get_position(self):
		return self._position
	
	def set_position(self, position):
		self._position = position
