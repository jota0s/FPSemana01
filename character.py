character1 = str(input("What is your character name? "))
Life1=int(input("Health? "))
Level1=int(input("Level? "))

character2 = str(input("What is your character name? "))
Life2=int(input("Health? "))
Level2=int(input("Level? "))

character3 = str(input("What is your character name? "))
Life3=int(input("Health ? "))
Level3=int(input("Level? "))


print(character1)
print(Life1)
print(Level1)

print(character2)
print(Life2)
print(Level2)

print(character3)
print(Life3)
print(Level3)

array=[
    [character1,(Life1,Level1)],
    [character2,(Life2,Level2)],
    [character3,(Life3,Level3)]
]

print(array)

def status_characterlvl(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j][1][1]<array[j+1][1][1]:
                array[j],array[j+1] = array[j+1], array[j]

status_characterlvl(array)

for i in array:
    print(i[0])
