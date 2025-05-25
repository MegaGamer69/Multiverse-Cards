#ifndef MCARDS_GRAPHICS_HEADER
#define MCARDS_GRAPHICS_HEADER

#include <stdio.h>
#include <string.h>
#include <SFML/Graphics.h>
#include <MCards/mcards.h>
#include <zip.h>

#define MAX_CARD_TEXTURES  26

#define CARD_WIDTH         90 // Tamanho de largura da carta
#define CARD_HEIGHT       121 // Tamango de altura da carta
#define DECK_POS_Y        500 // Posição de início do alinhamento vertical... OH YEAH
#define PLAY_AREA_MAX_Y   640 // O máximo que você pode posicionar sua carta!

static sfTexture* g_CardTextures[MAX_CARD_TEXTURES];
static char g_TexturePaths[MAX_CARD_TEXTURES][256];
static size_t g_CardTextureCount = 0;

static zip_t* g_GlobalZIPFile = NULL;

static inline void mc_OpenZIPFile(const char* zipPath) {
	int error = 0;
	
	g_GlobalZIPFile = zip_open(zipPath, ZIP_RDONLY, &error);
	
	if(!g_GlobalZIPFile) {
		fprintf(stderr, "ALERTA: a porra do arquivo zip solicitado TALVEZ não seja válida, recomendo confirmar e beba água. (código de erro: %d\n)", error);
	}
}

static inline void mc_CloseZIPFile() {
	if(g_GlobalZIPFile) zip_close(g_GlobalZIPFile);
	
	g_GlobalZIPFile = NULL;
}

static inline const char* mc_GetZIPCardPath(const char* classID) {
	static char buffer[512];
	
	snprintf(buffer, sizeof(buffer), "assets/cards/%s.png", classID);
	
	return buffer;
}

static inline sfTexture* mc_GetTextureFromZIPFile(const char* fileName) {
	zip_int64_t index = zip_name_locate(g_GlobalZIPFile, fileName, 0);
	
	if(index < 0) {
		fprintf(stderr, "ALERTA: não há evidência do arquivo %s, desculpe pelo imprevisto (o índice é menor que zero).\n", fileName);
		
		return NULL;
	}
	
	zip_file_t* file = zip_fopen_index(g_GlobalZIPFile, index, 0);
	
	if(!file) {
		fprintf(stderr, "ALERTA: não há evidência do arquivo %s, desculpe pelo imprevisto (não pôde ler esta merda, sentimos muito).\n", fileName);
		
		return NULL;
	}
	
	struct zip_stat stat;
	
	zip_stat_init(&stat);
	zip_stat_index(g_GlobalZIPFile, index, 0, &stat);
	
	void* buffer = malloc(stat.size);
	
	if(!buffer) {
		fprintf(stderr, "ALERTA VERMELHO: falha ao alocar a desgraça da RAM...\n");
		zip_fclose(file);
		
		return NULL;
	}
	
	zip_fread(file, buffer, stat.size);
	
	sfTexture* texture = sfTexture_createFromMemory(buffer, stat.size, NULL);
	
	free(buffer);
	zip_fclose(file);
	
	return texture;
}

static inline void mc_DrawCard(sfRenderWindow* window, mc_Card* card, sfVector2f pos) {
	sfTexture* texture = NULL;
	
	const char* classID = NULL;
	
	classID = card->i_ClassID;
	
	if(classID) {
		texture = mc_GetTextureFromZIPFile(mc_GetZIPCardPath(classID));
	}
	
	sfRectangleShape* cardShape = sfRectangleShape_create();
	
	sfRectangleShape_setSize(cardShape, (sfVector2f){CARD_WIDTH, CARD_HEIGHT});
	sfRectangleShape_setPosition(cardShape, pos);
	
	if(texture) {
		sfRectangleShape_setTexture(cardShape, texture, sfTrue);
	} else {
		sfRectangleShape_setFillColor(cardShape, sfColor_fromRGB(255, 0, 0));
	}
	
	sfRenderWindow_drawRectangleShape(window, cardShape, NULL);
    sfRectangleShape_destroy(cardShape);
}

static inline void mc_DrawClientDeck(sfRenderWindow* window, mc_PlayerDeck* deck) {
	for(size_t i = 0; i < 4; i++) {
		sfVector2f pos = {65 + (i * 100), DECK_POS_Y};
		
		mc_DrawCard(window, &deck->d_DeckCards[i], pos);
	}
}

#endif
