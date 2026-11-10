import platform
import time
import sys
import subprocess
import hashlib
import random

hashuje_potem = True

def qwhat():
    system = platform.system()
    
    if system == 'Darwin': 
        print("HAHA! NA IPHONE TEGO NIE ODPALISZ!")
        sys.exit()
    else:
        print("MASZ NORMALNY TELEFON!")
        time.sleep(2)
        print("TO MOŻNA ZACZYNAĆ!")
        with open("/sdcard/_TERMUKSIĄTKO/FUCK_GEMINI.py", "r") as f:
        	pirgemini = f.read()
        	exec(f"hashuje_potem = {hashuje_potem}\n" + pirgemini, globals())

qwhat()