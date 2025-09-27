import pygame
import time

from game_manager import center_value_to_grid

rarity_colors = {
	"Common": (31, 31, 255),
	"Rare": (255, 255, 31),
	"Epic": (255, 31, 255),
	"Exclusive": (255, 31, 31),
}

class Card(pygame.sprite.Sprite):
	"""
	Represents the game card, inherting the `pygame.sprite.Sprite` class to renderize stuffs.

	Attributes:
		1. _display_name (str): cool display name (must be simple and cool, like Giant Theropod);
		2. _deploy_cost (int): deploy cost (0 to 10);
		3. _asset_path (str): path to local assets (images, animations and `.json` data);
		4. _instance_spawns (list): unit list (can be a troop, building or spell);
		5. _instance_type (str): reference of type like a troop, building or spell;
		6. _collect_rarity (str): repeated collect rarity like common, rare, epic or exclusive (e.g.: event only);
	"""
	
	def __init__(self, name, cost, asset, spawns, type, rarity, blue_side):
		super().__init__()
		
		self._display_name = name
		self._deploy_cost = cost
		self._asset_path = asset
		self._instance_spawns = spawns
		self._instance_type = type
		self._collect_rarity = rarity
		self._blue_side = blue_side
		
		self._usable = False
		self._overlay_surface = pygame.Surface((120, 160), pygame.SRCALPHA)
		self._rarity_surface = pygame.Surface((128, 168))
		
		try:
			self._image_surface = pygame.image.load(f"./assets/cards/{asset}.png")
			self._image_surface = pygame.transform.scale(self._image_surface, (120, 160))
			self._image_loaded = True
		except FileNotFoundError:
			self._image_surface = pygame.Surface((120, 160))
			self._image_loaded = False
		
		self._selected = False
		
		self._rarity_surface.fill(rarity_colors[self._collect_rarity])
	
	def get_display_name(self):
		return self._display_name
	
	def get_deploy_cost(self):
		return self._deploy_cost
	
	def get_asset_path(self):
		return self._asset_path
	
	def get_instance_spawns(self):
		return self._instance_spawns
	
	def get_image_surface(self):
		return self._image_surface
	
	def get_overlay_surface(self):
		return self._overlay_surface
	
	def get_rarity_surface(self):
		return self._rarity_surface
	
	def __str__(self):
		return "Card(\"{}\", cost: {}, asset: {}, type: {}, rarity: {})".format(
			self._display_name,
			self._deploy_cost,
			self._asset_path,
			self._instance_type,
			self._collect_rarity
		)
	
	def update(self, current_elixir):
		self._usable = (current_elixir >= self._deploy_cost)
		
		if not self._usable:
			self._overlay_surface.fill((100, 100, 100, 128))
		else:
			self._overlay_surface.fill((0, 0, 0, 0))
	
	def is_selected(self):
		return self._selected
	
	def set_selected(self, value):
		self._selected = value
	
	def summon_card(self, position):
		if not self._usable:
			return None, 0
			
		spawned_instances = []
		
		for instance_class in self._instance_spawns:
			unit = instance_class(self._blue_side)
			
			rect = unit.get_image_surface().get_size()
			
			if self._instance_type == "Troop":
				normalized_position = pygame.math.Vector2(
					position[0],
					position[1] - (rect[1] / 2)
				)
			else:
				normalized_position = pygame.math.Vector2(
					position[0],
					position[1]
				)
			
			unit.set_position(center_value_to_grid(normalized_position, rect))
			spawned_instances.append(unit)
		
		return spawned_instances, self._deploy_cost


