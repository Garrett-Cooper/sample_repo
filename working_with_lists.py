# list can be changed (mutable) --> use square brackes // tuples can't be changed (immutable) --> parentheses

import random

line_break = "\n"

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
print (line_break)

# print a series of numbers
for i in range(0,5):
    print(i)

# converts range of numbers to a list
numbers = list(range(0,5))
print(numbers)

# prints out list of numbers from 2-10 in increments of 2
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    sqr_number = value**2
    squares.append(sqr_number)
print(squares)

# a more compact way of writing the above program
squares2=[]
for value in range(1,11):
    squares2.append(value**2)
print(squares2)

rand_list =[]
rand_list = list(random.sample(range(1,100),10))

# Max, Min, Sum other operations don't change the list, so they are functions
print(rand_list)
print(max(rand_list))
print(min(rand_list))
print(sum(rand_list))

# using LIST COMPREHENSION = combines for loop + creation of new elements in 1 line and appends new elements
squares3 = [value**2 for value in random.sample(range(1,100),10)]
print(squares3)

# Slice = working with a specific group of items in a list
players = ['Sid', 'Phil','Tanger','Hornqvist','Sheary','Rust','Malkin','Bonino','Cullen','Schultz','Dumo','Cole','Hagelin','Murray','Fleury','Daley','Maata']
print(players[:3])
print(players[3:])

print(players[-3:])
print(players[:-3])

print ("Here are my favorite Pens: ")
for player in players:
    print(player.lower())

print("\n")
# how to copy a list
top_players = []
top_players = players[:3]
# append Malkin
top_players.append(players[6])
print(top_players)
print("\n")

# how to properly copy a list
all_time_players = top_players[:]
all_time_players.append("Lemieux, Francis, Jagr, Stevens")
print(all_time_players)
print(top_players)
print("\n")

## USING TUPLES --> you can't change a tuple like you can a list
dimensions = (10, 12)
print(dimensions[:])
print(dimensions[1])
print(dimensions[0])
print("\n")
dimensions = (50, 100,27,14,10)
for dim in dimensions:
    print(dim)

print("\n")
# if statement runs if a condition is True, run the indented block of code.
# if the condition is not true, skip the indented block and continue the program
age = 37
if age >= 21:
    print("You are old enough to drink alcohol.\n")

# if-else statement are ideal if you want to run a condition when true,
# and another condition when false
# that is, you want to run 1 of 2 conditions

age2 = 19
if age2 >= 21:
    print("You are old enough to drink alcohol\n.")
else:
    print("You are not old enough to drink.")
    print("The legal age is 21.\n")

# if testing more than 2 conditions, use the if-elif-else chain
# this conditional statement structure only runs 1 condition

age3 = 21
if age3 < 18:
    print("You're a youngster - have fun!\n")
elif age3 < 21:
# you can use a comma to continue strings on the next line
    print ("You're old enough to go to war, but not old enough to drink",
    "a beer.\n")
else:
    print ("You're old enough to go to war and drink a beer.\n")
