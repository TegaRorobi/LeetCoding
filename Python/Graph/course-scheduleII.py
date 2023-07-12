# medium 

"Topoloical sort"
def findOrder(numCourses:int, prerequisites:list[list[int]]) -> list[int]:
	preMap = {key:[] for key in range(numCourses)}
	for course, prerequisite in prerequisites:
		preMap[course].append(prerequisite)

	res, visited, cycle = [], set(), set()
	def dfs(course):
		if course in cycle:
			return False
		if course in visited:
			return True
		cycle.add(course)
		for prerequisite in preMap[course]:
			if dfs(prerequisite) is False:
				return False
		cycle.remove(course)

		visited.add(course)
		res.append(course)

		return True

	for course in range(numCourses):
		if dfs(course) == False:
			return []
	return res






print(findOrder(6, [[5,0], [4,0], [0,1], [1,3], [0,2], [3,2]]))
print(findOrder(2, [[1,0]]))
print(findOrder(5, [[0,1], [0,2], [1,3], [1,4], [3,4]]))
print(findOrder(3, [[0,1], [1,2], [2,0]]))
