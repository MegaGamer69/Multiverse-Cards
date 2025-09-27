import pygame
import os

from card_factory import *
from game_manager import *

pygame.init()

all_cards = get_all_cards()
all_units = []
player_units = []
all_enemies = [HeroPirate(False)]

frame_rate = 60
screen_res = (720, 1280)
screen_center_x = 720 / 2
elixir_bar_x = (720 - 480) / 2
elixir_bar_y = 1200

spawn_rect = pygame.Rect(0, 500, 720, 1000)

global mouse_position

class PreRenderedUI:
	ELIXIR_BAR_BG = None
	ELIXIR_BAR_TRACK = None
	ELIXIR_BAR_MARKERS = None
	CARD_COST_BG = None
	CARD_RARITY_BG = None
	SPAWN_AREA_BG = None
	
	@classmethod
	def initialize_all(cls):
		cls.pre_render_elixir_bar()
		cls.pre_render_card_costs()
		cls.pre_render_spawn_area()
	
	@classmethod
	def pre_render_elixir_bar(cls):
		cls.ELIXIR_BAR_BG = pygame.Surface((560, 56))
		cls.ELIXIR_BAR_TRACK = pygame.Surface((494, 44))
		
		cls.ELIXIR_BAR_BG.fill((75, 75, 85))
		cls.ELIXIR_BAR_TRACK.fill((128, 128, 128))
		
		cls.ELIXIR_BAR_MARKERS = []
		
		for index in range(9):
			marker = pygame.Surface((6, 56))
			
			marker.fill((75, 75, 85))
			cls.ELIXIR_BAR_MARKERS.append(marker)
	
	@classmethod
	def pre_render_card_costs(cls):
		cls.CARD_COST_BG = pygame.Surface((30, 30))
		
		cls.CARD_COST_BG.fill((255, 255, 0))
	
	@classmethod
	def pre_render_spawn_area(cls):
		cls.SPAWN_AREA_BG = pygame.Surface((720, 500))
		
		cls.SPAWN_AREA_BG.fill((200, 200, 200))

