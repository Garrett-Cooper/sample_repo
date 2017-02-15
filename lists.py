bikes = ['trek', 'cannondale','redline','specialized']
print(bikes)

#caps the first bike in the list
print(bikes[0].upper())

print(bikes[-1].title())

print ("My first bike was a " + bikes[0].title() + ". \nNo it wasn't, it was a LeMond.")

message = "\nMy second bike was a " + bikes[-2].title() + \
    ". \nWhat?! You never even owned a " + bikes[-2].upper()

print (message)

#changing, adding and removing elements

#modifying elements in a list
bikes[0]='Giant'
print(bikes)

#append element to a list using the append method
bikes.append('LeMond')
print(bikes)

#create an empty list and append elements to it
cars = []
cars.append('Ford')
cars.append('Chevy')
cars.append('Buick')
cars.append('Toyota')
print(cars)

#insert an element using the insert method
cars.insert(0,'Kia')
print(cars)

#use the delete statement
del cars[2]
print(cars)

#we may want to remove an item from a list (ex: user name) and add it to another list. We can use the pop method
#to accomplish this function

popped_cars_list = cars.pop()
print(popped_cars_list)
print (cars)
message = "The first car in the list that is popped is a " + cars.pop(0) + "."
print (message)

#Use the remove method to delete an element / value
cars.remove("Ford")
print(cars)

friends = ['Bryan','Chris','Sean','Wes','Sam','Shane','Jeff']
#use the sort method to alphabetize the list // once the order is changed it can't be changed back
friends.sort()
print(friends)
#you can reverse the order of the list // this will permanently alter the list
friends.sort(reverse=True)
print(friends)
#sort a list temporarily with the sorted functions (not a method!!)
friends.append('Scott')
friends.append('Laura')
friends.append('Emily')
print(friends)
print(sorted(friends))

#we can print a list in reverse using the reverse method // permanently changes the order //
#revert back to the original order by doing another reverse method call
bikes.reverse()
print(bikes)
#use the len method to find the len
message = 'The bikes list has ' + str(len(bikes)) + ' elements in the list.'
print(message)
