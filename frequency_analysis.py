def freq_analysis(message):
	# define list alphabet, it help find posion in freq_list
	abc = "abcdefghijklmnopqrstuvwxyz"
	freq_list = []
	# initialize frequency alphabet
	lenght = len(message) * 1.0
	i = 0
	while (i < 26):
		char = abc[i]
		# x is frequency for freq_list, if not search alphabet, it'll return frequency   
		x = message.count(char) / lenght
		freq_list.append(x)
		i += 1
	return freq_list
print freq_analysis("abcd")
#GG