class Launcher:
	ELIXIR_TEXT_FONT = pygame.font.SysFont("", 30)
	COST_TEXT_FONT = pygame.font.SysFont("", 30)
	DRAGGING_CARD = None
	DRAGGING_INDEX = -1
	CARD_OFFSET = (0, 0)
	GLOW_TIMER = 0.0
	LAST_ELIXIR_INT = 0
	NEXT_ELIXIR_INT = 0
	
	PLAYER = Player(True)
	
	def launch_mcards():
		PreRenderedUI.initialize_all()
		
		Launcher.PLAYER.setup_deck(all_cards, [0, 1, 2, 3, 4, 5, 6, 7])
		
		for index, card in enumerate(all_cards):
			print(f"{index}: {all_cards[index](True).__str__()}")
		
		screen = pygame.display.set_mode(screen_res)
		clock = pygame.time.Clock()
		running = True
		
		pygame.display.set_caption("Multiverse Cards")
		
		Launcher.__update_game_state(running, screen, clock)
	
	@staticmethod
	def __update_game_state(running, screen, clock):
		while running:
			delta_time = clock.tick(frame_rate) / 1000.0
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				elif event.type == pygame.FINGERDOWN:
					mouse_position = (event.x * 720, event.y * 1280)
					
					hand_positions = Launcher.PLAYER.get_hand_positions(720)
					
					for index, position in enumerate(hand_positions):
						card_rect = pygame.Rect(position[0], position[1], 120, 160)
						
						if card_rect.collidepoint(mouse_position) and index < len(Launcher.PLAYER.get_player_hand()):
							card = Launcher.PLAYER.get_player_hand()[index]
							
							Launcher.DRAGGING_CARD = card
							Launcher.DRAGGING_INDEX = index
							Launcher.CARD_OFFSET = (
								mouse_position[0] - position[0],
								mouse_position[1] - position[1]
							)
							
							Launcher.DRAGGING_CARD.set_selected(True)
				elif event.type == pygame.FINGERUP:
					if Launcher.DRAGGING_CARD:
						mouse_position = (event.x * 720, event.y * 1280)
						
						if spawn_rect.collidepoint(mouse_position):
							units = Launcher.PLAYER.try_to_summon(
								Launcher.DRAGGING_INDEX,
								mouse_position
							)
							
							if units:
								for unit in units:
									all_units.append(unit)
									player_units.append(unit)
						
						Launcher.DRAGGING_CARD.set_selected(False)
						Launcher.DRAGGING_CARD = None
						Launcher.DRAGGING_INDEX = -1
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						mouse_position = pygame.mouse.get_pos()
						
						hand_positions = Launcher.PLAYER.get_hand_positions(720)
						
						for index, position in enumerate(hand_positions):
							card_rect = pygame.Rect(position[0], position[1], 120, 160)
							
							if card_rect.collidepoint(mouse_position) and index < len(Launcher.PLAYER.get_player_hand()):
								card = Launcher.PLAYER.get_player_hand()[index]
								
								Launcher.DRAGGING_CARD = card
								Launcher.DRAGGING_INDEX = index
								Launcher.CARD_OFFSET = (
									int(mouse_position[0] - position[0]),
									int(mouse_position[1] - position[1])
								)
								
								if not Launcher.DRAGGING_CARD.is_selected():
									Launcher.DRAGGING_CARD.set_selected(True)
				elif event.type == pygame.MOUSEBUTTONUP:
					if event.button == 1 and Launcher.DRAGGING_CARD:
						mouse_position = pygame.mouse.get_pos()
						
						if spawn_rect.collidepoint(mouse_position):
							units = Launcher.PLAYER.try_to_summon(
								Launcher.DRAGGING_INDEX,
								mouse_position
							)
							
							if units:
								for unit in units:
									all_units.append(unit)
									player_units.append(unit)
						
						Launcher.DRAGGING_CARD.set_selected(False)
						Launcher.DRAGGING_CARD = None
						Launcher.DRAGGING_INDEX = -1
			
			Launcher.PLAYER.update(delta_time)
			screen.fill("white")
			
			screen.blit(PreRenderedUI.SPAWN_AREA_BG, (0, 500))
			
			for enemy in all_enemies:
				screen.blit(enemy.get_image_surface(), enemy.get_position())
				enemy.update(delta_time, player_units)
			
			for unit in all_units:
				screen.blit(unit.get_image_surface(), unit.get_position())
				unit.update(delta_time, all_enemies)
			
			total_elixir_progress = Launcher.PLAYER.get_elixir() / 10
			bar = 494 * total_elixir_progress
			
			# pygame.draw.rect(screen, (75, 75, 85), (elixir_bar_x - 56, elixir_bar_y, 560, 56))
			# pygame.draw.rect(screen, (128, 128, 128), (elixir_bar_x + 4, elixir_bar_y + 6, 494, 44))
			
			screen.blit(PreRenderedUI.ELIXIR_BAR_BG, (elixir_bar_x - 56, elixir_bar_y))
			screen.blit(PreRenderedUI.ELIXIR_BAR_TRACK, (elixir_bar_x + 4, elixir_bar_y + 6))
			
			elixir_text = Launcher.ELIXIR_TEXT_FONT.render(str(int(Launcher.PLAYER.get_elixir())), True, (0, 0, 0))
			
			hand_positions = Launcher.PLAYER.get_hand_positions(720)
			new_bar_color = (0, 0, 0)
			
			Launcher.NEXT_ELIXIR_INT = int(Launcher.PLAYER.get_elixir())
			
			if Launcher.NEXT_ELIXIR_INT > Launcher.LAST_ELIXIR_INT:
				Launcher.GLOW_TIMER = 0.1
			
			Launcher.LAST_ELIXIR_INT = Launcher.NEXT_ELIXIR_INT
			
			if Launcher.GLOW_TIMER > 0:
				new_bar_color = (255, 255, 200)
				Launcher.GLOW_TIMER -= delta_time
			else:
				new_bar_color = (255, 255, 32)
			
			bar_surface = pygame.draw.rect(screen, new_bar_color, (elixir_bar_x + 4, elixir_bar_y + 6, bar, 44))
			box_surface = pygame.draw.rect(screen, new_bar_color, (elixir_bar_x - 50, elixir_bar_y + 6, 46, 44))
			
			for index in range(9):
				screen.blit(PreRenderedUI.ELIXIR_BAR_MARKERS[index], (elixir_bar_x + 48 + (50 * index), elixir_bar_y, 6, 56))
			
			screen.blit(elixir_text, (elixir_bar_x - 32, elixir_bar_y + 20))
			
			for index, card in enumerate(Launcher.PLAYER.get_player_hand()):
				if index < len(hand_positions):
					if card != Launcher.DRAGGING_CARD:
						rs_position = (hand_positions[index][0] - 4, hand_positions[index][1] - 4)
						
						screen.blit(card.get_rarity_surface(), rs_position)
						screen.blit(card.get_image_surface(), hand_positions[index])
						screen.blit(card.get_overlay_surface(), hand_positions[index])
						
						screen.blit(PreRenderedUI.CARD_COST_BG, (hand_positions[index][0] + 5, hand_positions[index][1] + 5))
						
						cost_text = Launcher.COST_TEXT_FONT.render(str(card.get_deploy_cost()), True, (0, 0, 0))
						
						screen.blit(cost_text, (hand_positions[index][0] + 15, hand_positions[index][1] + 10))
					
			if Launcher.DRAGGING_CARD:
				mouse_pos = pygame.mouse.get_pos()
				
				screen.blit(
					Launcher.DRAGGING_CARD.get_image_surface(),
					(mouse_pos[0] - Launcher.CARD_OFFSET[0], 
					mouse_pos[1] - Launcher.CARD_OFFSET[1])
				)
			
			pygame.display.flip()
			
		pygame.quit()

def log(message):
	log_path = "sdcard/mcards_log.txt"
	
	with open(log_path, "a") as f:
		f.write(msg + "\n")

if __name__ == "__main__":
	Launcher.launch_mcards()
