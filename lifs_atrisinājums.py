starts=int(input("Stāvs, kurā lifts atrodas:"))
finish=int(input("Stāvs, uz kuru jābrauc:"))

if starts<finish:
    virziens=1
else:
    virziens=-1

for i in range(starts,finish,virziens):
    print(i)
print(f"{finish} STOP")