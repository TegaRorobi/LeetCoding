
def spiralOrder(matrix: list[list[int]]) -> list[int]:
	return [*matrix[0]] + spiralOrder([*zip(*matrix[1:])][::-1]) if len(matrix) >=1 else []

def spiralOrder2(matrix: list[list[int]]) -> list[int]:
	if len(matrix) == 0:
		return []
	transposed = list(zip(*matrix[1:]))[::-1]
	return [*matrix[0], *spiralOrder(transposed)]


print(spiralOrder2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))