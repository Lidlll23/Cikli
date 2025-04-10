stafsA=int(input("Kurā stāvā tu atrodies?"))
stafsJ=int(input("Uz kuru stāvu vēlies doties?"))


print(stafsA)
stafsJ=stafsA-(stafsA-stafsJ)

d1=stafsA-stafsJ
st=stafsA-1

while d1>=stafsJ:
    if st>=stafsJ:
        st2=stafsA-1
        print(st)
        print(st2)
    else:
        break

print(stafsJ)

print("STOP")
print("Tu esi ieradies izvēlētajā stāvā!")
