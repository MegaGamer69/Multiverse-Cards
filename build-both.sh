# Cria o direrório padrão (se é que ele pode ser criado)

if [[ ! -e "./distr" ]]; then
	mkdir "./distr"
	mkdir "./distr/bin"
fi

./build-linux.sh
./build-windows.sh
