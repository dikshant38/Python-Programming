#Write a Python program that takes a list of daily stock prices as input, and returns the best days to buy and sell stocks in order to maximize profit. The list contains the stock prices for each day, starting from the first day. For example, the list (100, 180, 260, 310, 40, 535, 695) represents the stock prices for 7 days, where the price on the first day is 100, the second day is 180, and so on. The program should find the best days to buy and sell stocks such that the profit obtained is maximum. For instance, in the given list of stock prices, the best days to buy and sell stocks would be: Buy stock on the 1st day (price=100) Sell stock on the 4th day (price=310) Buy stock on the 5th day (price=40) Sell stock on the 7th day (price=695) The program should output these buy and sell days as a tuple or list of integers. 

def find_best_days(prices): 
  min_price = float('inf') 
  max_profit = 0 
  buy_day = 0 
  sell_day = 0 

  for i in range(len(prices)): 
    if prices[i] < min_price: 
      min_price = prices[i] 
      buy_day = i 

    profit = prices[i] - min_price 
    if profit > max_profit: 
      max_profit = profit 
      sell_day = i 
   return (buy_day+1, sell_day+1) 

prices = [100, 180, 260, 310, 40, 535, 695] 
print(f"Prices on Each Date:") 
for i in range(0,len(prices)): 
  print("Price of Day",i+1,"is",prices[i]) 
best_days = find_best_days(prices) 
print(f"Buy on day {best_days[0]} and sell on day {best_days[1]}")
