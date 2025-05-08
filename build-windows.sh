if [ -e "./distr/mcards.exe" ]; then
	echo "Limpando o diretório de buildagem"
	
	rm -rf "./distr/mcards.exe"
fi

echo "Buildando para Windows"

gcc ./source/c/mcards.c -o distr/mcards.exe -I./include -lcsfml-graphics -lcsfml-window -lcsfml-system -O2
