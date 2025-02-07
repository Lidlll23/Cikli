augli=[]
#Tukši saraksti =[]
svars=[]

izvele="jā"

while izvele=="jā":
    augli.append(input("Sarakstam pievieno augļa nosaukumu:"))
    svars.append(input("Ievadi piegādātās preces svaru (kg):"))
    #append - pievienošanas komanda sarakstam.

    izvele=input("Vai vēlies turpināt ievadīt piegādāto preci? (jā vai nē):")

print(augli)
print(svars)