elso=int(input("Add meg az első számot: "))
masodik=int(input("Add meg a második számot: "))
harmadik=int(input("Add meg a harmadik számot: "))

if elso%2==0 and masodik%2==0 and harmadik%2==0:
    print("Mindhárom szám páros")
elif elso%2 !=0 and masodik%2 !=0 and harmadik%2 !=0:
    print("mindhárom szám páratlan")
else:
    print("Kevert számok")