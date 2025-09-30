from mcards.engine import Engine

import mcards.gvars

if __name__ == "__main__":
	mcards.gvars.ENGINE = Engine()
	
	mcards.gvars.ENGINE.initialize(True)
