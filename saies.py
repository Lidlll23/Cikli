Speletajavards=input("Iavadi savu vārdu: ")
print(Speletajavards)
Speletajavards=Speletajavards.lower()
# Mainīgais.lower() - konvertē visus burtus par mazajiem simboliem.
Speletajavards=Speletajavards.capitalize()
# Mainīgais.capitalize() - konvertē simbolu virknē pirmo burtu par lielo.
print(Speletajavards)

vards1="čība"
burtuSK=len(vards1)
# len - saskaita virknē simbolu skaitu.
minejums=input(f"Uzraksti vārdu pareizi - {vards1[3]}{vards1[0]}{vards1[2]}{vards1[1]}")
# Mainīgais[burta pozīcija] - simbolu virkne sākasn ar indeksu - 0.
minejums=minejums.lower()
if minejums==vards1:
    print("Ūzminēji vārdu!")
else:
    print("Neuzminēji vārdu!")
