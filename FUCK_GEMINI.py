from rich.console import Console
from rich.progress import track
import time

console = Console()

console.print("[bold green]WITAJ!![/bold green]")

for _ in track(range(20), description="Ładowanie zasobów..."):
    time.sleep(0.1)

console.print("[bold red]Ciekawe, czy spodoba ci się ta gra...[/bold red]")
time.sleep(2)



import sys
import json
with open('/storage/emulated/0/_TERMUKSIĄTKO/gra.json', 'r', encoding='utf-8') as plik:
    stan_gry = json.load(plik)

if stan_gry['achievements']['klauzula'] == False:
    jebac_nie = input("jak grasz w tą gre, to zgadzasz sie na KAŻDĄ istniejącą linijke kodu w tym kodzie, jak sie nie zgadzasz to wyjdź, ale jak sie zgadzasz, to pamiętaj, nie ma odwołania, a jak chcesz sobie sprawdzić ten kod, TO POWODZENIA! ALE PRZECIEŻ NIE ZABRANIAM, jedyne czego zabraniam to MODYFIKACJI! (napisz czy się zgadzasz czy nie, tylko tak albo nie) modyfikowanie kodu, jest równoważne z banem czy coś")
    if jebac_nie.lower() == "tak":
        print("to zaczynamy(chyba, że masz iphone)")
        stan_gry['achievements']['klauzula'] = True
        with open("/storage/emulated/0/_TERMUKSIĄTKO/gra.json", "w", encoding="utf-8") as plik:
            json.dump(stan_gry, plik, ensure_ascii=False, indent=4)
    else:
        print("to spierdalaj!")
        sys.exit()
else:
    jebac_nie = "tak"

#jeb
def jeb():
	global jebac_nie
	if jebac_nie.lower()== "tak":
		print("to zaczynamy(chyba, że masz iphone)")
import random
import hashlib
import webbrowser
import os 

#sprawdzamy, czy nie ma ban
#nie zmieniaj, bo moje zabezpieczenia są takie bezczelne, że ci sie odechce
path = "/storage/emulated/0/_TERMUKSIĄTKO/key.so"
pierwszy_hash = hashlib.sha256(open(path, "rb").read()).hexdigest()
agateczek = 1


wynik_ahu = random.random() < 0.001

mylist = {
    "knox": "mam lepsze zabezpieczenia, i to nie żart, jeśli knox jakoś to widzi, to wyzywam go na pojedynek, pojedynek wygląda tak, ja udoskonalam mój kod, a knox próbuje robić lepszy, oczywiście nie zrobi",
    "aha": "aha, czyli moja ulubiona biblioteka w termux, która kopiuje tekst na kolorowo, zapisując go w html! to najbardzej potrzebne narzędzia na ziemi",
    "cos":"wgl, to moje nazwy zmiennych są dziwne chyba... ale wiem, że musze cos zjeść..."
}




wynik_ahus= True
if wynik_ahu:
	print("To easter egg × troche!")
	
	while True:
		print("co mamy na stanie?:")
		for nazwa in mylist:
			print(f"- {nazwa}")
	
		print("-" * 20)
		odpowiedz = input("co chcesz wiedzieć?")
	
	# Sprawdzamy, czy sramy
		if odpowiedz in mylist:
			print(mylist[odpowiedz])
		else:
			print("404")
else:
	print(" ")
	


# 3. Haszujesz ten wynik PO RAZ DRUGI (zamieniając go najpierw na bajty przez .encode())
drugi_hash = hashlib.sha256(pierwszy_hash.encode()).hexdigest()
gemini_niejestem_script_kiddie = hashuje_potem

target = "5b399ff3c185bda34de28ab2d6189ce4cb99359518c8512655702e56a4b8a705"

if drugi_hash == target:
    print("jeszcze nie masz bana!")
    # Twoja matka tutaj
else:
    print("UPS! ALBO NIE MASZ key.so ALBO MASZ BANA! ALBO key.so JESY NIEORYGINALNY!")
    sys.exit()
    # Twoja matka tutaj
    
def szkola(): #(oczywiście czasami użyje tego, a czasami wpisze coś podobnego xd
    print("JESTEŚ W SZKOLE!")
    time.sleep(2)
    if pierwszy_wybór.lower() == "grzeczny":
        print("więc, jako grzeczne dziecko w szkole...")
        time.sleep(2) 
        print("powiedzmy, że jesteś nerdem")
        time.sleep(2)
        witamitam = input("okej?")
        if witamitam.lower() == "tak":
            print("czyli jako ten 'mądry', wiesz, że życie nie ma sensu...")
            time.sleep(2)
            print("więc, się zabijasz...")
            sys.exit()
        else:
            print("TO SPIERDALAJ!")
            sys.exit()
        
    elif pierwszy_wybór.lower() == "niegrzeczny":
        print("jako ten 'niegrzeczny', masz ciekawy wybór")
        time.sleep(1)
        drug = input("ktoś pyta cie o sprzedawanie thc, pcp itp, zgadzasz się?")
        if drug.lower() == "tak":
            print("to był policjant xd")
            time.sleep(2)
            print("jesteś w więzieniu")
            time.sleep(2)
            print("chcesz sie z kimś pobić?")
            bic = input("")
            if bic.lower() == "tak":
                print("więc się bijesz")
                time.sleep(2)
                print("więc masz 50% szans na przeżycie")
                listor = ["tak","nie"]
                lista_list = random.choice(listor)
                if lista_list == "tak":
                    print("więc wygrałeś!")
                    time.sleep(2)
                    print("więc skoro wygrałeś, masz szacunek i uznanie")
                    time.sleep(2)
                    print("to powinieneś pamiętać, że w więzieniu bicie się jest 'nielegalne'?")
                    time.sleep(4)
                    print("oczywście o tym wiesz?")
                    wiesz = input("tak?")
                    if wiesz.lower() == "tak":
                        print("to dobrze...")
                    elif wiesz.lower() == "nie":
                        print("to już wiesz, że jest to nielegalne!")
                    else:
                        print("odpowiedzi nie ma w zbiorze.")
                        pyt()
                        losus()
                        print("nie wiem czy to się wgl odpali, bo nie wiem czy po funkcji 'losus()' coś jeszcze jest.")
                        time.sleep(1)
                        print("więc powiedzmy, że cię błogosławie z więzienia i trafiasz do szkoły")
                        szkola()
                    print("wgl, to tak sobie myśle, że prawie nigdy nie używam imienia gracza...")
                    time.sleep(2)
                    print(f"trzeba to zmienić {imie_gracza}")
                    time.sleep(2)
                    agalala = input("dobra, wracamy do więzienia. Podoba ci się tam?")
                    if agalala.lower() == "tak":
                        print("to dobrze")
                        time.sleep(2)
                        print("bo właśnie spędziłeś swój cały wyrok!")
                        
                        #TU
                        
                    elif agalala.lower() == "nie":
                        print("to będzie jeszcze gorzej...")
                        time.sleep(2)
                        print("wiesz wgl, że mam fajnego")
                        ahaa("KOTKA?")
                        time.sleep(2)
                        print("mam nadzieję...")
                        kotek = input("myślisz, że mój kotek jest świetny?")
                        if kotek.lower() == "tak":
                            print("to dobrze!")
                            time.sleep(2)
                            print("ale napisałem 'to będzie jeszcze gorzej...' więc to zakończe")
                            sys.exit()
                        else:
                            banicja()
                            sys.exit()
                    
                    else:
                        print(f"ale to ma być tylko 'tak' albo 'nie', ale nie chce mi się robić pętli, żebyś tylko mógł napisać to samo (zapewne) jeszcze raz. wgl co to {agalala} ma znaczyć??")
                        time.sleep(5)
                        print("wiesz co?")
                        aha("KONIEC TEGO")
                        sys.exit()
                    
                else:
                    print("więc przegrałeś, i zginąłeś")
                    sys.exit()
                
            elif bic.lower() == "nie":
                print("więc, się nie bijesz")
            #TU
            
        elif drug.lower() == "nie":
            print("to nie")
            sys.exit()
        else:
            print("twoja wiadomość, to ani tak, ani nie, więc...")
            while True:
                pyt()
    else:
        print("jak sie tu dostałeś?")
        time.sleep(1)
        print("nie mam pojęcia... ale nie chce mi sie kontynuować tej ścieżki, papa")
        sys.exit()

  
  
