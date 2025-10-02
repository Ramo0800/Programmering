glass = 20
varmkorv = 15
läsk = 15
godis = 10
print("vi säljer glass, varmkorv, läsk och godis")
print("vad vill du ha?")
item = input()
print(item, "hur många?")
amount = input()
amount = int(amount)

if item == "glass":
    print("det blir", amount * glass, "kr")

elif item == "varmkorv":
    print("det blir", amount * varmkorv, "kr")

elif item == "läsk":
    print("det blir", amount * läsk, "kr")

elif item == "godis":
    print("det blir", amount * godis, "kr")
