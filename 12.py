import re
with open('12.json', 'r') as f:
	json = f.read().strip()
	print(sum(map(int, re.findall(r'-?\d+', json))))
