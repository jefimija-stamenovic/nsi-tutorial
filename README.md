# 🌟 Python FastAPI - Tutorijal

## Problematika ##
FastAPI je Python framework kreiran sa ciljem da ubrza razvoj i unapredi kvalitet web API server-a. Sam razvoj API-ja uključuje različite izazove poput ručne validacije podataka, održavanja dokumentacije i postizanja visokih performansi naročito pri obradi velikih količina zahteva. 
FastAPI rešava ove probleme jer pruža automatsku validaciju, automatsko generisanje dokumentacije u realnom vremenu i podršku za asinhroni rad. Pored toga, FastAPI koristi Python tipove za tipsku sigurnost čime se smanjuje broj grešaka i povećava pouzdanost koda čineći sam razvoj efikasnijim i manje podložnim greškama.  

---

## 🎯 **Karakteristike FastAPI-a**

### Ključne karakteristike FastAPI-ja

1. **Automatsko dokumentovanje API-a**: FastAPI automatski generiše interaktivnu dokumentaciju API-ja koristeći OpenAPI standard. Pregled dokumentacije je dostupan na posebno definisanim krajnjim tačkama (engl. *endpoints*) u aplikaciji što olakšava razumevanje i testiranje API-ja. Ovim se štedi vreme jer nema potrebe za ručnim pisanjem opširne dokumentacije. 

2. **Python type hintovi**: Jedna od najbitnijih prednosti FastAPI-ja je upotreba Python type hintova. Parametri i povratne vrednosti funkcija se anotiraju čime se značajno poboljšava čitljivost koda. 

3. **Validacija podataka**: FastAPI koristi **Pydantic** modele za automatsko proveravanje ispravnosti podataka. Pomoću Pydantic šema, mogu se jasno definisati pravila i struktura očekivanih podataka. Na ovaj način, ulazni podaci se proveravaju automatski, pretvaraju se u odgovarajuće formate i pripremaju se za dalju obradu čime je značajno smanjen rizik od rada sa neispravnim ili nepravilnim podacima. 

4. **Asinhrono programiranje**: FastAPI je ispratio trend rasta popularnosti asinhronog programiranja u Python-u, pa u potpunosti podržava asinhrone operacije. Standardno, koriste se ključne reči *async* i *await* za pisanje asinhronih krajnjih tačaka što ga čini idealnim za zadatke vezane za ulazno-izlazne operacije i poboljšava ukupno odzivnost aplikacije

5. **Dependency injection**: FastAPI podržava *dependency injection* čime je moguće definisanje i korišćenje zavisnosti među komponentama aplikacije. Upotreba *dependency injection-a* čini kod modularnim, olakšava njegovo testiranje i održavanje. 

6. **Bezbednost** : FastAPI pruža podršku za različite vrste autentifikacije i autorizacije (npr. OAuth2, JWT). Sem toga, automatskom validacijom ulaznih vrednost, FastAPI pomaže u zaštiti aplikacije od nekih uobičajenih hakerskih napada poput *SQL injection-a* ili *XSS-a (cross-site scripting)*. Ovim je značajno povećana sigurnost aplikacije i efikasno su zaštićene osetljivi podaci i korisničke informacije. 

---

## 🎯 **Prednosti i mane FastAPI-a**
### Prednosti ###
1. **Jednostavan za učenje i korišćenje**: FastAPI je dizajniran tako da bude jednostavan, naročito za Python programere. Sintaksa je intuitivna, a automatsko generisanje dokumentacije olakšava rad programera i održavanje aplikacije. 
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
framework-a.

---

## Zašto baš FastAPI? Ko su njegovi konkurenti? 
U odnosu na svoje konkurente poput Flask-a i Django-a, FastAPI balansira između brzog razvoja, jednostavnosti i modernih, tehničkih mogućnosti.
Flask je poznat po svojoj fleksibilnosti, ali programeri ulažu dodatno vreme na validaciji podataka, ručnom generisanju dokumentacije i obradi većeg broja zahteva.  <br> Django, kao drugi konkurent, nudi robusna rešenja, ali sa dodatnim slojevima kompleksnosti koji i nisu neophodni za razvoj API-ja. <br> Prilikom korišćenja FastAPI-ja, programeri se fokusiraju na samu logiku poslovanja, bez da gube vreme na tehničke detalje poput validacije ulaznih i izlaznih podataka ili kreiranja propratne dokumentacije. Sem toga, njegova podrška za asinhroni rad, integracija sa Python tipovima i kompatibilnost sa OpenAPI-em ga čini kao adekvatnim izborom koji objedinjuje brzinu, sigurnost i efikasnost. 

---

## :computer: **Pokretanje projekta**

