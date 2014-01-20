print "We are going to figure out if your triangle is a Pythagorean Triple.\n"
print "I will ask you to enter the three sides of your triangle, one at a time. You can enter them in any order.\n"
count = 1
while count == 1:
    a, b, c, = raw_input("Enter the length of the first side: "), raw_input("Enter the length of the second side: "), raw_input("Enter the length of the third side: ")
    a, b, c = int(a), int(b), int(c)

    if a > b and a > c:
    	side = b**2
    	side_two = c**2
    	largest = a**2      
    elif b > a and b > c:
        side = a**2
        side_two = c**2
        largest = b**2
    else:
        side = a**2
        side_two = b**2
        largest = c**2

    if side + side_two == largest:
    	print "You have a Pythagorean Triple!\n"
    else: 
        print "This is not a Pythagorean Triple\n"
