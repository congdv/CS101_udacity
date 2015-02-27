def split_string(source, splitlist):
	output = []
	atsplit = True
	for char in source:
		if char in splitlist:
			atsplit = True
		else:
			if atsplit:
				output.append(char)
				atsplit = False
			else:
				#print output[-1]
				output[-1] = output[-1] + char
	return output
out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
print out[-1]
out = split_string("After  the flood   ...  all the colors came out.", " .")
print out