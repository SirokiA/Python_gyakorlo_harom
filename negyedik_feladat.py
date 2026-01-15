mondat = input("Adj meg egy mondatot: ")
maganhangzok = "aáeéiíoóöőuúüű"
szamlalo = {}
for karakter in mondat:
    if karakter in maganhangzok:
        if karakter in szamlalo:
            szamlalo[karakter] += 1
        else:
            szamlalo[karakter] = 1

ossz = sum(szamlalo.values())

print(f"Összes magánhangzó: {ossz}")
print("Magánhangzónkénti megjelenés:")
for betu, db in szamlalo.items():
    print(f"{betu}: {db}")