"""
Caminho do módulo: mcards.globals.gdefs
"""

from mcards.register import Register

def register_card(key: str, value) -> None:
	"""
	Registra uma carta no dicionário (use este método para registrar).
	
	:param key: -> Uma chave de registro da carta.
	:param value: -> Um valor de armazenamento da carta.
	:return: -> Nenhum valor a ser retornado.
	"""
	
	Register.register_card(key, value)

def register_troop(key: str, value) -> None:
	"""
	Registra uma tropa no dicionário (use este método para registrar).
	
	:param key: -> Uma chave de registro da tropa.
	:param value: -> Um valor de armazenamento da tropa.
	:return: -> Nenhum valor a ser retornado.
	"""
	
	Register.register_troop(key, value)

def get_registered_card(key: str):
	"""
	Obtenha uma carta do dicionário.
	
	:param key: -> A chave do registro de cartas.
	:return: -> A classe da carta será retornada.
	"""
	
	return Register.get_registered_card(key)

def get_registered_troop(key: str):
	"""
	Obtenha uma tropa do dicionário.
	
	:param key: -> A chave do registro de tropas.
	:return: -> A classe da tropa será retornada.
	"""
	
	return Register.get_registered_troop(key)
