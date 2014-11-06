def fizz_buzz():
	x = 0
	while x < 100:
		x += 1
		if x % 3 == 0 and x % 5 == 0:
			print "Fizz Buzz"
		elif x % 3 == 0:
			print "Fizz"
		elif x % 5 == 0:
			print "Buzz"
		else:
			print x

fizz_buzz()