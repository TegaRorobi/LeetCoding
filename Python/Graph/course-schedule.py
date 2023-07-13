
def canFinish(numCourses:int, prerequisites:list[list[int]]) -> bool:
	preMap = {key:[] for key in range(numCourses)}
	for course, prerequisite in prerequisites:
		preMap[course].append(prerequisite)

	visited = [0] * numCourses
	def dfs(course):
		visited[course] = -1
		for prerequisite in preMap[course]:
			if visited[prerequisite] == -1 or dfs(prerequisite) is False:
				return False
		visited[course] = 1
		return True

	# visited[course] == 0: we haven't seen this course
	# visited[course] == 1: we have seen this course and it is possible to complete it
	# visited[course] == -1: we are currently running a dfs and checking for a cycle on this course

	for i in range(numCourses):
		# if we haven't seen this course and the dfs say's we can't complete it
		if visited[course] == 0 and  dfs(course) is False:
			return False
	return True


print(canFinish(5, [[0,1], [0,2], [1,3], [1,4], [3,4]]))
print(canFinish(3, [[0,1], [1,2], [2,0]]))
print(canFinish(5, [[4,1], [1,3], [3,4]]))
print(canFinish(2, [[1, 0], [0, 1]]))