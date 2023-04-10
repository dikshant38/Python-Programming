#a) Write a Python program to remove duplicates from a list of lists. Sample list: [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40] 

# Define the list of lists with duplicates 
list_of_lists = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]] 

# Create an empty set to store the unique lists 
unique_lists = set() 

# Loop through each list in the original list of lists 
for lst in list_of_lists: 
  # Convert the list to a tuple (because lists are not hashable, but tuples are) 
  lst_tuple = tuple(lst) 
  # Add the tuple to the set of unique tuples 
  unique_lists.add(lst_tuple) 

# Convert the set of unique tuples back to a list of lists 
unique_list_of_lists = [list(lst_tuple) for lst_tuple in unique_lists] 

# Print the original list of lists and the unique list of lists 
print("Original List of Lists:") 
print(list_of_lists) 
print("Unique List of Lists:") 
print(unique_list_of_lists)

#b)Write a Python program which takes a list and returns a list with the elements "shifted left by one position" so [1, 2, 3] yields [2, 3, 1]. Example: [1, 2, 3] → [2, 3, 1] [11, 12, 13] → [12, 13, 11]

def shift_left(lst): 
  # Check if the list is empty or has only one element 
  if len(lst) <= 1: 
    return lst 

  # Shift the elements of the list to the left by one position 
  shifted_lst = lst[1:] + [lst[0]] 
  # Return the shifted list 
  return shifted_lst 

list1 = [1,2,3] 
print(shift_left(list1))

#c)Iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element. Original list [11, 45, 8, 11, 23, 45, 23, 45, 89, 11, 89] And expected output is: Printing count of each item {11: 3, 45: 3, 8: 1, 23: 2, 89: 2}

def count_occurrences(lst):
  # Create an empty dictionary to store the count of each element 
  count_dict = {} 
  # Loop through each element in the list 
  for elem in lst: 
    # If the element is already in the dictionary, increment its count 
    if elem in count_dict: 
      count_dict[elem] += 1 
    # Otherwise, add the element to the dictionary with a count of 1 
    else: 
      count_dict[elem] = 1 
   # Return the dictionary of element counts 
    return count_dict 

list1 =[11, 45, 8, 11, 23, 45, 23, 45, 89, 11, 89] 
print(count_occurrences(list1))
