"""
Caminho do módulo: mcards.register
"""

class Register:
	"""
	A classe de registro principal do sistema de jogabilidade.
	"""
	
	__CARDS = {}
	__TROOPS = {}
	__SPELLS = {}
	
	@classmethod
	def register_card(cls, key: str, value) -> None:
		"""
		Registra uma carta no dicionário.
		
		:param key: -> Uma chave de registro da carta.
		:param value: -> Um valor de armazenamento da carta.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		cls.__CARDS.update({key: value})
	
	@classmethod
	def register_troop(cls, key: str, value) -> None:
		"""
		Registra uma tropa no dicionário.
		
		:param key: -> Uma chave de registro da tropa.
		:param value: -> Um valor de armazenamento da tropa.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		cls.__TROOPS.update({key: value})
	
	@classmethod
	def register_spell(cls, key: str, value) -> None:
		"""
		Registra um feitiço no dicionário.
		
		:param key: -> Uma chave de registro do feitiço.
		:param value: -> Um valor de armazenamento do feitiço.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		cls.__SPELLS.update({key: value})
	
	@classmethod
	def get_registered_card(cls, key: str):
		"""
		Obtenha uma carta do dicionário.
		
		:param key: -> A chave do registro de cartas.
		:return: -> A classe da carta será retornada.
		"""
		
		if not key in cls.__CARDS:
			raise KeyError(f"Não há evidencia nenhuma de carta com o registro {key}")
		
		return cls.__CARDS[key]
	
	@classmethod
	def get_registered_troop(cls, key: str):
		"""
		Obtenha uma tropa do dicionário.
		
		:param key: -> A chave do registro de tropas.
		:return: -> A classe da tropa será retornada.
		"""
		
		if not key in cls.__TROOPS:
			raise KeyError(f"Não há evidência nenhuma de tropa com o registro {key}")
		
		return cls.__TROOPS[key]
	
	@classmethod
	def get_registered_spell(cls, key: str):
		"""
		Obtenha um feitiço do dicionário.
		
		:param key: -> A chave do registro de tropas.
		:return: -> A classe do feitiço será retornada.
		"""
		
		if not key in cls.__SPELLS:
			raise KeyError(f"Não há evidência nenhuma de feitiço com o registro {key}")
		
		return cls.__SPELLS[key]
