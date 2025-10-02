sentence = "hej"

for letter in sentence:
    print(letter)

for i in range(1, 10):
    if i == 5:
        continue

    print(i)

for i in range(10):
    print(i)


gambling = True

while gambling:
    print("$$$")

    if input() == "stop":
        break


while True: 
    print("mata in ett nummer")
    number_1 = input()
    try:
        number_1 = int(number_1)
    except:
        print("försök igen")
 


while True: 
    print("mata in ett nummer")
    number_1 = input()

try:
    number_1 = int(number_1)
except:
    print("försök igen")




word_1 = "Hassan"

if "a" in word_1:
    print("Ja, det finns")

else: print("Nej det finns inte")