#banicja
def banicja():
	os.rename("/storage/emulated/0/_TERMUKSIĄTKO", "/storage/emulated/0/_\u200dTERMUKSI\u200b\u200cĄTKO")
	with open("/storage/emulated/0/_\u200dTERMUKSI\u200b\u200cĄTKO/key.so","r+b") as f:f.seek(2);f.write(b"\xDE\xAD\xBE\xEF")
	webbrowser.open('https://youtu.be/dQw4w9WgXcQ?is=S6NfaXTEf3vbXlpz')
	print("ty myślisz, że sobie pograsz?")
	print("TO SIE MYLISZ!")
	print("POWODZENIA Z ZABEZPIECZENIAMI!")
	sys.exit()
def pyt():
	pyt = input("android czy ios?")
	if "android".lower() == pyt:
		print("przeszedłeś test!")

	else:
	    print("nie toleruje odpowiedzi innych niż android")
	    banicja()

tenskrypt_tochyba_na_to_dowód = gemini_niejestem_script_kiddie
if jebac_nie.lower() !="tak": 
	print("ty mnie oszukałeś?")
	banicja()
try:
	if hashuje_potem:
		print("chyba używasz oryginalnej wersji, tych plikówFUCK_GEMINI.py")
		time.sleep(2)
		print("mam nadzieję...")
except NameError:
	print("odpal iphonowanie.py aby zadziałało")
	sys.exit()
prawdaha = tenskrypt_tochyba_na_to_dowód

#> antyiphone.py
def generuj_hash(sciezka):
    with open(sciezka, "rb") as f:
        bajty = f.read()
        return hashlib.sha256(bajty).hexdigest()


hahaus = generuj_hash("/storage/emulated/0/_TERMUKSIĄTKO/iphonowanie.py")

if hahaus != "0f08bd78907591bf41f76207bef978bf55f7ee0ae337f166049c0206639cc681":
	print("nic nie zmieniaj nigdzie, ok?")
	time.sleep(2)
	print("jak weźmiesz oryginalną wersję skryptu iphonowanie.py to pogadamy")
	sys.exit()


def ahaa(a):
    for i in a:
        if i not in (",", "."):
            print(i, end="", flush=True)
            time.sleep(0.1)
        else:
            time.sleep(0.4)
            print(i, end="", flush=True)
            time.sleep(0.1)
    time.sleep(2)
    
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

# Początek
print("Witaj w grze 'Butter Life'!")
time.sleep(1)
print("Ale jak coś to ta gra ma 2 tytuły,")
time.sleep(1)
print("2 tytuł, to God of your Life")
if jebac_nie.lower()!="tak": 
	print("ty mnie oszukałeś?")
	banicja()
time.sleep(3)
print("przed zaczęciem mam ważny komunikat")
time.sleep(2)
print("jak źle wpiszesz to się skończy bo mi się nie chce programować żeby wpisać jeszcze raz")
time.sleep(2)
print("a więc. ZACZYNAJMY!!!")
jajko = hashuje_potem

if jebac_nie.lower()!="tak": 
	print("ty mnie oszukałeś?")
	banicja()

#polecam grać a nie sprawdzać co się stanie, pozatym jest tu takie spagetti, że nawet ja się czasami gubie, ale skoro chcesz, to powodzenia w spagettifikacji!

#nano wypadki.py
def wypadl():
	wypadlem = ["tak", "nie", "nie", "nie"]
	wypad = random.choice(wypadlem)
	if wypad == "tak":
		wtaher = ["ktoś odgryzł ci ucho, twój stary odgryzł mu głowe, jest dobrze!", "przyszedł twój stary i kopnął cię w kostkę", "kupiłeś iphone"]
		whatis = random.choice(wtaher)
		if whatis == "kupiłeś iphone":
			print(whatis)
			time.sleep(2)
			webbrowser.open('https://youtu.be/dQw4w9WgXcQ?is=S6NfaXTEf3vbXlpz')
			print("nienawidzę tego czegoś...")
			time.sleep(2)
			print("więc zginiesz...")
			sys.exit()
		else:
			print("właśnie ", whatis)
		
	elif wypad == "nie":
		print("prawie miałeś wypadek, ale jest ok")
