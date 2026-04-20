print("hello world");

class Pizza:
    def __init__(self, nazwa, rodzaj, cena):
        self.nazwa = nazwa;
        self.rodzaj = rodzaj;
        self.cena = cena;

    def pizzaInfo(self):
        print(f"Nazwa: {self.nazwa}, Rodzaj: {self.rodzaj}, Cena: {self.cena}");

pizza1 = Pizza("Margherita", "Wegetariańska", 20);
pizza1.pizzaInfo();

class Dostawa:
    def __init__(self, rodzaj, odleglosc, cenaKm):
        self.rodzaj = rodzaj;
        self.odleglosc = odleglosc;
        self.cenaKm = cenaKm;
    
    def dostawaInfo(self):
        print(f"Rodzaj: {self.rodzaj}, Odległość: {self.odleglosc} km, Cena za km: {self.cenaKm} zł");

dostawa1 = Dostawa("NaMiejscu", 0, 0);
dostawa1.dostawaInfo();


class Dodatki:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa;
        self.cena = cena;

    def dodatkiInfo(self):
        print(f"Nazwa: {self.nazwa}, Cemna: {self.cena} zł");

dodatki1 = Dodatki("Ser", 5);
dodatki1.dodatkiInfo();