guests = ['Gore Vidal','Maya Angelou','Charlie Rose','David Axelrod','Samuel V. Cooper']

for guest in guests:
    invite = "Dear "+guest+ ", I would like to invite you to dine with my wife, Emily \n" + \
        "\tand me on Saturday, February 11, 2017. Please let me know if you are able to join?\n"
    print(invite)

print("Mr. "+guests.pop()+" sends his regrets. Who should we invite in his place?")

print ("Let's invite Thomas Jefferson.\n")

guests.append('Thomas Jefferson')
