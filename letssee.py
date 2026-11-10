import time
import sys
import random
import json

#kopiuj stąd:
#stan_gry['day'] = 5

# 2. Zmiana wartości wewnątrz "achievements"
#stan_gry['achievements']['lose job'] = True

# 3. Zwiększenie licznika "count null" o 1 (inkrementacja)
#stan_gry['achievements']['count null'] += 1


#zabezpieczam:
if sys.argv[1] != "123":
    try:
        ahaja = hashuje_potem
    except:
        sys.exit()
     
else:
    pass


def aha(a):
    for i in a:
        if i not in (",", "."):
            print(i, end="", flush=True)
            time.sleep(0.1)
        else:
            time.sleep(0.4)
            print(i, end="", flush=True)
            time.sleep(0.1)
    print()
    time.sleep(2)


class Aleksander:
    def __init__(self):
        with open('gra.json', 'r', encoding='utf-8') as plik:
            self.stan_gry = json.load(plik)
            self.day = self.stan_gry['day']
            self.rep = int(self.stan_gry['rep'])
            self.virus = self.stan_gry['virus']
        aha("witaj!")
        aha("podoba ci sie?")
        aha("ja kocham ten efekt, wolniejszego pisania!")
        self.cos()
        
    def praca(self):
        if self.day == 1:
            aha("jako Aleksander, oczywście od it, musisz robić it rzeczy, nie będzie łatwo, ostrzegam")
            aha("każdego dnia stanie sie zdarzenie, i musisz to naprawić")
            aha("powodzenia!")
            
        else:
            self.day = self.stan_gry['day']
            self.rep = int(self.stan_gry['rep'])
            pass
        zdarzenia= ["nie ma internetu","serwer sie rozwalił","jebany null","zepsuty komp","virus"]
        self.wylosowane= "virus"#random.choice(zdarzenia)
        aha(f"dzisiaj stało sie: {self.wylosowane}")
        if self.wylosowane == "nie ma internetu":
            self.internet()
        elif self.wylosowane == "serwer sie rozwalił":
            self.server()
        elif self.wylosowane == "jebany null":
            self.null()
        elif self.wylosowane == "zepsuty komp":
            self.komp()
        elif self.wylosowane == "virus":
            self.viruss()
        #tu też
    def viruss(self):
        
        while True:
            aha("więc, musisz zobaczyć, co zostało zainfekowane, robisz to?")
            virus=input(" ")
            if virus.lower() not in ["tak","nie"]:
                aha("nie ma takiej odpowiedzi!")
                continue
            elif virus.lower()== "tak":
                zainfekowane=["serwer","wszytko","komp","komps"]
                zainf = random.choice(zainfekowane)
                aha(f"zainfekowane jest {zainf}")
                lista = ["1","2","3","4","5"]
                poz = random.choice(lista)
                aha(f"poziom zainfekowania to {poz}")
                self.vir(poz)
                
                
            else:
                aha("okej, czyli przesiadujesz cały czas w serwerowni, i udajesz, że nie żyjesz")
                
                self.rep -= 10
                self.virus += 10
                #dodać -10 reputacji
                #dodać +10 virus work
                break
            
    def vir(self,poz):
        if poz == "1":
            aha(f"ten wirus jest tak żałosny, że wystarczy odpalić {zainf} jeszcze raz, bo siedzi tylko w ram")
        elif poz < 4:
            aha(f"poziom wirusa, jest na tyle mocny, że trzeba zrobić twardy reset {zainf}")
        else:
            aha("poziom wirusa jest tak duży, że jedyne co można zrobić to poszukać luki w jego zabezpieczeniach, bo ma uprawnienia root, i on może wszystko...")
           
    
    def komp(self):
        aha("komp")
    def null(self):
        aha("null")
    def server(self):
        aha("serwer sie rozwalił")
    def internet(self):
        aha("nie ma internetu")
    def cos(self):
        while True:
            self.day += 1
            self.stan_gry['day'] = self.day
            self.stan_gry['rep'] = self.rep
            self.stan_gry['virus'] = self.virus
            aha(f"to jest dzień {self.day}, bycia aleksandrem!")
            with open('gra.json', 'w', encoding='utf-8') as plik:
                json.dump(self.stan_gry, plik, indent=4, ensure_ascii=False)
            

            self.praca()
            


if __name__ == "__main__":
    gracz = Aleksander()#czyli po polsku wywoła init
else:
    sys.exit()
