DriverName = input("Enter driver name : ")
Destination = input("Enter destination : ")
distance = float(input("Enter distance (km) : "))
FuelConsumption = float(input("Enter fuel consumption (L/100km): "))
Price = float(input("Enter fuel price (KZT/L): "))
Destination1 = Destination.lower()
if distance < 100:
    Distance = "Short trip"
elif 100 <= distance < 500:
    Distance = "Medium trip"
else:
    Distance = "Long trip"
cost = (distance / 100) * Price * FuelConsumption

print("Driver :", DriverName)
print("Destination :", Destination.upper())
print("Distance :", distance, "km")
print("Fuel cost :", cost, "KZT")
print("Category :", Distance)
print(" ")
print("Cost breakdown:")
for i in range(100, int(distance) + 1, 100):
    a = (i / 100) * Price * FuelConsumption
    print(i, "km →", a)
print(" ")
print("Destination uppercase :", Destination.upper())
print("Destination lowercase :", Destination.lower())
print("Length :", len(Destination))
print("Letter 'a' count :", Destination1.count("a"))