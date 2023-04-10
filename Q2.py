def find_trilogy_year(books): 
  years = sorted(set(books.values())) 

  for i in range(len(years)-2): 
    if (years[i+2] - years[i+1] == years[i+1] - years[i]) and \ any(years[i+1] == year for book, year in books.items() if years[i] <= year <= years[i+2]): 
      return years[i]
  return None 

books = {'The Hunger Games': 2008, 'Catching Fire': 2009, 'Mockingjay': 2010, 'The Lord of the Rings': 1954, \ 
'The Return of the King': 1956, 'Divergent': 2011, 'Insurgent':2012,'Allegiant':2013, 'The Two Towers':1955} trilogy_year = find_trilogy_year(books) print(f"The earliest year in which a trilogy was published is {trilogy_year}")
