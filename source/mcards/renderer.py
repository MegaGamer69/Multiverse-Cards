"""
Caminho do módulo: mcards.renderer
"""

import pygame

class PreRenderedUI:
	"""
	Pré-renderizador de interface do usuário.
	"""
	
	HAND_BG = None
	CARD_COST_BG = None
	
	@classmethod
	def pre_render_hand(cls) -> None:
		"""
		Pré-renderize o fundo da mão principal.
		
		:return: -> Nenhum valor a ser retornado.
		"""
		
		cls.HAND_BG = pygame.Surface([720, 480])
		
		cls.HAND_BG.fill(pygame.Color(128, 128, 32))
	
	@classmethod
	def pre_render_card_cost(cls) -> None:
		"""
		Pré-renderize o fundo dos custos das cartas.
		
		:return: -> Nenhum valor a ser retornado.
		"""
		
		cls.CARD_COST_BG = pygame.Surface([40, 40], pygame.SRCALPHA)
		
		cls.CARD_COST_BG.fill(pygame.Color(0, 0, 0, 128))
