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

from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window

from mcards.player import Player

from mcards.globals.gdefs import get_registered_card

from mcards.factory.unit_factory import initialize_units
from mcards.factory.card_factory import initialize_cards

initialize_units()
initialize_cards()

player = Player()

class PygameWidget(Widget):
	"""
	Um widget que contém e gerencia a superfície da biblioteca `pygame`.
	"""
	
	def __init__(self, **kwargs) -> None:
		"""
		Crie uma nova instância do widget.
		
		:param **kwargs: -> Os argumentos do widget.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__(**kwargs)
		
		self.size = Window.size
		self.__pygame_surface = pygame.Surface(self.size)
		
		Clock.schedule_interval(self.update, 1.0 / 60.0)
	
	def update(self, delta_time: float) -> None:
		"""
		Atualize a nova instância do widget.
		
		:param delta_time: -> O tempo-delta da execução.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		self.__pygame_surface.fill((0, 0, 0))
		
		for index, card in enumerate(player.get_hand()):
			self.__pygame_surface.blit(card.get_surface(), player.get_hand_position(index))
		
		self.draw()
	
	def draw(self) -> None:
		"""
		Desenhe uma superfície do widget.
		
		:return: -> Nenhum valor a ser retornado.
		"""
		
		pygame_string = pygame.image.tostring(self.__pygame_surface, "RGB")
		texture = Texture.create(size=self.__pygame_surface.get_size())
		
		texture.blit_buffer(pygame_string, colorfmt='rgb', bufferfmt='ubyte')
		
		self.canvas.clear()
		
		with self.canvas:
			Rectangle(texture=texture, pos=self.pos, size=self.size)

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
		
		pygame_widget = PygameWidget()
		
		main_layout.add_widget(pygame_widget)
		pygame_widget.draw()
		
		return main_layout

if __name__ == "__main__":
	Application().run()
