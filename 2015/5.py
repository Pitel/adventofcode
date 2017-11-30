#vowels = ('a', 'e', 'i', 'o', 'u')
#naughties = ('ab', 'cd', 'pq', 'xy')
nice = 0

with open('5.in', 'r') as f:
	words = f.readlines()
	for word in words:
		word = word.strip()
		#word = 'qjhvhtzzzqqjkmpb'
		print(word)
		prev = None
		prevprev = None
		#v = 0
		cond_double = False
		#cond_naughty = False
		cond_between = False
		for c in word:
			'''
			if c in vowels: v += 1
			if prev == c: cond_double = True
			if prev + c in naughties:
				cond_naughty = True
				break;
			'''
			if prevprev == c:
				print("Between", c)
				cond_between = True
			if prev != None:
				pair = prev + c
				without = word.replace(pair, pair.upper(), 1)
				if pair in without:
					print(pair, without)
					cond_double = True
			prevprev = prev
			prev = c
		print(word, cond_between, cond_double)
		#if v >= 3 and cond_double and not(cond_naughty): nice += 1
		if cond_between and cond_double: nice += 1

print(nice)
