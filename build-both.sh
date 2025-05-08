echo "Build to Linux"
gcc ./source/c/mcards.c -o distr/mcards -I./include -lcsfml-graphics -lcsfml-window -lcsfml-system -O2

echo "Build to Windows"
x86_64-w64-mingw32-gcc ./source/c/mcards.c -o distr/mcards.exe -I./include -lcsfml-graphics -lcsfml-window -lcsfml-system -O2
