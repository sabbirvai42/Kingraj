import os, platform, time, sys
import requests
import time
import os
from sys import stderr

def jala(z):
	for e in z + '\n':
		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)

try:
	import requests
except ImportError:
	jala('\033[1;91m[\033[1;97m+\033[1;91m] \033[1;96minstall requests')
	os.system("pip install requests")

logo = ("""
  \033[1;91m   _____ __  _____    ____  __  _______   __
  \033[1;91s
  \033[38;5;208m  \__ \/ /_/ / /| | / / / / /_/ // //  |/ / 
  \033[38;5;208m ___/ / __  / ___ |/ /_/ / __  // // /|  /  
  \033[1;95m/____/_/ /_/_/  |_/_____/_/ /_/___/_/ |_/ 
\033[1;96m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def menu():
	if os.path.exists("fi_.txt"):
		with open("fi_.txt", "r") as file:
			saved_pas = file.read().strip()
			if saved_pas == "NOT DELETE THIS FILE":
				start_system()
	else:
		show_menu()



def watch_video():
    os.system("xdg-open https://fb.watch/kC4uRFCBog/?mibextid=NnVzG8")
    time.sleep(2.4)
    show_menu()

def show_menu():
	os.system("clear")
	print(logo)
	print("\033[1;37m [1] \033[1;32m FB id dump menu")
	print("\033[1;37m [2] \033[1;33m Watch a id dump video")
	print("\033[1;37m [3] \033[1;31m Exit")
	print("\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	umit =input("\033[1;37m [?] Choose :\033[1;32m ")
	if umit in ["1", "01"]:
		with open("fi_.txt", "w") as file:
			file.write("NOT DELETE THIS FILE")
		start_system()
	if umit in ["2","02"]:
		watch_video()
	if umit in ["3","03"]:
		exit("Exiting the system. Goodbye!")
	if umit in ["4", "04"]:
		os.system("cd _FILEs_ && python FILE21.py")
	else:
		with open("fi_.txt", "w") as file:
			file.write("NOT DELETE THIS FILE")
		start_system()


def start_system():
    print('\033[1;91m[\033[1;97m-\033[1;91m] \033[1;97mChecking For Update...')
    os.system('git pull --quiet 2>/dev/null')
    bit = platform.architecture()[0]
    if bit == '64bit':
    	print('\033[1;91m[\033[1;97m✓\033[1;91m] \033[1;97m64Bit Found')
    	import FILE64
    elif bit == '32bit':
    	print('\033[1;91m[\033[1;97m✓\033[1;91m] \033[1;97m32Bit Found')
    	import FILE32
    	
menu()
    
