with open("2.in", "r") as f:
	presents = f.readlines()
	paper = 0
	ribbon = 0
	for present in presents:
		edges = sorted(map(int, present.strip().split("x")))
		print(edges)
		paper += 2 * (edges[0] * edges[1] + edges[1] * edges[2] + edges[0] * edges[2]) + edges[0] * edges[1]
		ribbon += edges[0] + edges[0] + edges[1] + edges[1] + edges[0] * edges[1] * edges[2]
	print(paper, ribbon)
