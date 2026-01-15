class Diak:
    def __init__(self, nev, eletkor, jegyek):
        self.nev = nev
        self.eletkor = eletkor
        self.jegyek = jegyek

    def atlag(self):
        if len(self.jegyek) == 0:
            return 0
        return sum(self.jegyek) / len(self.jegyek)

    def bemutatkozas(self):
        print(f"Szia, {self.nev} vagyok, {self.eletkor} éves.")

    def szinten(self):
        atlag = self.atlag()
        if atlag >= 4.5:
            return "Jó"
        elif atlag >= 3.0:
            return "Közepes"
        else:
            return "Gyenge"


# -------------------------
# Interaktív rész

nev = input("Add meg a diák nevét: ")
eletkor = int(input("Add meg a diák életkorát: "))

# Jegyek bekérése: vesszővel elválasztva
jegyek_input = input("Add meg a jegyeket, vesszővel elválasztva (pl. 5,4,3): ")
jegyek = [int(j.strip()) for j in jegyek_input.split(",") if j.strip().isdigit()]

# Diák létrehozása
diak = Diak(nev, eletkor, jegyek)

# Eredmények
diak.bemutatkozas()
print("Átlag:", diak.atlag())
print("Szint:", diak.szinten())