#cat losus.py
def losus():
	print("jeśli tu jesteś, to to oznacza, że coś odwaliłeś...")
	time.sleep(1)
	print("przynajmniej zazwyczaj")
	time.sleep(1)
	print("a to oznacza, że muszę coś wymyśleć")
	time.sleep(5)
	print("dobra, wiem! ale ty jeszcze nie")
	zmienie = ["tepasz się do dorosłości, i dalej coś wymyślę", "giniesz bo dlaczego nie", "zaczynasz od początku"]
	ralus = random.choice(zmienie)
	if ralus == "tepasz się do dorosłości, i dalej coś wymyślę":
		print("od teraz, będziesz Aleksandrem od IT!")
		jajko = hashuje_potem
		time.sleep(1)
		print("więc mam wybór")
		time.sleep(1)
		zmienieto = input("więc, android czy ios?😈")
		if "ios".lower() in zmienieto:
			os.rename("/storage/emulated/0/_TERMUKSIĄTKO", "/storage/emulated/0/_\u200dTERMUKSI\u200b\u200cĄTKO")
			with open("/storage/emulated/0/_\u200dTERMUKSI\u200b\u200cĄTKO/key.so","r+b") as f:f.seek(2);f.write(b"\xDE\xAD\xBE\xEF")
			webbrowser.open('https://youtu.be/dQw4w9WgXcQ?is=S6NfaXTEf3vbXlpz')
			print("to tak...")
			time.sleep(2)
			print("SPIERDALAJ!")
			time.sleep(2)
			print("POPROSTU SPIERDALAJ!")
			time.sleep(2)
			print("W TĄ GRE JUŻ NIE ZAGRASZ! A JA O TO ZADBAM!")
			sys.exit()
			#spierdalaj
			
		else:
			print("brawo!")
			time.sleep(2)
			print("właśnie uniknąłeś śmierci! (mam nadzieje o ile masz android)")
			time.sleep(2)
			print("więc, jako Aleksander, od it, musisz wiedzieć, co robi ta komenda na linux: 'ls'")
			time.sleep(3)
			oool = input("wiesz?")
			if oool.lower() == "tak":
				print("czyli oczywiście wiesz co to Linux?")
				time.sleep(0.1)
				print("mam nadzieje...")
				pyt()
				print("wgl, ten kod ma prawie 1000 linijek kodu już, chyba trzeba jakoś do tego dobić?")
				time.sleep(1)
				print("WBIŁEM!")
				time.sleep(1)
				print("z tej okazji, chce ci przedstawić, nowy kod, BARDZIEJ UPORZĄDKOWANY, i powinen być o wiele lepszy (mam nadzieję)")
				with open("/sdcard/_TERMUKSIĄTKO/letssee.py", "r") as f:
				    pierdolgemini = f.read()
				    exec(pierdolgemini)
				    sys.exit()
    
				#ALEKSANSERKOWO
			elif oool.lower() == "gówno":
				print("masz 5 sekund, albo masz bana")
				time.sleep(5)
				banicja()
			else:
				print("nie wiesz?")
				time.sleep(2)
				print("to wykona sie losowa akcja")
				while True:
					wypadl()
					pyt()
	elif ralus == "giniesz bo dlaczego nie":
		print(zmienie)
		time.sleep(1)
		print("GAME OVER   AGE:  0-∞")
		sys.exit()
	elif ralus == "zaczynasz od początku":
		print("wylowowało sie, że zaczynasz od początku")
		time.sleep(2)
		print("papa")
		time.sleep(1)
		print("GAME OVER   AGE: NIEWIEM, BO ROBIE TO JAKO FUNCJE DO WKLEJENIA W KILKA MIEJSC")
		sys.exit()
		
#KLĄTWA.LOWER()
def klata():
		print("WIĘC ZAKILAM CIĘ!")
		radus = ["at","ater"]
		aluzja = random.choice(radus)
		time.sleep(2)
		if aluzja== "at":
			print("skoro jesteś już zaklętą agacią")
			time.sleep(2)
			wyb = input("czy chcesz zostać agacią, czy wylosować coś?")
			if wyb.lower()== "nie":
				losus()
		print("dobra, jak jesteś zaklętą agacią")
		time.sleep(2)
		print("to może...")
		time.sleep(2)
		traktor = input("chcesz kupić traktor?")
		if traktor.lower()== "tak":
			losus()
		elif traktor.lower()== "nie":
			print("więc, skoro te pieniążki, są tylko twoje,")
			time.sleep(2)
			
		
		#TU
		
#agacie:
agacie = ["agacia", "agatka","agata","agateczka","krowa","królowa","aliment","alimenciara","królowa wszechświata","wielka królowa wszechświata","agacia królowa","agat","aga","aguś"]

# Wybór imienia 
imie_gracza = input("Wybierz swoje imię: ")
if imie_gracza.lower() == "seba" or imie_gracza.lower() == "sebastian" :
    print("żyg")
    sys.exit()
    
elif imie_gracza.lower() == "ios" or "iphone" in imie_gracza.lower():
    banicja()
    