## Kloniranje projekta

- **Klonirajte projekat sa Github-a**
```bash 
git clone https://github.com/jefimija-stamenovic/nsi-tutorial
```
- **Premestite se u folder fast-api**

```bash 
cd fast-api
```

### Virtuelno okruženje
Pre nego što instaliramo **Python FastAPI** web framework, kreiraćemo virtuelno okruženje (engl. *virtual environment*). Kreiranjem virtuelnog okruženja, omogućena je izolacija biblioteka u Python-u čime se sprečavaju potencijalni konflikti među verzijama i obezbeđuje se konzistentnost u radu na projektu. Upotreba virtuelnih okruženja je naročito korisna prilikom rada na više projekata gde svaki projekat zahteva neku drugu verziju iste biblioteke. U terminalu unesite sledeću komandu: 
```bash
python -m venv naziv_virtuelnog_okruzenja
```

Da bismo aktivirali kreirano virtuelno okruženje, u terminalu unosimo sledeću komandu: 
```bash
naziv_virtuelnog_okruzenja\Scripts\Activate.ps1
```

Sada kada smo aktivirali virtuelno okruženje, možemo da instaliramo sve biblioteke koje su potrebne za pokretanje projekta. U terminalu unesite sledeću komandu: 
```bash 
    pip install -r requirements.txt
```
U ovom projektu će biti korišćena MySQL baza podataka i zato je potrebno da kreirate bazu sa podešavanjima prikazanim na slici ispod:

![db-schema](./fast-api/resources/images/image_db.png)

Glavni fajl ovog projekta je main.py čiji je kod dat ispod:
```python 
from fastapi import FastAPI
from database import engine
from UI.users import router as router_user
from UI.todos import router as router_todo
from dotenv import load_dotenv
import models.user as model_user
import models.todo as model_todo
import os 

model_user.Base.metadata.create_all(bind=engine)
model_todo.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Napredno softversko inženjerstvo - FastAPI tutorial")
app.include_router(router_user)
app.include_router(router_todo)

load_dotenv()

@app.get("/")
def read_root():
    return {"message": "Hello, this is tutorial for FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
```

Da bismo pokrenuli naš web server, u terminalu kucamo sledeću komandu 
```bash
   fastapi dev main.py
```
ili 
```bash
python main.py
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

### Arhitektura FastAPI web servera

Na slici ispod je prikazana arhitektura FastAPI web servera: 
![arhitektura-fastapi-servera](https://media.licdn.com/dms/image/v2/D4D12AQG_nawivlNG-Q/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1688666263274?e=2147483647&v=beta&t=tEFDYkFC0DSZdFpB86QNh75rC0P-GiDeocqtPfApug8)

Arhitekturu možemo da podelimo na nekoliko segmenata: 
1. Klijent - šalje HTTP zahteve (GET, POST, PUT, DELETE) na određeni URL (http://localhost:8000/...) putem web pretraživača ili nekog drugog interfejsa kako bi komucirao sa serverom. 
2. Web server - koristi se Uvicorn - asinhroni server kompatibilan sa ASGI standardom. Ujedno, Uvicorn predstavlja posrednika između klijenta i FastAPI aplikacije tako što prihvata zahteve i prosleđuje ih aplikaciji. 
3. Sloj aplikacije - predstavlja sloj koji implementira logiju apkikacije koristeći FastAPI framework. U okviru njega ima više komponenti: 
    1) *Logika rutiranja* definiše način na koji aplikacija obrađuje pristigle HTTP zahteve. Main.py predstavlja glavni fajl u okviru kog se definišu sve funkcije koje odgovaraju na zahteve. 
    2) *Pydantic modeli* se koriste za validaciju i serijalizaciju podataka čime je obezbeđeno da aplikacija ima tačne i konzistentne ulazne i izlazne podatke. Ovim modelima se definiše struktura podataka koji su potrebni za rad aplikacije. Pydantic automatski validira podatke koje klijent šalje i generiše dobro formatirane odgovore čime se značajno obrzava razvoj i smanjuje se mogućnost za nastanak grešaka 
    3) *SQLAlchemyORM* se koristi za rad sa bazom podataka na objektno-relacijski način. ORM modelima se definiše struktura podataka koji se čuvaju u bazi podataka i omogućena je jednostavna manpulacija podacima bez direktnog pisanja SQL upita. Modeli su obično deklarisani i implementirani u fajlu *model.py*
    Pored modela, imamo i fajl *database.py* koji služi za upravljanje konekcijama sa bazom podataka. U okviru ovog fajla se konfiguriše konekcija i sesije koje omogućavaju aplikaciji da komunicira sa bazom. 
---

### ⚙️ Šta je Uvicorn?
Sastavni deo FastAPI aplikacije je **Uvicorn**, brz i lagan ASGI (Asynchronous Server Gateway Interface) server koji omogućava pokretanje aplikacije i obradu korisničkih zahteva. Uvicorn obezbeđuje brzu i pre svega efikasnu komunikaciju 
klijenta i servera, pri čemu podržava i moderne tehnologije kao što su HTTP/2 i WebSocket. Integracija FastAPI-a i Uvicorn-a garantuje visoke performanse i stabilan rad aplikacije što ga čini pogodnim za produkciju. 

Ukoliko zakomentarišete sledeći deo u main.py
```python 
if __name__ == "__main__":
    import uvicorn
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
```
možete alternativno pokrenuti projekat korišćenjem uvicorn-a: 
```bash
uvicorn main:app --reload
```

## Konfiguracija baze podataka 

U okviru fajla database.py je konfigurisana konekcija ka prethodno kreiranoj MySQL bazi podataka. Kod je prikazan ispod: 
```python
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from dotenv import load_dotenv
    import os

    load_dotenv()

    DB_URL = os.getenv("DB_URL", "mysql+pymysql://root:root@localhost:3306/fast_api_sample")
    engine = create_engine(DB_URL,echo=True)
    SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

    Base = declarative_base()
