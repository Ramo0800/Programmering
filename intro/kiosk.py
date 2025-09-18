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
    print("det blir", amount * glass)

elif item == varmkorv:
    print("det blir", amount * varmkorv)

elif item == läsk:
    print("det blir", amount * läsk)
glass = input()
glass = int(glass)
varmkorv = input()
varmkorv = int(varmkorv)
läsk = input()
läsk = int(läsk)
godis = input()
godis = int(godis)
