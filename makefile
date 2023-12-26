LIBRARY=-lsfml-graphics -lsfml-window -lsfml-system

start:
    @echo "building the game... please, wait"
    g++ -c ./source/main.cpp -o multiverse-shit.o
    ./multiverse-shit.o
    @echo "compile game successfully"
    @echo "copyright 2023 MegaGamer69"