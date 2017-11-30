with open("3.in", "r") as f:
	directions = f.read()
	houses = {}
	santa = [0, 0]
	robo = [0, 0]
	roboturn = False

	for d in directions:
		if roboturn:
			if d == ">":
				robo[0] += 1
			elif d == "<":
				robo[0] -= 1
			elif d == "^":
				robo[1] += 1
			elif d == "v":
				robo[1] -= 1
			if not(robo[0] in houses): houses[robo[0]] = {}
			if not(robo[1] in houses[robo[0]]): houses[robo[0]][robo[1]] = 0
			houses[robo[0]][robo[1]] += 1
		else:
			if d == ">":
				santa[0] += 1
			elif d == "<":
				santa[0] -= 1
			elif d == "^":
				santa[1] += 1
			elif d == "v":
				santa[1] -= 1
			if not(santa[0] in houses): houses[santa[0]] = {}
			if not(santa[1] in houses[santa[0]]): houses[santa[0]][santa[1]] = 0
			houses[santa[0]][santa[1]] += 1
		roboturn = not(roboturn)

	atleast1 = 0
	for x in houses:
		for y in houses[x]:
			print(x, y, houses[x][y])
			atleast1 += 1
	print(atleast1)

