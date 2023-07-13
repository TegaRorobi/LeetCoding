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


# we don't need a visited and cycle set
def findOrder2(numCourses:int, prerequisites:list[list[int]]) -> list[int]:
	adj = {key:[] for key in range(numCourses)}
	for crs, pre in prerequisites: 
		adj[crs].append(pre)
	
	def dfs(crs, visited, res):
		if visitMap[crs] == 1:
			return True
		elif visitMap[crs] == -1:
			return False

		"""
		if visitMap[crs] is:
			-1, then we are currently running a dfs on that course, i.e that course is currently on the call stack
			0, then we haven't explored that course before. (at this point we start a new dfs on that course)
			1, then we are done with that course and we have explored all it's children and added them all to the result
		"""

		visitMap[crs] = -1
		for prereq in adj[crs]:
			if visitMap[prereq] == -1 or dfs(prereq, visited, res) is False:
				return False
		visitMap[crs] = 1
		res.append(crs)
		return True

	res = []
	visitMap = {key:0 for key in range(numCourses)}

	for i in range(numCourses):
		if visitMap[i]==0 and not dfs(i, visitMap, res):
			return []
	return res




print(findOrder2(6, [[5,0], [4,0], [0,1], [1,3], [0,2], [3,2]])) # [2, 3, 1, 0, 4, 5]
print(findOrder2(2, [[0, 1], [1, 0]]))
# print(findOrder2(2, [[1,0]]))
# print(findOrder2(5, [[0,1], [0,2], [1,3], [1,4], [3,4]]))
# print(findOrder2(3, [[0,1], [1,2], [2,0]]))
