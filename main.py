# Welcome! 
print('Reseller Calculator v0.01 - Currently supporting StockX (USD)')
user1 = input('Are you selling on StockX or Goat? ').lower()

# Breaks into either StockX or Goat
if (user1 == "stockx"):
  item_val = int(input('What is the value of the item you are selling? '))
  seller_lvl = int(input('What is your StockX Seller Level (1-4)? (Only input the number, ex. 3) '))

#StockX Seller Levels
  L1 = .095
  L2 = .09
  L3 = .085
  L4 = .08

#Other StockX Fees
  processing = .03

#Getting Seller Level from User Input
  if seller_lvl == 1:
      total1 = item_val - (item_val*L1) - (item_val*processing)
      rounded1 = str(round(total1, 2))
      print('After fees, you will receive $'+rounded1+'.')
  elif seller_lvl == 2:
      total2 = item_val - (item_val*L2) - (item_val*processing)
      rounded2 = str(round(total2, 2))
      print('After fees, you will receive $'+rounded2+'.')
  elif seller_lvl == 3:
      total3 = item_val - (item_val*L3) - (item_val*processing)
      rounded3 = str(round(total3, 2))
      print('After fees, you will receive $'+rounded3+'.')
  elif seller_lvl == 4:
      total4 = item_val - (item_val*L4) - (item_val*processing)
      rounded4 = str(round(total4, 2))
      print('After fees, you will receive $'+rounded4+'.')
  else: 
      print('Error, try again.')

