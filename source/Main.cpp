/**
 * code by MegaGamer69(me)
 * credits to Supercell :)
**/

// include the SFML basics
#include "../SFML/Window.hpp"
#include "../SFML/System.hpp"

// include the own lib(MCards)
#include "../MCards/Cards.hpp"

// include the STD lib
#include <string>
#include <iostream>

class Game {
public:
    Game() : Window(sf::VideoMode(720, 1280), "MultiverseCards") {
    	// nothing to see here :/
    }
    
    void Run() {
        while(Window.isOpen()) {
            sf::Event EventListener;
            while(Window.pollEvent(EventListener)) {
                if(EventListener.type == sf::Event::Closed) {
                    Window.close();
                }
            }
            
            Window.display();
        }
    }
    
private:
    sf::RenderWindow Window;
};

int main() {
    Game MainGame;
    MainGame.Run();
    
    return 0;
}