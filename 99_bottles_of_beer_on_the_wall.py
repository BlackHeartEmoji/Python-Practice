x = 99

while x >= 1:
	x -= 1
	if x == 1:
		print x, "bottle of beer on the wall,", x, "bottle of beer!"
		print "Take one down, pass it around!",  x, "bottle of beer on the wall!\n"
	
	elif x == 0:
		print "No more bottles of beer on the wall!"
	else:
		print x, "bottles of beer on the wall,", x, "bottles of beer!"
		print "Take one down, pass it around!",  x, "bottles of beer on the wall!\n"
	
