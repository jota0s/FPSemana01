name1 = (input(""))
Ataque1 = int(input (""))
Defesa1 = int(input (""))

name2 =  (input(""))
Ataque2 = int(input (""))
Defesa2 = int(input (""))

name3 =  (input(""))
Ataque3 = int(input (""))
Defesa3 = int(input (""))

array = [[name1,(Ataque1, Defesa1)], [name2, (Ataque2, Defesa2)], [name3, (Ataque3, Defesa3)]]

print (array)

Maior_ataque = array[0]
Maior_defesa = array[0]

for name, (Ataque, Defesa) in array :
    if Ataque > Maior_ataque[1][0]:
        Maior_ataque = [name, (Ataque, Defesa)]

    if Defesa > Maior_defesa[1][1]:
        Maior_defesa = [name, (Ataque, Defesa)]

print(f"Ataque {Maior_ataque[0]} {Maior_ataque[1][0]}")
print(f"Defesa {Maior_defesa[0]} {Maior_defesa[1][1]}")



