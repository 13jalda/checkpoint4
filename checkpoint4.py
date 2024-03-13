# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
from decimal import Decimal

# variables
l_animals = ["lion", "tiger", "elephant"]
t_animals = ("dog", "cat", "bird")
marks = 7.1
members = 40
d_marks = Decimal(7.1)

teams = {
  "ath": ["Simon", "Vivian", "Williams"],
  "bcn": ["Puyol", "Pique"],
  "rmd": ["Casillas", "Figo","Ramos"],
  "atl": ["Simeone", "Morata"],
}
# Exercise 2: Round your float up.
import math

round_marks = (math.ceil(marks))
print(round_marks)

# Exercise 3: Get the square root of your float.
print(math.sqrt(marks))

# Exercise 4: Select the first element from your dictionary.
first_element = teams['ath']
print(first_element) # 1er elemento del diccionario
print(first_element[0]) # 1er elemento de la lista del diccionario

# Exercise 5: Select the second element from your tuple.
second_element = t_animals[1]
print(second_element)

# Exercise 6: Add an element to the end of your list.
l_animals.append("bear")
print(l_animals)

# Exercise 7: Replace the first element in your list.
l_animals[0] = "monkey"
print(l_animals)

# Exercise 8: Sort your list alphabetically.
l_animals.sort()
print(l_animals)

# Exercise 9: Use reassignment to add an element to your tuple.
t_animals += ("hamster",)
print(t_animals)