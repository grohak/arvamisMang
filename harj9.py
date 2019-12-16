punktid = 0
print("Mis värvi on taevas?")
vastus1 = input()
õige1 = "sinine"
if vastus1 == õige1:
    punktid += 1
print("Mitu jalga on koeral?")
vastus2 = input()
õige2 = "4"
if vastus2 == õige2:
    punktid +=1
print("Kes on USA president?")
print("1. Clinton")
print("2. Trump")
print("3. Obama")
vastus3 = input()
õige3 = "2"
if (vastus3 == õige3):
    punktid += 1

if (punktid == 3):
    print("tubli, kõik õige")
else:
    print("peaaegu, proovi uuesti")
