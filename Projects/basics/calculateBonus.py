sales = float(input("Enter monthly sales: "))
bonus = 0.1 * sales if sales > 50000 else 0
print("Bonus:", bonus)
