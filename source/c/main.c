// Pensa comigo: o compilador basicamente já tem esses cabeçalhos, POR QUE PRECISO INCLUIR-LAS MANUALMENTE?! (ironia)

#include <stddef.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <assert.h>
#include <time.h>

// Inclusas diretamente em "<Raíz do projeto>/include/<blah blah blah...>/<cabeçalho>.h"

#include <MCards/graphics.h>
#include <MCards/mcards.h>
#include <SFML/Window.h>
#include <SFML/Graphics.h>
#include <SFML/System.h>

// O estado de alocação das unidades (tropas, feitiços, construções... HERÓ- brincadeira!)

typedef enum {
    DRAG_STATE_IDLE,
    DRAG_STATE_HOLDING,
    DRAG_STATE_DRAGGING
} mc_DragState;

static bool mc_IsDraggingCard = false;
static int mc_SelectedCardIndex = -1;

static sfVector2f mc_CardStartPosition;

static sfVector2i mc_MousePosition;

static sfVector2f mc_MouseGrabOffset;
static mc_DragState mc_CardDragState = DRAG_STATE_IDLE;

static mc_PlayerDeck mc_ClientDeck;

// Manipule a cacetada que vou dar na sua cabeça se falar que "Heróis são cartas"
// Digo... a entrada de usuário...

void mc_HandleInput(sfEvent windowEvent) {
	// Como dizia o interruptor: "eu alterno entre 0 e 1"
	
	switch(windowEvent.type) {
		case sfEvtClosed:
			sfRenderWindow_close(mc_GameWindow);
			
			break;
		case sfEvtMouseButtonPressed:
			if(windowEvent.mouseButton.button == sfMouseLeft) {
				mc_MousePosition = sfMouse_getPositionRenderWindow(mc_GameWindow);
				
				for(int i = 0; i < CARDS_TO_RENDER; i++) {
					sfFloatRect cardBounds = {
						75.0f + (i * 140),
						DECK_POS_Y,
						CARD_WIDTH,
						CARD_HEIGHT
					};
					
					if(sfFloatRect_contains(&cardBounds, mc_MousePosition.x, mc_MousePosition.y)) {
						mc_CardDragState = DRAG_STATE_HOLDING;
						
						mc_IsDraggingCard = true;
						mc_SelectedCardIndex = i;
						
						mc_MouseGrabOffset = (sfVector2f){
							mc_MousePosition.x - cardBounds.left,
							mc_MousePosition.y - cardBounds.top
						};
						
						break;
					}
				}
				
				break;
			}
			
			break;
		case sfEvtMouseMoved:
			if(mc_CardDragState == DRAG_STATE_HOLDING) {
				sfVector2i currentMousePosition = sfMouse_getPositionRenderWindow(mc_GameWindow);
				
				sfVector2i delta = {
					abs(mc_MousePosition.x - currentMousePosition.x),
					abs(mc_MousePosition.y - currentMousePosition.y)
				};
				
				if(delta.x > 5 || delta.y > 5) {
					mc_CardDragState = DRAG_STATE_DRAGGING;
				}
				
				break;
			}
			
			break;
		case sfEvtMouseButtonReleased:
			if(windowEvent.mouseButton.button == sfMouseLeft) {
				if(mc_CardDragState == DRAG_STATE_DRAGGING) {
					printf("Carta posicionada!\n");
				}
				
				mc_SelectedCardIndex = -1;
			}
			
			break;
	}
}

void mc_LoopUpdate(sfRenderWindow* window) {
	mc_DrawClientDeck(window, &mc_ClientDeck);
}

// Aqui, iremos fazer de tudo para prestar

