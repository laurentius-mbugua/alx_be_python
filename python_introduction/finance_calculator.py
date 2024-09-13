income = int(input("Enter your monthly income: "))
monthly_expense=int(input("Enter your total monthly expenses: "))
monthly_savings= income - monthly_expense
projected_saving= monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings is", monthly_savings)
print("Projected saving after one year , with interest, is :", projected_saving)