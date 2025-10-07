"""
Caminho do módulo: mcards.base.troop
"""

import pygame

class Unit(pygame.sprite.Sprite):
	"""
	Representa uma unidade genérica.
	Pode ser posicionada.
	"""
	
	def __init__(self, offset: list[pygame.math.Vector2], index: int, hitbox: pygame.Rect,
				blue_team: bool) -> None:
		"""
		Crie uma nova instância de uma unidade genérica.
		
		:param offset: -> O deslocamento para cada índice.
		:param index: -> O índice atual da instância.
		:param hitbox: -> A caixa de colisão da unidade.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__()
		
		self.__hitbox = hitbox
		self.__blue_team = blue_team
		
		self.__position = offset[index]
		self.__surface = pygame.Surface((80, 80))
	
	def update(self, delta_time_ms: int) -> None:
		"""
		Atualize a unidade com base no tempo-delta.
		
		:param delta_time_ms: -> O tempo-delta passado na chamada em milissegundos.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		pass
	
	def draw(self, surface: pygame.Surface) -> None:
		"""
		Desenhe a unidade em cima da superfície solicitada.
		
		:param surface: -> A superfície para desenhar a unidade em cima.
		"""
		
		surface.blit(self.__surface, self.__position)

class Troop(Unit):
	"""
	Representa uma unidade de tropa.
	Pode ser posicionada, atacar e se mover.
	"""
	
	def __init__(self, offset: list[pygame.math.Vector2], index: int, hitbox: pygame.Rect, blue_team: bool,
				hitpoints: int, damage: int, first_attack_delay_ms: int, attack_delay_ms: int, tile_speed_ms: int,
				attack_range: int, move_type: str, target_types: str) -> None:
		"""
		Crie uma nova instância de uma tropa.
		
		:param offset: -> O deslocamento para cada índice.
		:param index: -> O índice atual da instância.
		:param hitbox: -> A caixa de colisão da unidade.
		:param hitpoints: -> Os ponos de vida da tropa.
		:param damage: -> O dano base da tropa.
		:param first_attack_delay_ms: -> O intervalo do primeiro ataque em milissegundos.
		:param attack_delay_ms: -> O intervalo após o primeiro ataque em milissegundos.
		:param tile_speed_ms: -> A velocidade de movimento em milissegundos.
		:param attack_range: -> O alcance de ataque.
		:param move_type: -> O tipo de movimento.
		:param target_types: -> O tipo de alvos da tropa.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__(offset, index, hitbox, blue_team)
		
		self.__hitpoints = hitpoints
		self.__damage = damage
		self.__first_attack_delay_ms = first_attack_delay_ms
		self.__attack_delay_ms = attack_delay_ms
		self.__tile_speed_ms = tile_speed_ms
		self.__attack_range = attack_range
		self.__move_type = move_type
		self.__target_types = target_types

class Spell(Unit):
	"""
	Representa uma unidade de feitiço.
	Pode ser posicionado, conjurado e afetar outras instâncias.
	"""
	
	def __init__(self, offset: list[pygame.math.Vector2], index: int, hitbox: pygame.Rect, blue_team: bool,
				damage: int, effect_area: int, target_types: str) -> None:
		"""
		Crie uma nova instância de um feitiço.
		
		:param offset: -> O deslocamento para cada índice.
		:param index: -> O índice atual da instância.
		:param hitbox: -> A caixa de colisão da unidade.
		:param damage: -> O dano base do feitiço.
		:param effect_area: -> O alcance de efeito.
		:param target_types: -> O tipo de unidades afetadas pelo feitiço.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__(offset, index, hitbox, blue_team)
		
		self.__damage = damage
		self.__effect_area = effect_area
		self.__targets_types = targets_types
