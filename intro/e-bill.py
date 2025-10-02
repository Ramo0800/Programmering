import datetime

TAX = 1.25

def calculate_bill(start, end, power, cost, dayfare, tax):
    days = (end - start).days

    total = days * dayfare
    total += power * cost
    total *= tax

    return total


print("vilket startår är det?")
startyear = input()
startyear = int(startyear)

print("vilken startmånad är det?")
startmonth = input()
startmonth = int(startmonth)

print("vilken startdag är det?")
startday = input()
startday = int(startday)

start_date = datetime.datetime(startyear, startmonth, startday)

print("vilket slutdatår är det?")
endyear = input()
endyear = int(endyear)

print("vilken slutmånad är det?")
endmonth = input()
endmonth = int(endmonth)

print("vilken slutdag är det?")
endday = input()
endday = int(endday)

end_date = datetime.datetime(endyear, endmonth, endday)

print("hur mycket el har använts?")
power = input()
power = float(power)

print("hur mycket kostar elen?")
cost = input()
cost = float(cost)

print("vad är dagsavgiften?")
dayfare = input()
dayfare = float(dayfare)

price = calculate_bill(start_date, end_date, power, cost, dayfare, TAX)
print(f"kostnaden är {price} kr")