mapa = {}

with open('9.in', 'r') as f:
	distances = f.readlines()
	for distance in distances:
		words = distance.strip().split()
		print(words)
		if not(words[0] in mapa): mapa[words[0]] = {}
		if not(words[2] in mapa): mapa[words[2]] = {}
		mapa[words[0]][words[2]] = int(words[-1])
		mapa[words[2]][words[0]] = int(words[-1])

shortest = 9999999999999999999999999999999999999999999

for start, ends in mapa.items():
	for city, distance in ends.items():
		print(start, city, distance)

from itertools import permutations

for path in permutations(mapa.keys()):
	prev = None
	cost = 0
	for city in path:
		if prev != None:
			cost += mapa[city][prev]
		prev = city
	print(path, cost)
	if cost < shortest: shortest = cost

print(shortest)
