# Welcome! 
print("Reseller Calculator v0.01 - Currently supporting StockX (USD) ")
user_one = input("Are you selling on StockX or Goat? ").lower()

# Breaks into either StockX or Goat
if (user_one == "stockx"):
  item_val = int(input("What is the value of the item you are selling? "))
  seller_lvl = int(input("What is your StockX Seller Level (1-4)? (Only input the number, ex. 3) "))

#StockX Seller Levels
  lvl_one = 0.095
  lvl_two = 0.09
  lvl_three = 0.085
  lvl_four = 0.08

# Other StockX Fees
  processing = 0.03

# Getting Seller Level from User Input
  if seller_lvl == 1:
      total_one = item_val - (item_val * lvl_one) - (item_val * processing)
      rounded_one = str(round(total_one, 2))
      print("After fees, you will receive $" + rounded_one + ".")
  elif seller_lvl == 2:
      total_two = item_val - (item_val * lvl_two) - (item_val * processing)
      rounded_two = str(round(total_two, 2))
      print("After fees, you will receive $" + rounded_two + ".")
  elif seller_lvl == 3:
      total_three = item_val - (item_val * lvl_three) - (item_val * processing)
      rounded_three = str(round(total_three, 2))
      print("After fees, you will receive $" + rounded_three + ".")
  elif seller_lvl == 4:
      total_four = item_val - (item_val * lvl_four) - (item_val * processing)
      rounded_four = str(round(total_four, 2))
      print("After fees, you will receive $" + rounded_four + ".")
  else: 
      print("Error, try again.")
