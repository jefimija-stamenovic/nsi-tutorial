# 🌟 Python FastAPI - Tutorijal

FastAPI je moderan, brz (high-performance) Python web framework za kreiranje API-a. 
Dizajniran je tako da bude jednostavan za korišćenje, ali ujedno i efikasan i pouzdan što ga je 
učinilo jednim od čestih izbora programera za razvoj RESTful API-ja i web aplikacija. 
Svoju popularnost je stekao zbog jednostavnosti, automatskog generisanja dokumentacije i 
veoma dobrih performansi. 

---

## 🎯 **Karakteristike FastAPI-a**
1. **Automatsko dokumentovanje API-a**: FastAPI automatski generiše interaktivnu dokumentaciju API-ja koristeći
OpenAPI standard. Pregled dokumentacije je dostupan na posebno definisanim krajnjim tačkama (engl. *endpoints*)
u aplikaciji što olakšava razumevanje i testiranje API-ja. Ovim se štedi vreme jer nema potrebe za ručnim pisanjem
opširne dokumentacije. 

2. **Python type hintovi**: Jedna od najbitnijih prednosti FastAPI-ja je upotreba Python type 
hintova. Parametri i povratne vrednosti funkcija se anotiraju čime se značajno poboljšava čitljivost koda. 
Osim toga, FastAPI automatski obavlja validaciju ulaznih podataka i generiše API dokumentaciju. 

3. **Validacija podataka**: FastAPI koristi **Pydantic** modele za automatsko proveravanje ispravnosti
podataka. Pomoću Pydantic šema, mogu se jasno definisati pravila i struktura očekivanih podataka. Na ovaj način, 
ulazni podaci se proveravaju automatski, pretvaraju se u odgovarajuće formate i pripremaju se za dalju obradu čime 
je značajno smanjen rizik od rada sa neispravnim ili nepravilnim podacima. 

4. **Asinhrono programiranje**: FastAPI je ispratio trend rasta popularnosti asinhronog programiranja u Python-u, pa 
u potpunosti podržava asinhrone operacija. Standardno, koriste se ključne reči *async* i *await* za pisanje asinhronih
krajnjih tačaka što ga čini idealnim za zadatke vezane za ulazno-izlazne operacije i poboljšava ukupno odzivnost aplikacije

5. **Dependency injection**: FastAPI podržava *dependency injection* čime je moguće definisanje i 
korišćenje zavisnosti među komponentama aplikacije. Upotreba *dependency injection-a* čini kod modularnim, 
olakšava njegovo testiranje i održavanje. 

6. **Bezbednost** : FastAPI pruža podršku za različite vrste autentifikacije i autorizacije (npr. OAuth2, 
JWT). Sem toga, automatskom validacijom ulaznih vrednost, FastAPI pomaže u zaštiti aplikacije od nekih uobičajenih 
hakerskih napada poput *SQL injection-a* ili *XSS-a (cross-site scripting)*. Ovim je značajno povećana 
sigurnost aplikacije i efikasno su zaštićene osetljivi podaci i korisničke informacije. 

---

## 🎯 **Prednosti i mane FastAPI-a**
### Prednosti ###
1. **Jednostavan za učenje i korišćenje**: FastAPI je dizajniran tako da bude jednostavan,
naročito za Python programere. Sintaksa je intuitivna, a automatsko generisanje 
dokumentacije olakšava rad programera i održavanje aplikacije. 
2. **Visoke performanse**: FastAPI je jedan od najbržih web framework-a 
zahvaljujući podršci za asinhrono programiranje i efikasnim rukovanjem podacima. Aplikacije mogu
da obrađuju veliki broj zahteva pri čemu neće doći do njenog usporenja. 
3. **Automatska validacija podataka**: FastAPI automatski vrši validaciju podataka na osnovu prethodno 
definisanih struktura podataka korišćenjem Python type hintova, čime je smanjena mogućnost za nastanak 
grešaka uzrokovanih neispravnim unosom.
4. **Autentifikacija i autorizacija**: Jednostavno se upravlja autentifikacijom i autorizacijom
bez obzira da li se koristi JWT, OAuth2 ili nešto drugo. 
5. **Middleware**: Lako se dodaju middleware-i za logovanje, autentifikaciju itd. 

### Mane ###

1. **Učenje**: Iako je FastAPI prilagođen programerima, može biti izazovan za one koji se 
nisu susretali sa asinhronim programiranjem ili web framework-ovima generalno.
2. **Community zajednica i dokumentacija**: Iako community zajednica FastAPI-a
brzo raste, ona i dalje nije toliko velika kao kod nekih drugih popularnih web 
framework-a što rezultira manjkom tutorijala itd. 

---

## :computer: **Pokretanje projekta**

## Kloniranje projekta 

