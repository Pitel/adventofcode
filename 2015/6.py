lights = [[0 for i in range(1000)] for i in range(1000)]

def show():
	for row in lights:
		for light in row:
			if light:
				print('#', end='')
			else:
				print('.', end='')
		print()

with open('6.in', 'r') as f:
	#show()
	instructions = f.readlines()
	for instruction in instructions:
		#instruction = "turn on 0,0 through 2,2"
		instruction = tuple(instruction.strip().split())
		start = tuple(map(int, instruction[-3].split(',')))
		end = tuple(map(int, instruction[-1].split(',')))
		print(instruction, start, end)
		if instruction[0] == 'turn':
			for x in range(start[0], end[0] + 1):
				for y in range(start[1], end[1] + 1):
					if instruction[1] == 'on':
						lights[x][y] += 1
					else:
						lights[x][y] -= 1
						if lights[x][y] < 0: lights[x][y] = 0
					#show()
		elif instruction[0] == 'toggle':
			for x in range(start[0], end[0] + 1):
				for y in range(start[1], end[1] + 1):
					lights[x][y] += 2

	total = 0
	for row in lights:
		for light in row:
			total += light
	print(total)
