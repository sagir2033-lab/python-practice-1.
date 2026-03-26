CustomerName = input('Enter customer name :')
ProductName = input('Enter product name :') 
price = float(input('Enter price per unit :'))
Quantity = int(input('Enter quantity :'))
subtotal = price * Quantity
if subtotal > 5000:
    discount = subtotal * 0.1
else:
    discount = 0
total = subtotal - discount
print('Subtotal :', subtotal)
print('Discount :', discount)
print('Total :', total)
print('Discount applied :', subtotal > 5000)
print('Paid more than 3000 :', subtotal > 3000)