1. **Klonirajte projekat sa Github-a**
2. **Otvorite folder u Visual Studio Code ili u nekom drugom IDE-u za Python**
3. **Premestite se u folder *fastapi* tako što ćete u terminalu ukucati *cd fast-api***

### Virtuelno okruženje
Pre nego što instaliramo **Python FastAPI** web framework, kreiraćemo virtuelno okruženje (engl. *virtual environment*). 
Kreiranjem virtuelnog okruženja, omogućena je izolacija biblioteka u Python-u čime se sprečavaju potencijalni konflikti 
među verzijama i obezbeđuje se konzistentnost u radu na projektu. Upotreba virtuelnih okruženja je naročito korisna 
prilikom rada na više projekata gde svaki projekat zahteva neku drugu verziju iste biblioteke. 
Otvorite terminal i unesite sledeću komandu: 

```bash
python -m venv naziv_virtuelnog_okruzenja
```
Da bismo aktivirali kreirano virtuelno okruženje, u terminalu unosimo sledeću komandu: 
```bash
naziv_virtuelnog_okruzenja\Scripts\Activate.ps1
```
Sada kada smo aktivirali virtuelno okruženje, možemo da instaliramo **Python FastAPI** web framework. 
U terminalu pokrećemo sledeću komandu: 
```bash
pip install "fastapi[standard]"
```
U okviru trenutnog foldera u kom radite, kreirajte fajl **main.py** koji će sadržati sledeći kod: 

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```
Da bismo pokrenuli naš web server, u terminalu kucamo sledeću komandu 
```bash
   fastapi dev main.py
```

Klikom na sledeći [link](http://127.0.0.1:8000/), u okviru web pretraživača, imaćete sledeći rezultat: 

![hello-world-primer](./fast-api/resources/images/image.png)

Prilikom kreiranja **Python FastAPI** projekta, na [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 
je dostupan Swagger UI. Swagger UI je jedan od Swagger alata koji omogućava pregled i interakciju sa API-jima 
web servera kroz interaktivni web interfejs. Korisnici mogu da vide sve dostupne krajnje tačke (engl. *endpoints*), 
parametre i odgovore API-ja, kao i da direktno testiraju pozive bez nekih dodatnih alata. Trenutni izgled Swagger 
UI-a je prikazan na slici ispod: 

![izgled-swagger-ui](./fast-api/resources/images/image-1.png)

Alternativno, na [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) je dostupan ReDoc (slika ispod). 
Redoc je alat otvorenog koda (engl. *open-source*) za automatsko pravljenje API dokumentacije. ReDoc projekat je 
dostupan na Github-u, tako da možete pogledati projekat na [linku](https://github.com/Redocly/redoc)

![izgled-redoc-ui](./fast-api/resources/images/image-2.png)

### ⚙️ Šta je Uvicorn?
Sastavni deo FastAPI aplikacije je **Uvicorn**, brz i lagan ASGI (Asynchronous Server Gateway Interface) server koji 
omogućava pokretanje aplikacije i obradu korisničkih zahteva. Uvicorn obezbeđuje brzu i pre svega efikasnu komunikaciju 
klijenta i servera, pri čemu podržava i moderne tehnologije kao što su HTTP/2 i WebSocket. Integracija FastAPI-a i Uvicorn-a 
garantuje visoke performanse i stabilan rad aplikacije što ga čini pogodnim za produkciju. 

Alternativno pokretanje projekta korišćenjem uvicorn-a je: 
```bash
uvicorn main:app --reload
```

### Arhitektura FastAPI web servera

Na slici ispod je prikazana arhitektura FastAPI web servera: 

![arhitektura-fastapi-servera](https://media.licdn.com/dms/image/v2/D4D12AQG_nawivlNG-Q/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1688666263274?e=2147483647&v=beta&t=tEFDYkFC0DSZdFpB86QNh75rC0P-GiDeocqtPfApug8)

Baš kao i kod bilo kog drugog web servera, i ovde se arhitektura sastoji od klijenta koji šalje HTTP zahteve, 
Uvicorn web servera koji prosleđuje zahteve FastAPI aplikaciji 

# Pydantic
FastAPI koristi standardne Python tipove podataka (kao što su int, str, float...) za definisanje tipvoa u aplikaciji. FastAPI ima integraciju sa bibliotekom Pydantic koja omogućava jednostavno validiranje i manipulaciju podacima. 

## 🎓 **Resursi za učenje**
- [Zvanična dokumentacija](https://fastapi.tiangolo.com)  
- [Primeri na GitHub-u](https://github.com/tiangolo/fastapi)  
- [GeeksForGeeks](https://www.geeksforgeeks.org/fastapi-introduction/)

---


## 📬 **Kontakt**
Ukoliko imate nekih pitanja ili želite da doprinesete projektu, pišite nam na **jefimija.stamenovic@gmail.com**