```
Sami parametri za konekciju su definisani u okviru fajla .env koji treba ručno da kreirate. Kod koji je prikazan ispod iskopirajte i promenite parametre tako da odgovaraju vašem MySQL serveru: 
```bash 
DB_URL = "mysql+pymysql://root:root@localhost:3306/fast_api_sample"
HOST = "localhost"
PORT = 8000
```
U .env fajlu se, osim DB_URL konstante, nalaze i HOST i PORT konstante kojima se definišu host i port za pokretanje servera. One se učitavaju u main.py fajlu, tako da slobodno možete da ih promenite ukoliko želite da Vaš server radi na nekom drugom portu ili ukoliko želite da bude javno dostupan. 

# SQLAlchemy ORM 
SQLAlchemy je Python biblioteka za rad sa bazama podataka i u kombinaciji sa FastAPI-em omogućava efikasno upravljanje podacima. SQLAlchemy ima podršku za Object-Relational Mapping (ORM), pa samim tim omogućava mapiranje klasa na tabele u bazi. FastAPI koristi SQLAlchemy za: 
- **definisanje modela** - klase se mapiraju na tabele u bazi podataka 
- **upravljanje sesijama** - u sklopu biblioteke SQLAlchemy, postoji implementirana klasa Session koja služi za transakcije i rad sa bazom 
- **CRUD operacije** - kreiranje, čitanje, ažuriranje i brisanje podataka 

Kod ispod prikazuje kako su kreirane dve tabele upotrebom SQLALchemy ORM-a. Za svaku klasu se definiše naziv tabele u bazi koju reprezentuje. Nakon toga se definišu nazivi kolona, njihovi tipovi, da li su primarni ključ, indeksieane i jedinstvene. Takođe, 
definišu se veze među tabelama pomoću **relationship**
```python 
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    todos = relationship("Todo", back_populates="owner", cascade="all, delete")
    is_active = Column(Boolean, default=False)
    
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(255), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="todos")
```
Za Todo tabelu je karakteristično da ima referencu na tabelu Users jer zadatak pripada nekom korisniku. Zato je potrebno kaskadno brisanje kada se obriše korisnik što je definisano na tabeli Users sa  

```python 
back_populates="owner", cascade="all, delete")
```
## Troslojna arhitektura ##
Arhitektura DAL-BL-UI je arhitektura projekta koja obezbeđuje modularnost, olakšava održavanje i omogućava nezavisne izmene svakog sloja. 
### Data Access Layer (DAL)
DAL (Data Access Layer) sloj koji služi za manipulaciju podacima iz baze podataka. Na nivou DAL sloja definišemo sve funkcije koje su nam potrebne da manipulišemo podacima iz baze podataka - kreiranje, brisanje, ažuriranje i uzimanje podataka. Sem toga, možemo pisati i neke dodatne funkcije za traženje/filtriranje podataka. Primer funkcija na DAL nivou su prikazane ispod: 

```python 
from sqlalchemy.orm import Session
from models.user import User
from models.todo import Todo as TodoModel

