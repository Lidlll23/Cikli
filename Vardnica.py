vardnica={"go":"Uz priekšu, doties, iet.", "apple":"ābols", "a prankster":"blēņdaris"}
#Vādbnīcas struktūra - {"atslēgas vārds":"skaidrojums","atslēgas vārds":"skaidrojums"}

x=input("Ievadi tulkojamo vārdu:")
#x ievada vārdnīcas atslēgvārdu

print(f"{x} - {vardnica[x]}")
#vardnica[x] - izsaus no vārdnīcas skaidrojumu izmantojot atslēgas vārdu.

izvele="jā"
while izvele=="jā":
    x=input("Ievadi tulkojamo vārdu:")
    print(f"{x} - {vardnica[x]}")
    izvele=input("Ja vēlies turpināt ievadi - jā")
    