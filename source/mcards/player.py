"""
Caminho do módulo: mcards.player
"""

import random
import pygame

from .globals.gdefs import get_registered_card
from .globals.gvars import TEAMS

class Player:
	"""
	Uma classe básica de jogador (sem manipulador de cliente).
	"""
	
	def __init__(self) -> None:
		"""
		Crie uma instância da classe de jogador.
		
		:param team: -> O nome do time do jogador.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		self.__team = "blue" if not TEAMS["blue"] else "red"
		self.__unlocked_cards = []
		self.__deck = []
		self.__hand = []
		
		self.initialize_deck()
	
	def initialize_deck(self) -> None:
		"""
		Inicialize o baralho do jogador.
		
		:return: -> Nenhum valor a ser retornado.
		"""
		
		cards_to_unlock = ["gravedigger", "indians", "pelican", "seagulls", "bandit", "l_robot", "storm", "whale"]
		
		for card_key in cards_to_unlock:
			self.__unlock_card(card_key)
		
		deck_instances = []
		
		for card_key in self.__unlocked_cards:
			card_instance = get_registered_card(card_key)()
			
			card_instance.load_image_with_register(card_key)
			deck_instances.append(card_instance)
		
		random.shuffle(deck_instances)
		
		self.__deck = deck_instances
		self.__hand = self.__deck[:4] # 4 Cartas por mão.
		self.__deck = self.__deck[4:] # 4 Cartas de volta para o baralho.
	
	def __unlock_card(self, card_key: str) -> None:
		"""
		Inicialize o baralho do jogador.
		
		:param card_key: -> O registro da carta.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		self.__unlocked_cards.append(card_key)
	
	def get_hand_position(self, index) -> pygame.math.Vector2:
		"""
		Obtém a posição de mão com base no índice.
		
		:param card_key: -> O índice relativo da carta (de 1 a 4).
		:return: -> Um vetor bidimensional, representando a posição.
		"""
		
		return pygame.math.Vector2(0 + (index * 140), 320)
	
	def get_team(self):
		"""
		Obtenha o time do jogador.
		
		:return: -> O nome do time do jogador.
		"""
		
		return self.__team
	
	def get_unlocked_cards(self):
		"""
		Obtenha a lista de cartas desbloqueadas por chave de registro.
		
		:return: -> A lista de cartas desbloqueadas.
		"""
		
		return self.__unlocked_cards
	
	def get_deck(self):
		"""
		Obtenha o baralho do jogador.
		
		:return: -> O baralho do jogador.
		"""
		
		return self.__deck
	
	def get_hand(self):
		"""
		Obtenha a mão atual do jogador.
		
		:return: -> A mão do jogador.
		"""
		
		return self.__hand
