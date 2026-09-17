def make_change(amount_paid, amount_owed):
  """
  amount paid and amount owed -> change or remaining balance as a dictionary
  make_change takes in the amount paid and amount owed and returns 
  either the change as a dictionary or the remaining balance

  >>> make_change(1.90, 3.42)
  "After this payment, your total due is $1.52."
  >>> make_change(3.50, 1.92)
  {"1 dollar": 1, "quarter": 1, "nickel": 1, "penny": 3}
  >>> make_change(10.50, 1.92)
  {"5 dollar": 1, "1 dollar": 3, "quarter": 1, "nickel": 1, "penny": 3}
  """
  change = amount_paid - amount_owed

  if change < 0:
    balance = -change
    return f"After this payment, your total due is ${balance:.2f}."

change = round(change*100)

five_dollars = change // 500
change = change % 500

one_dollar = change // 100
change = change % 100

quarters = change // 25
change = change % 25

nickels = change // 5
change = change % 5

pennies = change

result = {}

if five_dollars > 0:
  result["5 dollars"] = five_dollars

if one_dollar > 0:
  result["1 dollar"] = one_dollar

if quarters > 0:
  result["quarter"] = quarters

if nickels > 0:
  result["nickel"] = nickels

if pennies > 0:
  result["penny"] = pennies

return result
  
