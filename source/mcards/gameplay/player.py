# Module path: mcards.gameplay.player

import random

import mcards.gvars as gvars

class Player:
	"""
	The player controller (not the client handler).
	Contains the basic functions to manage the player state.
	"""
	
	def __init__(self):
		self.__blue_side = True
		self.__collected_cards = [
			gvars.ENGINE.get_registered_card("card_gravedigger"),
			gvars.ENGINE.get_registered_card("card_indians"),
			gvars.ENGINE.get_registered_card("card_pelican"),
			gvars.ENGINE.get_registered_card("card_bomb"),
		]
		self.__card_deck = []
		self.__card_hand = []
		self.__elixir = 5
	
	def is_blue_side(self) -> bool:
		return self.__blue_side
	
	def set_blue_side(self, value: bool):
		self.__blue_side = value
	
	def get_collected_cards(self):
		return self.__collected_cards
	
	def get_card_deck(self):
		return self.__card_deck
	
	def get_card_hand(self):
		return self.__card_hand
	
	def get_elixir(self):
		return self.__elixir
	
	def setup_player_deck(self, indexes):
		self.__card_deck = [self.__collected_cards[i](self.__blue_side) for i in indexes]
		
		self.__shuffle_player_deck()
	
	def __shuffle_player_deck(self):
		random.shuffle(self.__card_deck)
