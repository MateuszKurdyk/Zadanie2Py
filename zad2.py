print("hello world");

class Pizza:
    def __init__(self, nazwa, rodzaj, cena):
        self.nazwa = nazwa;
        self.rodzaj = rodzaj;
        self.cena = cena;

    def info(self):
        print(f"Nazwa: {self.nazwa}, Rodzaj: {self.rodzaj}, Cena: {self.cena}");

pizza1 = Pizza("Margherita", "Wegetariańska", 20);
pizza1.info();

# class Dostawa:



# class Dodatki:


