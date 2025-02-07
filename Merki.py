while True:
    izvele1=input("vaivēlēsies atkārtoti lietot šo programmu? (jā,nē)")
    if izvele1=="jā":
        izvele=input("Vai vēlies nosaukt savu mērķi, vai nolasīt pēdējos ievadītos? (mērķi,ievadītos)")

        if izvele=="mērķi":
            f=open("informacija.text","a")
            # "a" - datu pievienošana
            f.write(input("Uzraksti mērķi, kuru vēlies sasniegt:"))
            f.write("\n")
            f.close()

        else:
            f=open("informacija.text","r")
            # "r" - read = nolasīt
            print(f.read())
    else:
        break