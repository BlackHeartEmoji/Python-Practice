toppings = ['pepperoni','sausage','cheese','peppers']
total = []

print "Hey, let's make a pizza"

item = raw_input("What topping would you like on your pizza? ")
if item in toppings:
    print "Yes we have " + item
    total.append(item)
else:
    print "Sorry we don't have " + item
itemtwo = raw_input("give me another topping? ")
if itemtwo in toppings:
    print "Yes we have " + itemtwo
    total.append(itemtwo)
else:
    print "Sorry we don't have " + itemtwo
print "Here are your toppings "
print total