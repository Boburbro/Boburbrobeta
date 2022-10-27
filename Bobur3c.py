import os, sys

def userbot(a):
	instal = 'git clone https://gitlab.com/friendly-telegram/friendly-telegram'
	install = 'bash https://gitlab.com/friendly-telegram/friendly-telegram/-/raw/master/install.sh --no-web'
	os.system(instal)
	os.system(install)
	
	umoda = '(. <($(which curl>/dev/null&&echo curl -Ls||echo wget -qO-) https://gitlab.com/friendly-telegram/friendly-telegram/-/raw/master/install.sh) --no-web)'