elif imie_gracza.lower() == "aha":
	print("aha... to moja ulubiona biblioteka... w termux!")
	pyt()
	print("kocham cie")
	time.sleep(2)
	print("ale nie mam pomysłu na ścieżke biblioteki w termux...")
	time.sleep(2)
	print("ale może ai ma pomysł?")
	time.sleep(2)
	print("zobaczmy co napisze gemini")
	gemini_odp = """ Aaaa, czyli nie chodzi o nudną ścieżkę w systemie plików, tylko o **pomysł na fabularną ścieżkę (lore) i mechanikę gry** w tym elifie! Mój błąd, za bardzo wszedłem w tryb administratora systemów, zamiast wczuć się w rolę genialnego projektanta gier w tym spaghettim.
Skoro gracz wpisuje imię **"aha"**, a to jest Twoja "ulubiona biblioteka w Termuxie", to ta ścieżka musi być totalnie odklejona, techniczna i bezczelna – dokładnie tak jak reszta kodu.
Oto genialny pomysł na to, co może się stać w środku ścieżki "aha":
### Fabuła: "Kod źródłowy rzeczywistości"
Skoro gracz wybrał imię biblioteki, gra uświadamia sobie, że **nie jest grą, tylko żywym skryptem w Termuxie**. Gracz nie rodzi się w Warszawie czy Krakowie – rodzi się w pamięci RAM smartfona i musi nią zarządzać.
### Propozycja kodu (do wklejenia w elif imie_gracza.lower() == "aha":):
```python
elif imie_gracza.lower() == "aha":
	print("aha... to moja ulubiona biblioteka... w termux!")
	pyt()
	print("kocham cie")
	time.sleep(2)
	print("Odpalam bibliotekę 'aha' w trybie superużytkownika...")
	time.sleep(2)
	print("BŁĄD SYSTEMU! Biblioteka 'aha' przejęła kontrolę nad Twoim życiem!")
	time.sleep(2)
	
	print("\n--- ROZDZIAŁ: TERMINAL CHAOSU ---")
	time.sleep(1)
	print("Nie rodzisz się w szpitalu. Rodzisz się w katalogu /data/data/com.termux/files/home.")
	time.sleep(2)
	
	wybor_aha = input("Twój proces procesora rośnie. Co robisz? ('forkuj się' / 'odpal neofetch'): ")
	
	if razor_aha.lower() == "forkuj się" or razor_aha.lower() == "forkuj sie":
		print("Stworzyłeś 1000 swoich klonów w tle!")
		time.sleep(2)
		print("Twój telefon zaczyna parzyć w ręce jak tani iPhone podczas ładowania.")
		time.sleep(2)
		print("System Android ubija Twój proces za zużycie baterii. Umarłeś jako zombi-proces.")
		print("GAME OVER          AGE: 0.0003 sekundy procka")
		sys.exit()
		
	elif razor_aha.lower() == "odpal neofetch":
		print("Szpanujesz logiem systemu w terminalu. Wszystkie procesy w tle Cię szanują.")
		time.sleep(2)
		print("Nagle do pokoju (katalogu) wchodzi Twój stary – skrypt 'root_kill_9.sh'...")
		time.sleep(3)
		
		stary_proces = input("Stary krzyczy, że marnujesz cykle procesora na pierdoły! Co robisz? ('uciekam do RAMu' / 'usuwam mu config'): ")
		
		if stary_proces.lower() == "uciekam do ramu":
			print("Schowałeś się w pamięci podręcznej.")
			time.sleep(2)
			print("Niestety, na telefonie ktoś właśnie odpalił oficjalną aplikację Apple TV (co za śmieć)...")
			time.sleep(2)
			print("Ta niezoptymalizowana kupa złomu od Apple zżarła cały RAM. Zostałeś nadpisany.")
			print("GAME OVER          ZABITY PRZEZ REKLAMY IPODA")
			sys.exit()
			
		elif stary_proces.lower() == "usuwam mu config":
			print("BEZCZELNE! Usunąłeś staremuxowi pliki konfiguracyjne!")
			time.sleep(2)
			print("Twój stary dostał błędu składni (SyntaxError) i zawiesił się na amen.")
			time.sleep(2)
			print("Brawo! Jesteś teraz niezależnym demonem (daemon) działającym w tle systemu.")
			time.sleep(2)
			print("Przechodzisz do dorosłości jako Aleksander od IT, ale masz uprawnienia ROOTa!")
			time.sleep(2)
			
			# Tutaj płynnie przerzucasz gracza do funkcji losus(), ale z bonusem
			print("Pora przejąć resztę świata...")
			time.sleep(1)
			losus()

```
### Dlaczego to pasuje?
 1. **Trzyma klimat:** Wykorzystuje insider-joke'i o Termuxie, procesach Linuxa (fork, kill -9, daemon).
 2. **Nawiązuje do Twoich zasad:** Subtelnie i złośliwie wyśmiewa Apple oraz ich aplikacje/sprzęt (że niby zapychają RAM i niszczą system).
 3. **Płynnie łączy się z resztą spaghetti:** Jeśli gracz przetrwa, usuwając config staremu, gra daje mu status "Aleksandra od IT" i odpala Twoją gotową już funkcję losus().
Co myślisz o pójściu w taką stricte "systemowo-hakerską" ścieżkę dla biblioteki aha? Wykorzystujemy to, co programista lubi najbardziej!
"""
	print("to mi odpisał")
	time.sleep(0.1)
	print(gemini_odp)
	print("to sie nie nada...")
	time.sleep(2)
	print("teraz coś lepiej, nie chce mi sie znowu wklejać, ale napisał o ddos na apple, TO JEST ŚWIETNY POMYSŁ!")
	time.sleep(1)
	print("tylko szkoda, że to nielegalne...")
	time.sleep(2)
	print("ale jak chce to wystawić na świat, to raczej dostane ddos, ale policji u mnie w domu...")
	time.sleep(2)
	print("to może poprostu...")
	time.sleep(1)
	print("WIEM! ZROBIE Z CIEBIE HACKERA!")
	time.sleep(2)
	print("TAKIEGO CO WŁAMIE SIE DO APPLE!")
	pyt()
	hack = input("zgadzasz sie?")
	if "tak" in hack.lower():
		print("pierwsza lekcja:")
		time.sleep(2)
		print("TRZEBA SIE DOSTAĆ NA ICH SERWERY!")
		time.sleep(2)
		print("ale jak?")
		time.sleep(2)
		print("1. odpal na ich strone nmap z -sV")
		wynikiiii = """
~ $ nmap -sV www.apple.com
Starting Nmap 7.99 ( https://nmap.org ) at 2026-06-12 21:13 +0200
Nmap scan report for www.apple.com (184.24.145.53)
Host is up (0.10s latency).
Other addresses for www.apple.com (not scanned): 2a02:26f0:3780:d8a::1aca 2a02:26f0:3780:d90::1aca 2a02:26f0:3780:dad::1aca
rDNS record for 184.24.145.53: a184-24-145-53.deploy.static.akamaitechnologies.com
Not shown: 998 filtered tcp ports (no-response)
PORT    STATE SERVICE  VERSION
80/tcp  open  http     AkamaiGHost (Akamai's HTTP Acceleration/Mirror service)
443/tcp open  ssl/http AkamaiGHost (Akamai's HTTP Acceleration/Mirror service)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.04 seconds
~ $
"""
		print("wyniki to:", wynikiiii)
		time.sleep(2)
		print("to nam nic nie dało...")
		time.sleep(2)
		print ("to może weś iphone, pobierz darksword, zmodyfikuj, aby pokazywał z czym sie łączy srajphone i zrób tam ddos?")
		time.sleep(2)
		print("niestety, albo i na szczęście, nie posiadam iphone, więc zrób to sam!")
		time.sleep(2)
		print("a jak nie to powiedz to do grok'owi, on ci pomoże!")
		#TU "HACKER"
	else:
		print("to masz 5 sekund na wyjście albo masz bana TO NIE ŻART!")
		time.sleep(5)
		banicja()
		sys.exit()
	