def find_user_by_id(db:Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
 
def get_users(db: Session, skip:int=0, limit:int=100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: User) -> User:
    db_user = User(email=user.email, name=user.name, is_active=True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    if user.todos:
        todos = [TodoModel(title=todo.title, description=todo.description, owner_id=db_user.id) for todo in user.todos]
        db.add_all(todos)
        db.commit()

    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_for_delete: User) -> bool:
    db.delete(user_for_delete)
    db.commit()
    return True

def update_user(db: Session, user_id: int, updated_user: User) -> User | None:
    user = find_user_by_id(db, user_id)
    if not user:
        return None
    for key, value in updated_user.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user
```
### Bussiness Layer (DAL)
Ovaj sloj služi za implementiranje pravila poslovanja i funkcionalnosti aplikacije. Preuzima podatke od sloja iznad sebe - UI, a prosleđuje ih sloju ispod sebe - DAL. BL sloj je uglavnom sloj u kom su definisani servisi koji pozivaju DAL sloj i sprovode validaciju, transformaciju ili neku drugu logiku nad preuzetim podacima. 
Primer BL sloja: 
```python 

import DAL.users as db_service
import schemas.user as schemas
from sqlalchemy.orm import Session
from typing import Sequence


def get_users(db: Session, 
              skip:int=0, 
              limit:int=100) -> Sequence[schemas.User]:
    return db_service.get_users(db, skip, limit)

def find_user_by_id(db: Session, user_id: int) -> schemas.User:
    user = db_service.find_user_by_id(db, user_id)
    if user == None: 
        raise Exception(f"User with ID {user_id} not found")
    return user
    
def get_user_by_email(db: Session, 
                      user_email : str): 
    return db_service.get_user_by_email(db, user_email)

def create_user(db: Session, user: schemas.UserCreate):
    if (user.name == ''):
        raise Exception("User must have name!")
    if (user.email == ''): 
        raise Exception("User must have email!")
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise Exception("There has been already registrated user with this email")
    return db_service.create_user(db, user)
    #return db_service.create_user(db, user)

def delete_user(db: Session, user_id: int) -> schemas.User: 
    try:
        user_for_delete = find_user_by_id(db, user_id)
        deleted = db_service.delete_user(db, user_for_delete)
        if not deleted: 
            raise Exception(f"An error occurred. User with ID {user_id} has not been deleted")
        return deleted
    except Exception as e: 
        raise e
    
def update_user(db: Session, user_id: int, user_data: schemas.UserUpdate):
    try:
        if (user_data.name == ""):
            raise Exception("Name cannot be empty.")
        if (user_data.email == ""):
            raise Exception("Email cannot be empty.")
        updated_user = db_service.update_user(db, user_id, user_data.model_dump(exclude_unset=True))
        if not updated_user:
            raise Exception("User not found or update failed.")
        return updated_user
    except Exception as e:
        raise e
``` 


---

# Pydantic i Logfire
FastAPI koristi standardne Python tipove podataka (int, str, float...) za definisanje tipova u aplikaciji, pa je sam kod čitljiv i lako razumljiv. 
Zahvaljujući integraciji sa bibliotekom **Pydantic**, FastAPI pruža veoma korisne alate za jednostavnu validaciju i manipulaciju podacima. 
Tim koji je razvio Pydantic, kreirao je još jedan alat **Logfire** čija je namena monitoring aplikacija. Logfire je dizajniran tako da bude jednostavan, a ujedno i efikasan za upotrebu. Integrisan je sa mnogim popularnim bibliotekama (FastAPI, OpenAI, sam Pydantic i dr.) što omogućava njegovu upotrebu za praćenje validacija u Pydantic-u i jasnije razumevanje zašto neki unosi ne ispunjavaju uslove validacije. 
Primer jedne validacije korišćenjem Pydantic biblioteke: 

```python 
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator
from schemas.todo import Todo, TodoCreate
from typing import List, Optional

class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(min_length=3, max_length=50)
    
    model_config = ConfigDict(from_attributes=True)

    @field_validator("name")
    def name_validator(cls, name: str): 
        if not name.isalpha(): 
            raise ValueError("Name must contain only alphabetic characters!")
        return name
```
Primer nevalidnog unosa email adrese i odgovora servera: 
![nevalidan-mejl](./fast-api/resources/images/nevalidan-mejl.png)
![odgovor-servera](./fast-api/resources/images/odgovor-servera-nevalidan-mejl.png)

## 🎓 **Resursi za učenje**
- [FastAPI - Zvanična dokumentacija](https://fastapi.tiangolo.com)  
- [Primeri na GitHub-u](https://github.com/tiangolo/fastapi)  
- [GeeksForGeeks](https://www.geeksforgeeks.org/fastapi-introduction/)
- [Pydantic - Zvanična dokumentacija](https://docs.pydantic.dev/latest/)
- [SQLAlchemy - Zvanična dokumentacija](https://docs.sqlalchemy.org/en/20/orm/)

---