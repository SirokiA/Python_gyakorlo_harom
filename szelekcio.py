szam = int(input("Adj meg egy egész számot: "))

if szam == 0:
    print("nulla")
elif szam > 0 and szam % 2 == 0:
    print("pozitív páros")
elif szam > 0 and szam % 2 != 0:
    print("pozitív páratlan")
elif szam < 0 and szam % 2 == 0:
    print("negatív páros")
else:
    print("negatív páratlan")
