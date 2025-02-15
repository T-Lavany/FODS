prices = [10, 20, 30]
quantities = [2, 1, 3]
discount_rate = 10  
tax_rate = 5  

subtotal = sum(p * q for p, q in zip(prices, quantities))
discount = subtotal * (discount_rate / 100)
tax = (subtotal - discount) * (tax_rate / 100)
total_cost = subtotal - discount + tax

print(total_cost)
