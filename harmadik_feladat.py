n = int(input("Adj meg egy egész számot: "))

szamok = list(range(1, n+1))

osszeg = 0
oszthato_harommal = []

for szam in szamok:
    if szam %3==0:
        oszthato_harommal.append(szam)
        osszeg += szam

print("A számok amik oszthatóak hárommal: ", oszthato_harommal)
print("Ezek összege: ", osszeg)