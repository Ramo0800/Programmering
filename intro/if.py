print("Hur gammal är du?")

age = input()
age = int(age)

if age <18:
    print("Du är ett barn")

elif age == 18:
    print("du är 18")

elif age >=18 and age <50:
    print("du är vuxen")

elif age >= 50:
    print("du är gammal")

elif age != 72:
    print()

else:
    print("jag vet inte")