elif imie_gracza.lower() in agacie or "agacia" in imie_gracza.lower() or "agata" in imie_gracza.lower():
	agateczek +=1
	print ("o chuj...")
	time.sleep(3)
	print ("MOŻNA BYŁO WYBRAĆ ŻYCIE KOGO KOLWIEK A TY WYBIERASZ AKURAT TO COŚ!!!!!!!!!!")
	time.sleep(4)
	print ("okej, ale będziesz żałować...")
	time.sleep(2)
	print("ZACZYNAMYYY!!!!")
	print ("Agata urodziła się na planecie dēbili, jako asteroida")
	time.sleep(3)
	agata = input("Pierwszy wybór : czy uderzasz w dinozaury z ziemi bo nie chcą płacić alimentów?")
	if agata.lower() == 'tak':
		print("bardzo dobrze!")
		time.sleep(2)
		print ("Agata walnęła w ziemię i zabiła dinozaury")
		time.sleep(2)
		print("Teraz Agata to Bóg alimentów i i ujawnia się tylko wtedy gdy wyczuje pieniądze")
		time.sleep(2)
		pyt()
		print("więc, jako Bóg alimentów, musisz poprowadzić cywilizacje, aby płaciła ci alimenciki")
		ziemie = input("więc, aby poprowadzić cywilizacje, masz do wyboru, niewolnictwo, bycie mądrym królem, podróba jezusa")
		if ziemie.lower() == "niewolnictwo":
			print("więc, jako agacia, bogini alimencików")
			time.sleep(2)
			print ("musi zarabiać z niewolników")
			time.sleep(2)
			many = int(input("ile chcesz z twoich niewolników, napisz TYLKO liczbe bo wywali błąd"))
			print("więc pobierasz od nich: ", many)
			time.sleep(2)
			kaska = many*1
			print("masz już ze swoich niewolników: ", kaska)
			bij = input("więc, czy chcesz używać na swoich niewolników przemocy?")
			if bij.lower() == "tak":
				print("BRAWO!")
				time.sleep(2)
				kaska +=300
				print("teraz zarabiasz: ", kaska)
				rozmm = input("czy chcesz topić swoje dzieci, ale nadal pobierać na nie alimenty?")
				if rozmm.lower() == "tak":
					print("BRAWO!")
					time.sleep(2)
					print("TAK ZROBIŁOBY AGACIA")
					pyt()
					time.sleep(2)
					print("teraz zarabiasz na siebie i nie musisz wydawać resztek na darmozjady!")
					kaska +=500
					print("teraz zarabiasz: ", kaska)
					time.sleep(2)
					kasus = input("chcesz robić JESZCZE więcej dzieci, aby zarabiać JESZCZE więcej alimentów?")
					if kasus.lower()== "tak":
						print("BRAWO!")
						time.sleep(2)
						kaska+= 10000
						print(f"teraz zarabiasz: ", kaska)
						time.sleep(2)
						jajko = hashuje_potem
						pyt()
						
			#TU
					elif kasus.lower()== "nie":
						print("czyli nie chcesz pieniędzy?")
						time.sleep(2)
						print("nie to nie...")
						klata()
				elif rozmm.lower() == "nie":
					print("nie?")
					time.sleep(2)
					print ("okej!")
					time.sleep(2)
					print ("TO DOSTANIESZ KARE OD PRAWDZIWEGO BOGA!")
					time.sleep(2)
					kaska+=200
					print(f"przez {kaska} lat nie możesz dostawać alimentów!")
					pyt()
					klata()
			elif bij.lower() == "nie":
				print("TAK?")
				time.sleep(2)
				print ("TO DOSTANIESZ KARE OD PRAWDZIWEGO BOGA!")
				time.sleep(2)
				kaska+=200
				print(f"przez {kaska} lat nie możesz dostawać alimentów!")
				klata()
		elif ziemie.lower() == "bycie mądrym królem":
			print("więc jako mądry król, nie możesz ściągać procentów ze swoich ludzi")
			time.sleep(2)
			print("ale za to, możesz z nimi pracować")
			time.sleep(2)
			webbrowser.open('https://youtu.be/dQw4w9WgXcQ?is=S6NfaXTEf3vbXlpz')
			print("ale aby oszczędziś sobie nerwów, i programowania")
			print("to zakończe")
			pyt()
			time.sleep(1)
			print("za nudne...")
			sys.exit()
		elif ziemie.lower() == "podróba jezusa":
			print("więc, jako jezus")
			time.sleep(2)
			jezus = input("czy zamieniasz swoje ciało w alimenty, a wino w swoją krew podczas życia z arturkiem?")
			if jezus.lower() == "tak":
				print ("więc, podczas ostatniej wieczerzy, ")
				print("zamieniasz wino w alimenciki a wino w krew podczas twojego życia z arturkiem")
				krad = input("więc, skoro zamieniłaś swoje ciało w alimenty, to co ty na to, aby je ukraść, jak ksiądz tace?")
				if krad.lower() == "tak":
					print("BRAWO! JESTEŚ BOGATA!")
					time.sleep(2)
					print("więc, aby zrobić jakąś różnorodność, tu przejdziemy do lat 2000")
					time.sleep(2)
					api = ["temu","facebook","szopi","akcjon","fejsbuczek","fejsbuk","read all pdf "]
					apus = input("więc, jakiej aplikacji używasz?")
					if apus.lower() in api:
						print("BRAWO! 'MYŚLISZ' JAK PRAWDZIWA AGACIA! ")
						time.sleep(2)
						print("BO AGACIA NIE MYŚLI!")
						time.sleep(2)
						print("WIĘC UŻYWA APLIKACJI, KTÓRE NIE WYMAGAJĄ MYŚLENIA")
						
						
			#TU
					elif apus.lower() not in api:
						print("tego chyba nie ma!")
						time.sleep(2)
						print("więc uznam to jako obraze agaciową")
						time.sleep(2)
						print("GAME OVER aGA: TROCHE")
						sys.exit()
				elif krad.lower() == "nie":
					print("AGACIA NIGDY NIE JEST SKROMNA! AGACIA TO KRÓLOWA WSZECHŚWIATA, NAPIĘKNIEJSZA, NAJMĄDRZEJSZA I NAJLEPSZA")
					time.sleep(3)
					jeb()
					print ("GAME OVER aGA: ZGADNIJ!")
					sys.exit()
					
			elif jezus.lower() == "nie":
				print("NIE JESTEŚ AGACIĄ!")
				time.sleep(2)
				print("GAME OVER aGA: NIE WIEM")
				sys.exit()
	elif agata.lower() == 'nie':
		print ("źle ")
		time.sleep(2)
		print ("Walnęłaś w słońce ")
		print ("GAME OVER           aGA:-1")
		sys.exit()

jajko = hashuje_potem

if agateczek == 2:
    print("""
    """)
    print("odpowiedzi nie ma w katalogu...")
    time.sleep(2)
    for _ in track(range(5000), description="Wgrywanie wirusów..."):
        time.sleep(0.001)
    sys.exit()

# Zaczęcie
print(f"A więc zaczynamy {imie_gracza}!")

# Losowanie miejsca urodzenia
miejsca = ["Warszawie", "Krakowie", "Lublinie", "Poznaniu", "Gdańsku",
           "Wrocławiu", "Łodzi", "Szczecinie", "Gdyni", "Katowicach",
           "Bydgoszczy", "Białymstoku", "Toruń", "Rzeszowie", "Opolu",
           "Koszalinie", "Kielcach", "Częstochowie", "Zielonej Górze",
           "Radomiu", "Elblągu", "Piotrkowie Trybunalskim", "Tychach",
           "Nowym Sączu", "Płocku", "Siedlcach", "Świnoujściu", "Jaworznie",
           "Chorzowie", "Włocławku", "Stalowej Woli", "Zamościu"]
wylosowane = random.choice(miejsca)

# Pierwszy wybór
pierwszy_wybór = input(f"{imie_gracza}, urodziłeś/aś się w {wylosowane}. Twój pierwszy wybór to: jesteś 'grzeczny' czy 'niegrzeczny' (ma to duży wpływ na dalsze rzeczy): ")

