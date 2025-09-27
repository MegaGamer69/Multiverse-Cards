import pygame
import time
from collections import deque
import random

from global_variables import *

def center_value_to_grid(position, size):
	x, y = position
	w, h = size
	
	center_x = x - w / 2
	center_y = y - h / 2
	
	snapped_x = round(center_x / GRID_SIZE) * GRID_SIZE
	snapped_y = round(center_y / GRID_SIZE) * GRID_SIZE
	
	return pygame.math.Vector2(snapped_x, snapped_y)

def center_position_to_grid(position):
	x, y = position
	
	snapped_x = round(x / GRID_SIZE) * GRID_SIZE
	snapped_y = round(y / GRID_SIZE) * GRID_SIZE
	
	return pygame.math.Vector2(snapped_x, snapped_y)

class Player:
	def __init__(self, blue_side):
		self._blue_side = blue_side
		
		self._current_elixir = 5
		self._max_elixir = 10
		self._last_elixir_update = time.time()
		self._player_deck = []
		self._player_hand = []
		self._card_queue = deque()
		self._selected_card = None
		
		self.units = []
	
	def setup_deck(self, available_cards, deck_indices):
		self._player_deck = [available_cards[index](self._blue_side) for index in deck_indices]
		
		self.__shuffle_deck()
		self.__draw_initial_hand()
		
		for card in self._player_deck:
			print(card.get_display_name())
	
	def __shuffle_deck(self):
		random.shuffle(self._player_deck)
		
		self._card_queue = deque(self._player_deck)
	
	def __draw_initial_hand(self):
		self._player_hand = []
		
		for _ in range(min(4, len(self._card_queue))):
			if self._card_queue:
				self._player_hand.append(self._card_queue.popleft())
	
	def __draw_cards(self):
		if self._card_queue and len(self._player_hand) < 4:
			self._player_hand.append(self._card_queue.popleft())

			if not self._card_queue:
				self.__shuffle_deck()
	
	def update(self, delta_time):
		self._current_elixir = min(self._current_elixir + (1 / ELIXIR_TOTAL_TIME) * delta_time, self._max_elixir)
		
		for card in self._player_hand:
			card.update(self._current_elixir)
	
	def get_player_deck(self):
		return self._player_deck
	
	def get_player_hand(self):
		return self._player_hand
	
	def get_hand_positions(self, screen_width):
		card_width = 120
		card_spacing = 10
		total_width = len(self._player_hand) * card_width + (len(self._player_hand) - 1) * card_spacing
		start_x_position = (screen_width - total_width) // 2
		
		positions = []
		
		for index in range(len(self._player_hand)):
			x = start_x_position + index * (card_width + card_spacing)
			
			positions.append((x, 1024))
		
		return positions
	
	def try_to_summon(self, card_index, position):
		if 0 <= card_index < len(self._player_hand):
			card = self._player_hand[card_index]
			units, cost = card.summon_card(position)
			
			if units:
				self._current_elixir -= cost
				
				self._player_hand.pop(card_index)
				self.__draw_cards()
				
				return units
		
		return None
	
	def get_elixir(self):
		return self._current_elixir
