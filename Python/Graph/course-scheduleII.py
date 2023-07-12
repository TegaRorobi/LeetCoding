# medium 

"Topological sort"
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



def findOrder2(numCourses:int, prerequisites:list[list[int]]) -> list[int]:
	hashmap = {key:[] for key in range(numCourses)}
	for crs, pre in prerequisites: 
		hashmap[crs].append(pre)
	print(hashmap)
	

	def dfs(crs, visited, res):
		if crs in visited:
			return 
		visited.add(crs)
		for prereq in hashmap[crs]:
			if dfs(prereq, visited, res) is False:
				return 
		res.append(crs)

	res = []
	visited = set()
	for i in range(numCourses):
		dfs(i, visited, res)
	return res




print(findOrder2(6, [[5,0], [4,0], [0,1], [1,3], [0,2], [3,2]])) # [2, 3, 1, 0, 4, 5]
print(findOrder2(2, [[0, 1], [1, 0]]))
# print(findOrder2(2, [[1,0]]))
# print(findOrder2(5, [[0,1], [0,2], [1,3], [1,4], [3,4]]))
# print(findOrder2(3, [[0,1], [1,2], [2,0]]))
