# dictionaries contain key-value pairs (ex: color / green)
alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

print("\n")

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

## adding new key-value pairs
alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0)

print("\n")

# starting with an empty dictionary

alien_1 = {}

alien_1["color"] = "green"
alien_1["points"] = 5

print(alien_1)
print("\n")

#modifying a value of an existing key-value pair
alien_1["color"] = "yellow"
print(alien_1)

alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# move the alien to the right.
# determine how far to move the alien based on its current speed.
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

# the new position is the old position plus the new increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

print("\n")
# the alien moving at a different speed
alien_0['speed'] = 'fast'
print(alien_0)

print("Original x-position: " + str(alien_0['x_position']))

# move the alien to the right.
# determine how far to move the alien based on its current speed.
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

# the new position is the old position plus the new increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

print("\n")
# delete a key-value pair using the 'del' statement
print(alien_0)
del alien_0['y_position']
print(alien_0)

print("\n")

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

# use + sign to break up long print statements
print("Sarah's favorite language is " +
    favorite_languages["sarah"].title() +
    ".")

#### LOOPING THROUGH DICTIONARIES ####
user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last': 'fermi',
}

# loop
# items() is a method -> it returns a list of key-value pairs

for key, value in user_0.items():
    print("\nKey: " + key)
    print("\nValue: " + value)

print("\n")
# print out the key and values for the language dictionary
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print("\n")
# looping through keys

for name in favorite_languages.keys():
    print(name.title())

print("\n")

# the default behavior is to use keys(), so you can omit it if you want
for name in favorite_languages:
    print(name.title())

print("\n")

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

# list
friends = ['phil','sarah']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print (" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")

# you can use the keys method to look up a particular key (ex: 'erin')
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
