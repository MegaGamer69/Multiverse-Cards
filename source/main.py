"""
Caminho do módulo: main
"""

import pygame

pygame.init()

import mcards

import kivy

kivy.require("2.1.0")

from kivy.config import Config

Config.set("graphics", "width", "720")
Config.set("graphics", "height", "1280")
Config.set("graphics", "resizable", "0")
Config.set("graphics", "fullscreen", "0")
Config.set("input", "hidinput", "")
Config.set("input", "mtdev", "")
Config.set("input", "mouse", "mouse")

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window

class PygameWidget(Widget):
	"""
	Um widget que contém e gerencia a superfície da biblioteca `pygame`.
	"""
	
	def __init__(self, **kwargs):
		"""
		Crie uma nova instância do widget.
		
		:param kwargs: -> Os argumentos do widget.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__(**kwargs)
		
		self.__size = Window.size
		self.__pygame_surface = pygame.Surface(self.__size)

class Application(App):
	"""
	Uma classe de aplicativo utilizando a biblioteca `kivy` junto da `pygame`.
	"""
	
	def __init__(self, **kwargs) -> None:
		"""
		Crie uma nova instância de aplicativo do jogo.
		
		:param kwargs: -> Os argumentos do aplicativo.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__(**kwargs)
	
	def build(self) -> None:
		"""
		Contrói a interface do aplicativo.
		"""
		
		main_layout = BoxLayout(orientation="vertical", padding=0, spacing=0)
		
		return main_layout

if __name__ == "__main__":
	Application().run()
