# initialized matrix input vectors
matrix = [
	[0, 0, 1, 1],
	[1, 0, 0, 0],
	[0, 1, 1, 0],
	[0, 0, 0, 1]
]

weights = [
	[0.2, 0.4, 0.6, 0.8],
	[0.9, 0.7, 0.5, 0.3]
]

alpha = 0.5

for i in range(len(matrix)):
	win = []

	for j in range(len(weights)):
		sum = 0
		# print(matrix[1])
		for k in range(len(weights[j])):
			sum += (matrix[i][k] - weights[j][k])**2
			# print(sum)

		win.append(round(sum, 3))

	print(win)

	if (win[0] > win[1]):
		for j in range(0, 4):
			weights[1][j] = round(weights[1][j] + alpha * (matrix[i][j] - weights[1][j]), 3)
	else:
		for j in range(0, 4):
			weights[0][j] = round(weights[0][j] + alpha * (matrix[i][j] - weights[0][j]), 3)
	print(weights)