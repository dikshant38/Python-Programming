#Write a Python program that reads in a CSV file of stock prices (e.g. ticker symbol, date, price), and then uses dictionaries and lists to calculate the highest and lowest prices for each stock 

import csv 
with open('3_csv.csv') as file: 
  reader = csv.reader(file) 
  next(reader) # Skip the header row 
  prices = {} # Create an empty dictionary to store the prices for each stock 

for row in reader: 
  # Extract the symbol, date, and price from the row 
  ticker, date, price = row 

  # Convert the price from a string to a float 
  price = float(price) 

  # Check if the ticker symbol is already in the dictionary 
  if ticker in prices: 
    prices[ticker].append(price) 
  else: 
    prices[ticker] = [price] 

for ticker, price_list in prices.items(): 
  highest_price = max(price_list) 
  lowest_price = min(price_list) 
  print(f"{ticker}: Highest Price = ${highest_price:.2f}, Lowest Price = ${lowest_price:.2f}")

