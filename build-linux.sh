if [ -e "./distr/mcards" ]; then
	echo "Limpando o diretório de buildagem"
	
	rm -rf "./distr/mcards"
fi

echo "Buildando para Linux"

gcc ./source/c/main.c -o distr/mcards -I./include -lcsfml-graphics -lcsfml-window -lcsfml-system -O2
