
# include <iostream>
# include <vector>

using std::cout;
using std::vector;
using std::endl;


bool dfs(int node, vector<int> adj[], vector<int>& visited, vector<int>& res) {
	if (visited[node] == -1)
		return false;

	else if (visited[node] == 1)
		return true;

	visited[node] = -1;
	for (int n: *(adj+node)) 
		if (visited[n]==-1 || !dfs(n, adj, visited, res))
			return false;

	visited[node] = 1;
	res.push_back(node);
	return true;
}

vector<int> findOrder(int numCourses, vector<vector<int>> prerequisites) {
	vector<int>* adj = new vector<int>[numCourses];
	for (vector<int> pair: prerequisites) 
		(adj+pair[0])->push_back(pair[1]);

	vector<int> res;
	res.reserve(numCourses);

	vector<int> visited(numCourses, 0);

	for (int i=0; i<numCourses; i++)
		if (!visited[i] && !dfs(i, adj, visited, res)) {
			cout << "None, cycle detected";
			return {};
		}

	delete[] adj;
	return res;
}


int main() {
	vector<vector<int>> prerequisites = {{5,0}, {4,0}, {0,1}, {1,3}, {0,2}, {3,2}};
	for (int n: findOrder(6, prerequisites)) 
		cout << n << ' ';

	cout << '\n';

	vector<vector<int>> prerequisites2 = {{0,1}, {1,2}, {2,0}};
	for (int n: findOrder(3, prerequisites2))
		cout << n << ' ';


	return 0;
}
