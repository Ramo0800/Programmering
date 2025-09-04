print("hur gammal är du?")

age = input()
age = int(age)

if age <7:
    print("det kostar 21 kr")

elif age >6 and age <20:
    print("Det kostar 21 kr")

elif age >20 and age <65:
    print("Det kostar 32 kr")

elif age >65:
    print("Det kostar 21 kr")