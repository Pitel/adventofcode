number = '3113322113'

for i in range(50):
	#print(number)
	prev = number[0]
	count = 0
	out = ""
	for letter in number:
		#print(prev, letter)
		if letter == prev:
			count += 1
			#print("Same", letter, "Count is", count)
		else:
			out += str(count)
			out += prev
			#print(count, "occurences of", prev)
			count = 1
		prev = letter
	out += str(count)
	out += prev
	number = out

print(len(number))
