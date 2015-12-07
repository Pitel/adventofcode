vowels = ("a", "e", "i", "o", "u")
naughties = ("ab", "cd", "pq", "xy")
nice = 0

with open("5.in", "r") as f:
	words = f.readlines()
	for word in words:
		prev = ""
		v = 0
		cond_double = False
		cond_naughty = False
		for c in word:
			if c in vowels: v += 1
			if prev == c: cond_double = True
			if prev + c in naughties:
				cond_naughty = True
				break;
			prev = c
		print(word)
		if v >= 3 and cond_double and not(cond_naughty): nice += 1

print(nice)
