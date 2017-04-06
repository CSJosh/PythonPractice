import thread


def printA():
	count = 0;

	while count < 500000:
		if count % 1000 == 0:
			print "================================="
		print "A"
		count += 1


def printB():
	count = 0;

	while count < 500000:
		if count % 1000 == 0:
			printSep()

		print "B"
		count += 1


def printSep():
	print "************************************"




if __name__ == "__main__":
	thread.start_new_thread(printA, ())
	#thread.start_new_thread(printB, ())
	printB()
