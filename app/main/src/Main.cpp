/**
 * code by: MegaGamer69(Me)
 * design by: Gerlianius(My Friend)
 * this project is open source
**/

// Include the SFML window
#include "app/main/src/include/SFML/Window.hpp"

// Include the MCards headers
// MCards is the game header
#include "app/main/src/include/MCards/Cards.hpp"

// Main class
class Main {
public:
    Main() : Wind(sf::VideoMode(720, 1280), "Multiverse Cards") {}
    
    // Loop method
    void Loop() {
        while(Wind.isOpen()) {
            sf::Event EventListener;
            
            while(Wind.pollEvent(EventListener)) {
                if(EventListener.type == sf::Event::Close) {
                    Wind.close();
                }
            }
        }
    }
    
private:
    sf::RenderWindow Wind;
};

// Initial function
int main() {
    Main Game;
    Game.Loop();
    
    return 0;
}