class Pizza:
    def __init__(self, nazwa, rodzaj, cena):
        self.nazwa = nazwa;
        self.rodzaj = rodzaj;
        self.cena = cena;

    def pizzaInfo(self):
        print(f"Nazwa: {self.nazwa}, Rodzaj: {self.rodzaj}, Cena: {self.cena}");

# pizza1 = Pizza("Margherita", "Wegetariańska", 20);
# pizza1.pizzaInfo();
menu = [
    Pizza("Margherita", "Wegetariańska", 20),
    Pizza("Pepperoni", "Mięsna", 25),
    Pizza("Hawajska", "Słodka", 22)
]

# zasotowanie def, zeby return był mozliwy

def wybierzPizze():
    print("Menu pizz:");
    for i, pizza in enumerate(menu, start=1):
        print(f"{i}. {pizza.nazwa} - {pizza.rodzaj} - {pizza.cena} zł");

    wyborP = int(input("Wybierz pizzę (1-3): "));
    if wyborP < 1 or wyborP > 3:
        print("Nieprawidłowy wybór")
        return
#    return print(menu[wyborP - 1].nazwa);
    return menu[wyborP - 1];
class Dostawa:
    def __init__(self, rodzaj, odleglosc, cenaKm):
        self.rodzaj = rodzaj;
        self.odleglosc = odleglosc;
        self.cenaKm = cenaKm;
    
    def dostawaInfo(self):
        print(f"Rodzaj: {self.rodzaj}, Odległość: {self.odleglosc} km, Cena za km: {self.cenaKm} zł");

menuDostawa = [
    Dostawa("NaMiejscu", 0, 0),
    Dostawa("Dowóz", 0, 2),
    Dostawa("OdbiórOsobisty", 0, 0)
]
odlegloscI = 0;

def wyborDostawy():
    print("Menu dostaw:");
    for i, dostawa in enumerate(menuDostawa, start=1):
        print(f"{i}. {dostawa.rodzaj}");
    wyborD = int(input("Wybierz rodzaj dostawy (1-3):"));
    if wyborD < 1 or wyborD > 3:
        print("Nieprawidłowy wybór")
        return
    if wyborD == 2:
        odlegloscI = int(input("Podaj odległość dostawy w km: "));
        menuDostawa[wyborD - 1].odleglosc = odlegloscI;
    #return print(menuDostawa[wyborD - 1].rodzaj);
    return menuDostawa[wyborD - 1];


# odlegloscI = int(input("Podaj odległość dostawy w km: "));


#dostawa1 = Dostawa("NaMiejscu", 0, 0);
#dostawa1.dostawaInfo();

class Dodatki:
    def __init__(self, nazwa, ilosc, cena):
        self.nazwa = nazwa;
        self.ilosc = ilosc;
        self.cena = cena;

    def dodatkiInfo(self):
        print(f"Nazwa: {self.nazwa}, Ilość: {self.ilosc}, Cena: {self.cena} zł");

# dodatki1 = Dodatki("Ser", 0, 5);
menuDodatki = [
    Dodatki("Ser", 0, 5),
    Dodatki("Oliwki", 0, 3),
    Dodatki("Pieczarki", 0, 3),
]


def wybierzDodatki():
    DodatkiI = input("Czy chcesz dodać dodatki? (tak/nie): ");
    #sumaD = 0;
    if DodatkiI.lower() == "tak":
        while (1):
            print("Menu dodatków:");
            for i, dodatek in enumerate(menuDodatki, start=1):
                print(f"{i}. {dodatek.nazwa} - {dodatek.cena} zł");
            wyborD = int(input("Wybierz dodatek (1-3) lub 0, aby zakończyć:"));
            if wyborD == 0:
                break;
            if wyborD < 1 or wyborD > 3:
                print("Nieprawidłowy wybór");
                continue;
            menuDodatki[wyborD - 1].ilosc += 1;
        return menuDodatki;
    if DodatkiI.lower() == "nie":
        return 0;
    else:
        print("Nieprawidłowy wybór");
        return 0;

# dodatki1.dodatkiInfo();

class Zamowienie:
    def __init__(self, pizza: Pizza, dostawa: Dostawa, dodatki: Dodatki):
        self.pizza = pizza;
        self.dostawa = dostawa;
        self.dodatki = dodatki;
        # sumowanie ceny dodatków
        self.sumaD = sum(i.cena * i.ilosc for i in dodatki)
        self.suma = self.pizza.cena + self.dostawa.odleglosc * self.dostawa.cenaKm+self.sumaD;

    def zamowienieInfo(self):
        print("Zamówienie:");
        self.pizza.pizzaInfo();
        self.dostawa.dostawaInfo();
        #suma dodatków w pętli bo jest więcej obiektów na raz
        for i in self.dodatki:
            if i.ilosc > 0:
                i.dodatkiInfo();
        print(f"Suma: {self.suma} zł");

# Połączenie klas
zamowienie = Zamowienie(wybierzPizze(), wyborDostawy(), wybierzDodatki());
zamowienie.zamowienieInfo();
# zamowienie1 = Zamowienie(pizza1, dostawa1, dodatki1);
# zamowienie1.zamowienieInfo();