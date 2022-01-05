'''Sample Input 

G = 6.67 * 10-11

MEarth = 6.0 * 1024

mMoon = 7.34 * 1022

r = 3.84 * 108
GMm/r**2'''

G = 6.67 * (10 ** -11)
M = 6.0 * (10 ** 24)
m = 7.34 * (10 ** 22)
r = 3.84 * (10 ** 8)

calculated_gravity = G * M * m /r ** 2
print(calculated_gravity)

'''In this challenge, you must discount a price according to its value.

    If the price is 300 or above, there will be a 30% discount.

    If the price is between 200 and 300 (200 inclusive), there will be a 20% discount.

    If the price is between 100 and 200 (100 inclusive), there will be a 10% discount.

    If the price is less than 100, there will be a 5% discount.

    If the price is negative, there will be no discount.
'''

price = 250
if (price >= 300):
    discount = price * .30
    total = price - discount
elif (price < 300):
    discount = price * .20
    total = price - discount
elif (price <= 200):
    discount = price * .10
    total = price - discount
elif (price < 100):
    discount = price * .05
    total = price - discount
else:
    print(price)

print(total)

price = 250
if price >= 300:
    price *= 0.7  # (1 - 0.3)
elif price >= 200:
    price *= 0.8  # (1 - 0.2)
elif price >= 100:
    price *= 0.9  # (1 - 0.1)
elif price < 100 and price >= 0:
    price *= 0.95  # (1 - 0.05)
print(price)