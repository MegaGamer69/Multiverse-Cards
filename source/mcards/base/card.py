"""
Caminho do módulo: mcards.base.card
"""

import pygame
import os

from kivy.resources import resource_find
from kivy.logger import Logger

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
		
		self.__surface = pygame.Surface([120, 160])
	
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
	
	def get_surface(self):
		"""
		Obtenha a superfície da carta.
		
		:return: -> O valor referente a superfície da carta.
		"""
		
		return self.__surface
	
	def load_image_with_register(self, key: str) -> None:
		"""
		Carregue a imagem com base na chave de registro da carta.
		Requer o tipo de arquivo `.png` para carregar.
		
		Caminho requirido: `assets/images/cards/{key}.png`;
		
		:param key: -> A chave do registro que será obtida.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		if not isinstance(key, str):
			raise ValueError(f"Tentativa de usar um objeto diferente de string. Tipo: {type(key)};")
		
		image_path = None
		found_path = resource_find(f"source/assets/images/card/{key}.png")
		
		if found_path:
			image_path = found_path
			
			Logger.info(f"Caminho de arquivo encontrado: {found_path};")
		
		else:
			Logger.error(f"Caminho de arquivo não encontrado!")
			
			self.__surface.fill(pygame.Color(255, 0, 0))
			
			return
		
		loaded = pygame.image.load(image_path)
		
		self.__surface = pygame.transform.smoothscale(loaded, [120, 160])

