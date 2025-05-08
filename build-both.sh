

echo "Build to Windows"
gcc ./source/c/mcards.c -o distr/mcards.exe -I./include -lcsfml-graphics -lcsfml-window -lcsfml-system -O2