int main() {
	mc_OpenZIPFile("./assets.zip");
	
	srand((unsigned int)(time(NULL)));
	
	mc_Hero mc_HeroList[] = {
		mc_CreateHero("Pirate",        "pirate",      1900, 32, 5.5f, 1.4f),
		mc_CreateHero("Mighty Indian", "mighty",      1960, 20, 3.5f, 0.7f),
		
		mc_CreateHero("Elite Shugun",  "shugun",      2000, 30, 4.0f, 1.8f),
		
		mc_CreateHero("Chemist",       "chemical",    1890, 26, 7.0f, 1.0f),
		
		mc_CreateHero("Livestocker",   "livestocker", 1780, 28, 5.5f, 1.1f),
		mc_CreateHero("Hunter",        "hunter",      1920, 23, 6.5f, 1.6f),
	};
	
	mc_Troop mc_TroopList[] = {
		mc_CreateTroop(400,  66,  ONLY_GROUND,           1.0f,  1.2f, 2.0f),
		mc_CreateTroop(160,  40,  GROUND_AND_AIR,        4.0f,  1.0f, 2.0f),
		mc_CreateTroop(777,  78,  ONLY_HERO_OR_BUILDING, 0.1f,  2.4f, 1.2f),
		mc_CreateTroop(282,  60,  GROUND_AND_AIR,        5.5f,  1.1f, 2.0f),
		mc_CreateTroop(444,  98,  ONLY_GROUND,           0.5f,  1.6f, 2.5f),
		mc_CreateTroop(360,  45,  ONLY_HERO_OR_BUILDING, 0.5f,  0.9f, 3.0f),
		mc_CreateTroop(192,  55,  GROUND_AND_AIR,        1.2f,  1.1f, 1.5f),
		
		mc_CreateTroop(893,  122, ONLY_GROUND,           1.0f,  1.9f, 1.0f),
		mc_CreateTroop(390,  77,  ONLY_GROUND,           1.0f,  1.4f, 2.0f),
		
		mc_CreateTroop(400,  53,  ONLY_GROUND,           1.0f,  1.1f, 2.5f),
		mc_CreateTroop(290,  59,  GROUND_AND_AIR,        4.0f,  1.3f, 2.0f),
		mc_CreateTroop(16,   12,  GROUND_AND_AIR,        0.5f,  1.5f, 1.5f),
		mc_CreateTroop(860,  84,  ONLY_GROUND,           1.5f,  1.5f, 2.0f),
		
		mc_CreateTroop(397,  70,  GROUND_AND_AIR,        1.5f,  1.3f, 1.5f),
		mc_CreateTroop(950,  98,  ONLY_HERO_OR_BUILDING, 0.5f,  2.0f, 1.2f),
		mc_CreateTroop(300,  72,  GROUND_AND_AIR,        10.0f, 1.5f, 2.0f),
		
		mc_CreateTroop(566,  77,  GROUND_AND_AIR,        1.5f,  1.5f, 2.0f),
		mc_CreateTroop(487,  67,  ONLY_GROUND,           1.5f,  1.3f, 2.0f),
		
		mc_CreateTroop(1100, 87,  ONLY_GROUND,           1.0f,  1.8f, 1.0f),
	};
	
	mc_Build mc_BuildList[] = {
		mc_CreateBuild(80,  166, GROUND_AND_AIR, 1.0f, 1.0f),
		
		mc_CreateBuild(520, 80,  ONLY_GROUND,    5.0f, 1.0f),
		mc_CreateBuild(420, 20,  GROUND_AND_AIR, 9.0f, 0.4f),
		mc_CreateBuild(598, 0,   ONLY_GROUND,    0.0f, 0.0f),
	};
	
	mc_Spell mc_SpellList[] = {
		mc_CreateSpell(200, GROUND_AND_AIR, 3.0f, 1.0f, 3.0f),
		mc_CreateSpell(100, ONLY_GROUND,    1.5f, 0.1f, 5.0f),
		
		mc_CreateSpell(53,  GROUND_AND_AIR, 4.0f, 0.1f, 8.0f),
		mc_CreateSpell(106, ONLY_GROUND,    3.0f, 1.0f, 3.0f),
		
		mc_CreateSpell(100, GROUND_AND_AIR, 2.5f, 1.0f, 1.0f),
		
		mc_CreateSpell(120, GROUND_AND_AIR, 2.0f, 0.5f, 2.0f),
	};
	
	mc_Card mc_CardList[] = {
	    mc_CreateCardTroop("Gravedigger",      "gravedigger", 1, PIRATE_EPOCH,       3, mc_TroopList[0] ),
	    mc_CreateCardTroop("Indians",          "indians",     1, PIRATE_EPOCH,       2, mc_TroopList[1] ),
	    mc_CreateCardTroop("Pelican",          "pelican",     1, PIRATE_EPOCH,       5, mc_TroopList[2] ),
	    mc_CreateCardBuild("Bomb",             "bomb",        1, PIRATE_EPOCH,       2, mc_BuildList[0] ),
	    mc_CreateCardTroop("Bandit",           "bandit",      1, PIRATE_EPOCH,       4, mc_TroopList[3] ),
	    mc_CreateCardTroop("L-Robot",          "lrobot",      1, PIRATE_EPOCH,       5, mc_TroopList[4] ),
	    mc_CreateCardSpell("Storms",           "storms",      1, PIRATE_EPOCH,       4, mc_SpellList[0] ),
	    mc_CreateCardSpell("Tsunami",          "tsunami",     1, PIRATE_EPOCH,       6, mc_SpellList[1] ),
	    mc_CreateCardTroop("Capybaras",        "capy",        1, PIRATE_EPOCH,       5, mc_TroopList[5] ),
	    mc_CreateCardTroop("Rope-Bombers",     "bombers",     1, PIRATE_EPOCH,       3, mc_TroopList[6] ),
	    
	    mc_CreateCardTroop("Crusher",          "crusher",     1, FEUDAL_JAPAN,       7, mc_TroopList[7] ),
	    mc_CreateCardTroop("Samurai Hunter",   "shunter",     1, FEUDAL_JAPAN,       4, mc_TroopList[8] ),
	    
	    mc_CreateCardTroop("Plague Assasin",   "plaguek",     1, DARK_PLAGUE_ERA,    4, mc_TroopList[9] ),
	    mc_CreateCardTroop("Ghost Musketeer",  "ghost",       1, DARK_PLAGUE_ERA,    3, mc_TroopList[10]),
	    mc_CreateCardTroop("Mosquitoes",       "bugs",        1, DARK_PLAGUE_ERA,    2, mc_TroopList[11]),
	    mc_CreateCardSpell("Scary Fog",        "fog",         1, DARK_PLAGUE_ERA,    4, mc_SpellList[2] ),
	    mc_CreateCardTroop("Reaper",           "reaper",      1, DARK_PLAGUE_ERA,    6, mc_TroopList[12]),
	    mc_CreateCardSpell("Sledgehammer",     "sledge",      1, DARK_PLAGUE_ERA,    5, mc_SpellList[3] ),
	    
	    mc_CreateCardBuild("Cannon",           "cannon",      1, TROUBLES_IN_FRANCE, 3, mc_BuildList[1] ),
	    
	    mc_CreateCardTroop("Nun",              "nun",         1, POST_TYRANNY_WORLD, 4, mc_TroopList[13]),
	    mc_CreateCardTroop("H-Robot",          "hrobot",      1, POST_TYRANNY_WORLD, 8, mc_TroopList[14]),
	    mc_CreateCardBuild("Turret",           "turret",      1, POST_TYRANNY_WORLD, 4, mc_BuildList[2] ),
	    mc_CreateCardBuild("German Bunker",    "german",      1, POST_TYRANNY_WORLD, 6, mc_BuildList[3] ),
	    mc_CreateCardTroop("Sniper",           "sniper",      1, POST_TYRANNY_WORLD, 4, mc_TroopList[15]),
	    
	    mc_CreateCardTroop("Gaucho",           "gauch",       1, GAUCHO_HISTORY,     5, mc_TroopList[16]),
	    mc_CreateCardTroop("Warrior",          "warrior",     1, GAUCHO_HISTORY,     4, mc_TroopList[17]),
	    
	    mc_CreateCardTroop("Giant Theropod",   "theropod",    1, DINOSAURS_EPOCH,    8, mc_TroopList[18]),
	    mc_CreateCardSpell("Vulcano Eruption", "eruption",    1, DINOSAURS_EPOCH,    5, mc_SpellList[4] ),
	};
	
	mc_Card mc_InitialCards[8] = {
		mc_CardList[0],
		mc_CardList[1],
		mc_CardList[2],
		mc_CardList[3],
		mc_CardList[4],
		mc_CardList[5],
		mc_CardList[6],
		mc_CardList[7],
	};
	
	mc_ClientDeck = mc_CreatePlayerDeck(mc_HeroList[0], mc_InitialCards, 8);
	
	mc_ShufflePlayerDeck(&mc_ClientDeck);
	
	sfVideoMode videoMode = {720, 1280, 32};
	
	mc_GameWindow = sfRenderWindow_create(videoMode, "Multiverse Cards", sfResize | sfClose, NULL);
	
	if(!mc_GameWindow) {
		printf("A janela do jogo não inicializou, contate ao desenvolvedor para tirar suas dúvidas.\n");
		
		return 1;
	}
	
	while(sfRenderWindow_isOpen(mc_GameWindow)) {
		sfEvent event;
		
		while(sfRenderWindow_pollEvent(mc_GameWindow, &event)) {
			mc_HandleInput(event);
		}
		
		sfRenderWindow_clear(mc_GameWindow, sfWhite);
		
		// Aqui vai atualizar a porra toda! EBA!!!!
		
		mc_LoopUpdate(mc_GameWindow);
		
		sfRenderWindow_display(mc_GameWindow);
	}
	
	sfRenderWindow_destroy(mc_GameWindow);
	
	mc_CloseZIPFile();
	
	return 0;
}