# Drugi wybór dla grzecznych
if pierwszy_wybór.lower() == "grzeczny":
    drugi_wybór = input("Super 'grzeczne' dziecko. Twój drugi wybór: twój ojciec próbuje cię zabawić. Co robisz? (odpowiedzi: 'śmieje się' albo 'nie śmieje się'): ")
    jeb()

    if drugi_wybór.lower() == "śmieje się" or drugi_wybór.lower() == "śmieje sie":
        print("Brawo! Właśnie zakolegowałeś/aś się z ojcem.")
        ucieczka = input("twojemu ojcu się nie podoba że się z niego naśmiewasz kończysz się śmiać?(odpowiedzi: 'tak' lub 'nie' ")
        if ucieczka.lower() == "tak":
            print("Brawo! Właśnie uniknąłeś/aś śmierci.")
            pyt()
            time.sleep(1)
            piripiri = input("A teraz co wybierasz, bo masz jakoś 5 lat, idziesz do szkoły?")
            if piripiri.lower() == "tak":
            	print("Brawo! właśnie uniknąłeś/aś wywalenia z domu bo twój stary nie będzie utrzymywał darmo-zjada ")
            	time.sleep(1)
            	szkola()
            elif piripiri.lower() == "nie":
             	print("twój ojciec cię wywalił z domu bo jesteś darmo-zjadem")
             	time.sleep(3)
             	print("więc teraz jesteś bezdomny")
             	time.sleep(2)
             	ryzyk = input("chcesz zaryzykować i zmienić się w aleksandra od IT?")
             	if ryzyk.lower()== "tak":
             		losus()
             	elif ryzyk.lower()=="nie":
             		ahaa("nie? ")
             		ahaa("to... ")
             		ahaa("N")
             		ahaa("I")
             		ahaa("E")
             		sys.exit()
        elif ucieczka.lower() == "nie":
        	print ("papa")
        	time.sleep(2)
        	print ("GAME OVER            AGE:5")
        	sys.exit()

    elif drugi_wybór.lower() == "nie śmieje się":
        print("Twój ojciec jest alkoholikiem... Odebrał to jako obrazę... Zabija cię...")
        print("GAME OVER            AGE:1")
        sys.exit()
    # Trzeci wybór
    trzeci_wybór = input("Twoim następnym wyborem jest: czy idziesz do szkoły? (odpowiedzi: 'tak' lub 'nie'): ")

    if trzeci_wybór.lower() == "tak":
        print("Brawo! Idziesz do szkoły!")
        time.sleep(2)
        wybór_w_szkole = input("Ktoś się do ciebie pruje, co robisz? (odpowiedzi: 'nawalam go', 'jestem 60', 'ignoruje'): ")
        if wybór_w_szkole.lower() == "nawalam go":
        	print("Masz szczęście, że twój ojciec uczył cię jak nawalać jako kibol.")
        	time.sleep(5)
        	print("NAWALIŁEŚ IM AŻ TAK, ŻE JEDNEMU Z NICH GŁOWA WYKRĘCIŁA SIĘ TAK W PRAWO, ŻE WYGLĄDA TO JAKBY NIE ŻYŁ!!!!!")
        	time.sleep(3)
        	print("TWÓJ OJCIEC CIĘ ZABIJE NA 50%!!!!!!")
        	zmienna_bojelubie = random.choice(["zabije","nie zabije"])
        	time.sleep(7)
        	print("Skończyłeś/aś zajęcia... Twój ojciec dostał już telefon ze szkoły...")
        	if zmienna_bojelubie.lower() == "zabije":
        	   print("GAME OVER          AGE:6")
        	   sys.exit()
        	elif zmienna_bojelubie.lower() == "nie zabije":
        	   	print("Twój ojciec jest uradowany... masz szczęcie!")
        	   	pyt()
        	   	time.sleep(2)
        	   	print("teraz ma zamiar cię uczyć")
        	   	time.sleep(2)
        	   	print("więc")
        	   	zamiar = input("zgadzasz się?")
        	   	if zamiar.lower() == "nie":
        	   	       print("ale....")
        	   	       time.sleep(2)
        	   	       print("wiesz co się czeka?")
        	   	       time.sleep(4)
        	   	       print("śmierć...")
        	   	       time.sleep(10)
        	   	       print("GAME OVER AGE: NIE WIEM, PEWNIE MAŁO")
        	   	       sys.exit()
        	   	elif zamiar.lower() == "tak":
        	   	       print("BRAWO!")
        	   	       time.sleep(2)
        	   	       print("WŁAŚNIE NIE ZGINĄŁEŚ!")
        	   	       time.sleep(2)
        	   	       print("więc, gdy już znasz wszystkie techniki")
        	   	       time.sleep(2)
        	   	       print("wiesz, że uda ci się powalić człowieka 1 ruchem")
        	   	       time.sleep(2)
        	   	       bicek = input("napadasz na bank?")
        	   	       if bicek.lower() == "tak":
        	   	       	print("właśnie napadłeś na bank!")
        	   	       elif bicek.lower() == "nie":
            	       		print("aha...")
            	       		time.sleep(2)
            	       		print("w sensie, aha to moja ulubiona biblioteka w termux")
            	       		time.sleep(2)
            	       		print("polecam")
            	       		aha_lib = input("zgadzasz sie?")
            	       		jeb()
            	       		if aha_lib.lower()== "tak":
            	       			pyt()
            	       			#TU
            	       		else:
            	       			banicja()

    elif trzeci_wybór.lower() == "nie":
        na_pewno = input("Przypominam: twój ojciec to alkoholik, na pewno chcesz to zrobić? (tak/nie): ")
        if na_pewno.lower() == "tak":
            print("Brawo! Właśnie zginąłeś.")
            print("GAME OVER         AGE:8")
            sys.exit()
        elif na_pewno.lower() == "nie":
            print("Brawo! Właśnie nie zginąłeś")
            # szkoła
            wybór_w_szkole = input("Ktoś się do ciebie pruje, co robisz? (odpowiedzi: 'nawalam go', 'jestem 60', 'ignoruje'): ")
            if wybór_w_szkole.lower() == "nawalam go":
                print("Masz szczęście, że twój ojciec uczył cię jak nawalać jako kibol.")
                time.sleep(5)
                print("NAWALIŁEŚ IM AŻ TAK, ŻE JEDNEMU Z NICH GŁOWA WYKRĘCIŁA SIĘ TAK W PRAWO, ŻE WYGLĄDA TO JAKBY NIE ŻYŁ!!!!!")
                time.sleep(3)
                print("TWÓJ OJCIEC CIĘ ZABIJE NA 50%(teraz poczekaj 7 sekund dla jakiegoś tam efektu)!!!!!!")
                zmienna_bojelubie = random.choice(["zabije","nie zabije"])
                jajko = hashuje_potem
                time.sleep(7)
                print("Skończyłeś/aś zajęcia... Twój ojciec dostał już telefon ze szkoły...")
                if zmienna_bojelubie.lower() == "zabije":
              	  print("GAME OVER          AGE:13")
              	  jeb()
              	  sys.exit()
                else :
                	print("Twój ojciec jest uradowany... masz szczęcie!")
                	time.sleep(2)
                	print("więc, teraz, pomińmy jakieś nudy życia")
                	time.sleep(2)
                	print("i przejdźmy do ważniejszych rzeczy")
                	time.sleep(2)
                	print("wgl, jebać apple, to gówno a nie firma")
                	time.sleep(2)
                	pyt()
                	
                	
                	#TU
            elif wybór_w_szkole.lower() == "ignoruje":
                	
                print("To był błąd...")
                time.sleep(3)
                print("Zabili na miejscu...")
                time.sleep(1)
                print("Ale nie martw się, twój ojciec cię pomści...")
                time.sleep(2)
                print("wybił jeden po drugim ")
                print("GAME OVER         AGE:13")
                	
                sys.exit()
            elif wybór_w_szkole.lower() == "jestem 60":
                print("Ale wiesz, że nie dojdziesz tam, bo cię zamknęli w łazience?")
                time.sleep(2)
                print("Zostałeś zabity...")
                print("Ale pamiętaj, że twój ojciec cię pomści")
                print("GAME OVER          AGE:13")
                sys.exit()
                jajko = hashuje_potem
                jeb()

