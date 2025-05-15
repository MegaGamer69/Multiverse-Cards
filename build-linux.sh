if [ -e "./distr/bin/mcards" ]; then
	echo "Limpando o diretório de buildagem"
	
	rm -rf "./distr/bin/mcards"
fi

echo "Buildando para Linux"

gcc ./source/c/main.c -o "./distr/bin/mcards" -I./include -lcsfml-graphics -lcsfml-window -lcsfml-system -O2
