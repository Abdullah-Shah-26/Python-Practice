# format specifiers = {value : flags} format a value based on what flags are inserted

price1 = 3000.14255253
price2 = 359.958403750

print(f"price1 is ${price1 : .2f}")
print(f"price2 is ${price2 : .1f}")

print(f"price1 is ${price1 : >10}")
print(f"price2 is ${price2 : <10}")
