DriverName = input("Enter driver name : ")
Distance = float(input("Enter distance (km): "))
FuelConsumption = float(input("Enter fuel consumption (L/100km): "))
Price = float(input("Enter fuel price (KZT/L): "))
litres_needed = (Distance * FuelConsumption) / 100
fuel_cost = litres_needed * Price
cost_per_km = fuel_cost / Distance
if Distance > 300:
    a = "True"
else:
    a = "False"
if fuel_cost > 5000:
    b = "True"
else:
    b = "False"
print("Driver :", DriverName)
print("Distance :", Distance, "km")
print("Consumption :", FuelConsumption, "L/100km")
print("Fuel price :", Price,  "KZT/L")
print("Litres needed :", litres_needed, "L")
print("Fuel cost :", fuel_cost, "KZT")
print("Cost per km :", cost_per_km, "KZT")
print("Trip longer than 300 km :", a )
print("Fuel cost above 5000 KZT :", b )