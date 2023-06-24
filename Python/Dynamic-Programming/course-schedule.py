
def canFinish(numCourses:int, prerequisites:list[list[int]]) -> bool:
	preMap = {key:[] for key in range(numCourses)}
	for course, prerequisite in prerequisites:
		preMap[course].append(prerequisite)
	# print(preMap)

	visited = set()
	def dfs(course):
		visited.add(course)
		# print(course, visited)
		for prerequisite in preMap[course]:
			if prerequisite in visited or dfs(prerequisite) is False:
				return False
		visited.remove(course)
		return True
	return dfs(0)


print(canFinish(5, [[0,1], [0,2], [1,3], [1,4], [3,4]]))
print(canFinish(3, [[0,1], [1,2], [2,0]]))
