# Module path: mcards.gameplay.player

import random

import pygame
import mcards.gvars as gvars

class Player:
	"""
	The player controller (not the client handler).
	Contains the basic functions to manage the player state.
	"""
	
	def __init__(self):
		self.__blue_side = True
		self.__collected_cards = []
		self.__collected_cards_reg_id = [
			"card_gravedigger",
			"card_indians",
			"card_pelican",
			"card_bomb",
			"card_wave",
			"card_bandit",
			"card_l_robot",
			"card_bombers",
		]
		self.__card_deck = []
		self.__card_hand = []
		self.__elixir = 5
		
		for reg_id in self.__collected_cards_reg_id:
			self.unlock_card(reg_id)
	
	def is_blue_side(self) -> bool:
		return self.__blue_side
	
	def set_blue_side(self, value: bool):
		self.__blue_side = value
	
	def get_collected_cards_reg_ids(self):
		return self.__collected_cards_reg_id
	
	def get_collected_cards(self):
		return self.__collected_cards
	
	def get_card_deck(self):
		return self.__card_deck
	
	def get_card_hand(self):
		return self.__card_hand
	
	def get_elixir(self):
		return self.__elixir
	
	def unlock_card(self, reg_id: str):
		self.__collected_cards.append(gvars.ENGINE.get_registered_card(reg_id))
	
	def setup_player_deck(self, indexes: list[int]):
		self.__card_deck = [self.__collected_cards[i](1, self.__blue_side) for i in indexes]
		
		for i, card_instance in enumerate(self.__card_deck):
			reg_id = self.__collected_cards_reg_id[indexes[i]]
			
			card_instance.load_image(reg_id)
		
		self.__shuffle_player_deck()
	
	def __shuffle_player_deck(self):
		random.shuffle(self.__card_deck)
		
		self.__card_hand = self.__card_deck[4:]
	
	def get_hand_position(self, index):
		x = 80 + (index * 140)
		
		return pygame.math.Vector2(x, 1024)
	
	def __get_card_reg_id_pairs(self):
		return zip(self.__collected_cards, self.__collected_cards_reg_id)
