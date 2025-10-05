"""
Caminho do módulo: mcards.base.card
"""

import pygame

from mcards.globals.gvars import *

class Card(pygame.sprite.Sprite):
	"""
	Representa uma carta do baralho.
	Pode ser coletada, equipada e aprimorada.
	
	A imagem de exibição não precisa ser explícitamente associada, o registro já lida com isso.
	"""
	
	def __init__(self, name_variations: dict[str, str], cost: int, description_variations: str, summons: dict[str, int]):
		"""
		Cria uma nova instância de carta genérica.
		
		:param name_variations: -> O dicionário de traduções do nome da carta.
		:param cost: -> O custo de implantação da carta.
		:param description_variations: -> O dicionário de traduções da descrição da carta.
		:param summons: -> O dicionário de invocações da carta. Incluindo o registro da unidade e a quantidade.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__()
		
		self.__name_variations = name_variations
		self.__cost = cost
		self.__description_variations = description_variations
	
	def get_name_variations(self):
		"""
		Obtenha o dicionário de traduções do nome da carta.
		
		:return: -> O valor referente ao dicionário de traduções.
		"""
		
		return self.__name_variations
	
	def get_cost(self):
		"""
		Obtenha o custo de implantação da carta.
		
		:return: -> O valor referente ao custo de implantação.
		"""
		
		return self.__cost
	
	def get_description_variations(self):
		"""
		Obtenha o dicionário de traduções da descrição da carta.
		
		:return: -> O valor referente ao dicionário de traduções.
		"""
		
		return self.__description_variations

