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

# a smarter way to program conditional statements
# do the computation in the conditional statements, then
# use a print statement at the end to output the price amount
age4 = 12
if age4 < 4:
    price = 0
elif age4 < 18:
    price = 5
else:
    price = 10

print ("Your admission cost is $" + str(price) + ".\n")

#
age5 = 64
if age5 < 4:
    price = 0
elif age5 < 18:
    price = 5
elif age5 < 65:
    price = 10
#you could use an 'else' statement; however, you may not want to have a
#catch all statement at the end. Plus, using a final 'elif' statement
#makes it clearer what are the conditions you are checking for
elif age5 >= 65:
    price = 5

print ("Your admission cost is $" + str(price) + ".\n")

# testing multiple conditions
# in this case we are testing 3 individiual tests:

requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print ("\nFinished making your pizza!\n")

#### THIS WILL NOT WORK ####
# Python does not run any additional tests once one of the tests
# passes in the if-elif-else chain

requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print ("\nFinished making your pizza!]\n")

#Using if statements with lists && checking for special items
requested_toppings = ['mushrooms','green peppers','extra cheese']

for topping in requested_toppings:
    if topping == 'green peppers':
        print ("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + topping + ".")

print("\nFinished making your pizza!\n")

# checking that a list is not empty
# if the list is empty it will not pass the first if-statement
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print ("Adding " + requested_topping + ".")
        print ("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?\n")

# using multiple lists
available_toppings = ['mushrooms','green peppers','extra cheese','olives',
'pepperoni','pineapple']
requested_toppings = ['mushrooms','french fries','extra cheese']
# to test logic below
#requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print ("Adding " + requested_topping + ".")
        else:
            print ("We do not carry " + requested_topping + ".")
    print ("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
