if [ -e "./distr/bin/mcards.exe" ]; then
	echo "Limpando o diretório de buildagem"
	
	rm -rf "./distr/bin/mcards.exe"
fi

echo "Buildando para Windows"

gcc ./source/c/main.c -o "./distr/bin/mcards.exe" -I./include -lcsfml-graphics -lcsfml-window -lcsfml-system -lzip -O2
