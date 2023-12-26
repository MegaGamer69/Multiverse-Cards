/* all of the credits for supercell */

#ifndef GAME_INCLUDE_H
#define GAME_INCLUDE_H

/* include the SFML library */
#include "../SFML/Graphics.hpp"
#include "../SFML/Window.hpp"
#include "../SFML/System.hpp"

/* include the STD library */
#include <string>
#include <vector>
#include <iostream>

#endif

/* the most important in-game character, if your trainer has been defeated, you lose */
class Trainer {
  public:
    Trainer(const std::string Name, unsigned int HP, unsigned int DG, const std::string TX) : TrainerName(Name), TrainerHP(HP), TrainerDG(DG), TrainerTextures(TX) {
        if(!TextureAtlas.loadFromFile(TX)) {
            std::cout << "Exit Code -0x01" << std::endl;
        }
    }
  private:
    const std::string TrainerName;
    unsigned int TrainerHP;
    const unsigned int TrainerDG;
    const std::string TrainerTextures;
    sf::Texture TextureAtlas;
};

class AllyTrainer : public Trainer {
  public:
    using Trainer::Trainer;
};

class EnemyTrainer : public Trainer {
  public:
    using Trainer::Trainer;
};

/* the main core of the game */
int main() {
    sf::RenderWindow WindowGame(sf::VideoMode(720, 1280), "Multiverse Cards");
    
    while(WindowGame.isOpen()) {
        sf::Event EListener;
        
        while(WindowGame.pollEvent(EListener)) {
            if(EListener.type == sf::Event::Closed) {
                WindowGame.close();
            }
        }
        
        WindowGame.display();
    }
    
    return 0;
}