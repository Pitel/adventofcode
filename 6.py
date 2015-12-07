lights = [[False for i in range(1000)] for i in range(1000)]

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
					#print(x, y)
					lights[x][y] = instruction[1] == 'on'
					#show()
		elif instruction[0] == 'toggle':
			for x in range(start[0], end[0] + 1):
				for y in range(start[1], end[1] + 1):
					lights[x][y] = not(lights[x][y])

	i = 0
	for row in lights:
		for light in row:
			if light: i += 1
	print(i)
