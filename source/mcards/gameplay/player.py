# Module path: mcards.gameplay.player

class Player:
	"""
	The player controller (not the client handler).
	Contains the basic functions to manage the player state.
	"""
	
	def __init__(self):
		self.__collected_cards = []
		self.__card_deck = []
		self.__card_hand = []
		self.__elixir = 5
	
	def get_collected_cards(self):
		return self.__collected_cards
	
	def get_card_deck(self):
		return self.__card_deck
	
	def get_card_hand(self):
		return self.__card_hand
	
	def get_elixir(self):
		return self.__elixir
	