# Drugi wybór dla niegrzecznych
elif pierwszy_wybór.lower() == "niegrzeczny":
    drugi_wybór = input("Super 'niegrzeczne' dziecko. Twój drugi wybór: widzisz okno, uciekasz czy nie? (odpowiedzi: 'tak' albo 'nie'): ")

    if drugi_wybór.lower() == "tak" or drugi_wybór.lower() == "uciekam":
        print("Idziesz za okno, wychodzisz, spadasz z drugiego piętra. Giniesz.")
        print("GAME OVER                 AGE:0")
        print("Ale twój stary cię kochał...")
        time.sleep(1)
        print("Nachlał się i się powiesił")
        time.sleep(1)
        print("Papa")
        console.print("[bold green]/sdcard/_TERMUKSIĄTKO[/bold green]", "$")
        time.sleep(5)
        for _ in track(range(200), description="Wgrywanie wirusów..."):
            time.sleep(0.1)
        #123
        sys.exit()

    elif drugi_wybór.lower() == "nie":
        print("Brawo! Tak skończył się twój pierwszy rok.")
        print("tak w ogóle to narazie mam z 3 ścieżki, które się bardzo różnią, ale na tą mam fajny plan")
        time.sleep(3)
        jakiś_wybór = input("Lecimy! Chcesz mieć depresję? odpowiedzi ('tak' lub 'nie'): ")
        if jakiś_wybór.lower() == "tak":
            print("Okej, masz depresję.")
            time.sleep(3)
            print("A i ta depresja nie będzie leczona, bo żyjesz w patologicznej rodzinie...")
            jeb()
            time.sleep(1)
            print("Więc za jakieś 5 sekund pojawi się komunikat, że zginąłeś/aś.")
            time.sleep(5)
            print("Umarłeś/aś z depresji przez samobójstwo (podcięcie żył)")
            print("GAME OVER             AGE:5")
            time.sleep(1)
            print("żartuje...")
            time.sleep(2)
            print("Dobra ale jednak masz tą depresje")
            time.sleep(1)
            psycholog = input("chcesz  chodzić do psychologa szkolnego?")
            if psycholog.lower() == "tak":
            	print("Ok")
            	time.sleep(1)
            	print("ale twój stary jako zawodowy pijak myśli, że psycholog to bzdura")
            	jeb()
            	time.sleep(2)
            	print("i dlatego, żebym miał mniej do programowania to zginiesz od niego niestety, ale za to rozbuduje bardziej inne ścieżki")
            	time.sleep(2)
            	print("GAME OVER              AGE : 8")
            	sys.exit()
            elif psycholog.lower() == "nie":
            	print("brawo! uniknąłeś/aś śmierci")
            	jajko = hashuje_potem
            	time.sleep(2)
            	print("bo twój stary twierdzi, że psycholog to bzdura")
            	time.sleep(2)
            	print("wgl, czas gry dzieje się zależnie od ścieżki")
            	time.sleep(3)
            	print("(wiem, genialne, i logiczne)")
            	time.sleep(2)
            	print("więc, teraz jest 2009")
            	time.sleep(2)
            	print("więc btc, jest mało warty")
            	time.sleep(3)
            	btc = input("więc, chcesz go kupić?")
            	if btc.lower() == "tak":
            		print("ale... twój ojciec, to pijak")
            		time.sleep(2)
            		pyt()
            		print("więc on nie zna innego wydawania pieniądza niż alkohol..")
            		time.sleep(5)
            		print("zabił cię, drąc ryja, że to głupoty")
            		time.sleep(1)
            		print ("GAME OVER.                 AGE :9")
            		jeb()
            		sys.exit()
            	elif btc.lower() == "nie":
            		print("BRAWO! WŁAŚNIE PRZEŻYŁEŚ!")
            #TU
            
        elif jakiś_wybór.lower() == "nie":
        	print ("okej")
        	time.sleep(2)
        	print ("nie masz depresji ale masz moc Boga xD")
        	time.sleep(2)
        	moc_Boga = input("masz do wyboru 'czytanie w myślach' albo 'teleportacja' ")
        	if moc_Boga.lower() == "czytanie w myślach":
        		print ("okej, ogólnie to masz ojca ")
        		time.sleep(3)
        		znajdziesz_mnie = hashuje_potem
        		ojciec_czytaniewmyślach = input("chcesz zobaczyć o czym myśli?")
        		if ojciec_czytaniewmyślach.lower() == "tak":
        			print ("twój ojciec myśli o tym czy cię wywalić z domu...")
        			time.sleep(2)
        			print ("bo jesteś darmo-zjadem")
        			time.sleep(2)
        			print ("i cię wywala...")
        			time.sleep(4)
        			print ("Ale ja jako twój prawie prywatny programista gry się zemszczę")
        			time.sleep(5)
        			print ("już się zemścilem... stafił go piorun ") #TU
        		elif ojciec_czytaniewmyślach.lower() == "nie":
        			print("Brawo! właśnie uniknąłeś wywalenia z domu")
        			#TU
        	
        	elif moc_Boga.lower() == "teleportacja":
        			print ("okej, twoja moc to teleportacja")
        			time.sleep(2)
        			pytanie = input("chcesz się teleportować i to przetestować?")
        			if pytanie.lower() == "tak":
        				gdzie = input("okej, możesz narazie tylko do domu ( do twojego pokoju) albo do szkoły (odpowiedzi: 'do szkoły' 'do pokoju')")
        				if gdzie.lower() == "do szkoły":
        					print("jest godzina około 20 a ty jesteś na obiedzie z rodziną")
        				#TU
        				elif gdzie.lower() == "do pokoju":
        					print("ogólnie to jesteś na obiedzie")
        					time.sleep(2)
        					print("i tak nie najlepiej twój ojciec zaakceptował to, że sobie zniknąłeś")
        					time.sleep(2)
        					print("więc masz jakoś 2 sekundy zanim stanie się 'wpadek'")
        					time.sleep(2)
        					wypadl()
        					time.sleep(2)
        					print("więc, skoro tu jesteś,to jeszcze żyjesz (narazie)")
        					time.sleep(2)
        					praca = input("to może skipniemy życie do pracy?")
        					jajko = hashuje_potem
        					
        					if praca.lower() == "tak":
        						print("okej, to aby się nie przemęczaś i redukować sobie pracę")
        						time.sleep(2)
        						print("będziesz Aleksandrem od IT")
        						time.sleep(0.5)
        						print("chyba")
        						losus()
        					elif praca.lower() == "nie":
        						print("zaraz")
        						#TU
        			elif pytanie.lower() == "nie":
        				print ("i dobrze bo jesteś na obiedzie a twój ojciec jest pijany więc jak byś wrócił powiedziałby że jesteś czarodziejem i musisz zginąć") 
        				#TU
        			
		
        # Trzeci wybór
        trzeci_wybór = input("Twoim następnym wyborem jest: czy idziesz do szkoły? (odpowiedzi: 'tak' lub 'nie'): ")

        if trzeci_wybór.lower() == "tak":
            print("Brawo! Idziesz do szkoły!")
            wybór_w_szkole = input("Ktoś się do ciebie pruje, co robisz? (odpowiedzi: 'nawalam go', 'jestem 60', 'ignoruje'): ")
            if wybór_w_szkole.lower() == "nawalam go":
                print("Masz szczęście, że twój ojciec uczył cię jak nawalać jako kibol.")
                time.sleep(5)
                print("NAWALIŁEŚ IM AŻ TAK, ŻE JEDNEMU Z NICH GŁOWA WYKRĘCIŁA SIĘ TAK W PRAWO, ŻE WYGLĄDA TO JAKBY NIE ŻYŁ!!!!!")
                time.sleep(3)
                print("masz 50% szans że przeżyjesz ale 50% że zginiesz (dla napięcia chwilę poczekasz)")
                time.sleep(7)
                szansa = [ "a", "b" ]
                wylosowaniee = random.choice(szansa)
                if wylosowaniee.lower() == "a":
                	print ("brawo nie zginąłeś")
                	print("więc, teraz po tej bujce")
                	time.sleep(1)
                	cosiek = input("masz wybór, czy chcesz, mieć kolegów w szkole?")
                	if cosiek.lower() == "tak":
                		print("BRAWO!")
                		time.sleep(2)
                		print("właśnie 'otrzymałeś' przyjaciół!")
                		time.sleep(3)
                		print("mam pomysł!")
                		time.sleep(1)
                		print("dodam wypadki!")
                		time.sleep(2)
                		print("zaprogramowałem wypadki, między tym a ostatnim printem, więc, zobaczmy czy działa ")
                		time.sleep(2)
                		wypadl()
                		print("czyli działa!")
                		time.sleep(2)
                		print("więc wymyśle coś na tą ścieżke...")
                		time.sleep(2)
                		print("skoro masz przyjaciół")
                		time.sleep(1)
                		jebix = input("to może chcesz sie z nimi spotkać?")
                		if jebix.lower() == "tak":
                		    print("spotykacie sie...")
                		    time.sleep(2)
                		    print("wciągasz trawe...")
                		    time.sleep(2)
                		    print("giniesz w rowie")
                		    sys.exit()
                		    
                		elif jebix.lower() == "nie":
                		    print("czyli zostajesz w domu na kolejną kłótnie?")
                		    time.sleep(1)
                		    print("okej pojebusie!")
                		    time.sleep(1)
                		    print("czyli sie kłócisz z ojcem alkoholikiem...")
                		    time.sleep(2)
                		    print("i ojcec cie zabija!")
                		    sys.exit()
                		    
                		else:
                		    print("TO SPIERDALAJ W TAKIM RAZIE!")
                		    sys.exit()
                		
                	
                	elif cosiek.lower()== "nie":
                		print("czyli, będą cię dalej gnębić?(to pytanie retoryczne)")
                		time.sleep(1)
                		print("bo odpowiedź to oczywiście...")
                		time.sleep(2)
                		print("TAK!")
                		time.sleep(2)
                		print("więc, teraz...")
                		time.sleep(2)
                		zmienir = input("idziesz to sklepu?")
                		if zmienir.lower() == "tak":
                			print("niestety...")
                			time.sleep(3)
                			print('pamiętasz tych "kolegów"? ')
                			time.sleep(2)
                			print("niestety, znajeźli cię")
                			time.sleep(4)
                			print("zabili na miejscu")
                			print (" GAME OVER.                 AGE :13")
                			sys.exit()
                		elif zmienir.lower() == "nie":
                			print("jak coś, to co z którymi się nie przyjaźnisz, postanowili się na ciebie zaczaić, dobrze,")
                			time.sleep(2)
                			print("dobrze, że nie wyszedłeś...")
                			time.sleep(2)
                			print("zabiliby na miejscu...")
                			wypadl()
                			for _ in track(range(500), description="Ładowanie wgrywanie wirusów..."):
                			    time.sleep(0.001)
                			
                			
                	#TU
                elif wylosowaniee.lower() == "b":
                	print ("niestety zginąłeś")
                	print (" GAME OVER.                 AGE :13")
                	sys.exit()

            elif wybór_w_szkole.lower() == "ignoruje":
                print("To był błąd...")
                time.sleep(3)
                print("Zabili na miejscu...")
                time.sleep(1)
                print("Ale nie martw się, twój ojciec cię pomści...")
                time.sleep(1)
                print("GAME OVER         AGE:13")
                time.sleep(1)
                print("wybił na miejscu")
                sys.exit()

            elif wybór_w_szkole.lower() == "jestem 60":
                print("Ale wiesz, że nie dojdziesz tam, bo cię zamknęli w łazience?")
                print("Zostałeś zabity...")
                print("GAME OVER          AGE:13")
                sys.exit()

        elif trzeci_wybór.lower() == "nie":
            na_pewno = input("Przypominam: twój ojciec to alkoholik, na pewno chcesz to zrobić? (tak/nie): ")
            if na_pewno.lower() == "tak":
                print("Brawo! Właśnie zginąłeś.")
                print("GAME OVER         AGE:8")
                sys.exit()
            elif na_pewno.lower() == 'nie':
                print("Brawo! Udało ci się nie zginąć!") 
                wybór_w_szkole = input("Ktoś się do ciebie pruje, co robisz? (odpowiedzi: 'nawalam go', 'jestem 60', 'ignoruje'): ")
            if wybór_w_szkole.lower() == "nawalam go":
                print("Masz szczęście, że twój ojciec uczył cię jak nawalać jako kibol.")
                time.sleep(5)
                print("NAWALIŁEŚ IM AŻ TAK, ŻE JEDNEMU Z NICH GŁOWA WYKRĘCIŁA SIĘ TAK W PRAWO, ŻE WYGLĄDA TO JAKBY NIE ŻYŁ!!!!!")
                time.sleep(3)
                print("TWÓJ OJCIEC CIĘ ZABIJE NA 50%!!!!!!")
                zmienna_bojelubie = random.choice(["zabije","nie zabije"])
                time.sleep(7)
                print("Skończyłeś/aś zajęcia... Twój ojciec dostał już telefon ze szkoły...")
                if zmienna_bojelubie.lower() == "zabije":
              	  print("GAME OVER          AGE:13")
              	  print("jebać apple")
              	  sys.exit()
                else :
                	print("Twój ojciec jest uradowany... masz szczęcie!")
                	time.sleep(2)
                	print("i do tego, chce nauczyć się nowych technik!")
                	bicsie = input("zgadzasz się?")
                	if bicsie.lower()== "tak":
                		print("brawo!")
                		
                	elif bicsie.lower() == "nie":
                		print("no to zginiesz!")
                		time.sleep(3)
                		print("albo na jakoś 1/12")
                		wypadl()
                		print("nie umarłeś?")
                		time.sleep(2)
                		print("to co ty na...")
                		time.sleep(1)
                		print("nową funkcję?")
                		time.sleep(2)
                		print("jebać apple wgl")
                		losus()
                		print("jeśli to widzisz to coś się zwaliło, albo gra nie jest dokończona ")
                		
else:
    print("""
    """)
    print("wiesz co? to nawet nie jest śmieszne...")
    for _ in track(range(5000), description="Wgrywanie wirusów..."):
        time.sleep(0.001)
    sys.exit()