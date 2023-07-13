
#include <iostream>
#include <vector>
#include <unordered_map>

using std::cout;
using std::endl;
using std::vector;
using std::unordered_map;


class Solution {
public:
	bool canFinish(int numCourses, vector<vector<int>> prerequisites) {
		// building the adjancency list
		unordered_map<int, vector<int>> adj(numCourses);
		for (auto v: prerequisites) 
			adj[v[0]].push_back(v[1]);

		// -1 -> we are currently checking for a cycle, i.e we are visiting the node.
		// 0 -> we haven't seen the node
		// 1 -> we are done with the node, and visited all it's children.

		vector<int> visited(numCourses, 0);
		for (int node=0; node < numCourses; node++) 
			if (visited[node] == 0 && !dfs(adj, node, visited)) 
				return false;
		return true;
	}

private:
	bool dfs(unordered_map<int, vector<int>> adj, int node, vector<int>& visited) {
		visited[node] = -1;
		for (int i : adj[node]) 
			if (visited[i] == -1 or !(dfs(adj, i, visited)))
				return false;
		visited[node] = 1;
		return true;
	}
};



int main() {
	typedef vector<vector<int>> graph;

	Solution sol;
	graph pre = {{0,1}, {0,2}, {1,3}, {1,4}, {3,4}};
	cout << (sol.canFinish(5, pre)?"true":"false") << endl;


	graph pre2 = {{0,1}, {1,2}, {2,3}, {3,0}};
	cout << (sol.canFinish(4, pre2)?"true":"false") << endl;

	return 0;
}