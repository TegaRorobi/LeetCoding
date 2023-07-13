
#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>

using std::cout;
using std::vector;
using std::stack;
using std::unordered_map;

class Graph {
protected:
	int V;
	unordered_map<int, vector<int>> adjacency;

public:
	Graph(int V) : V(V) {
		for (int i=0; i<V; ++i) 
			adjacency[i] = vector<int>();
	};

	// or we could just pass a vector of edges to the constructor
	void addEdge(int u, int v) {
		adjacency[u].push_back(v);
	}

	void topologicalSort() {
		vector<bool> visited(V, false);
		stack<int> stack;

		for (int i=0; i<V; ++i)
			if (!visited[i]) 
				dfs(i, visited, stack);

		while (!stack.empty()) {
			cout << stack.top() << ' ';
			stack.pop();
		}

	}

private:
	void dfs(int node, vector<bool>& visited, stack<int>& stack){
		visited[node] = true;
		for (int n: adjacency[node])
			if (!visited[n])
				dfs(n, visited, stack);
		stack.push(node);
	}
};


// Using a dynamic array of vectors as the adjacency list
// and a dynamic array of booleans as the visit cache and ..
// using ONLY pointer notation for indexing,
// for the sole fun of it :D
class Graph2 {
protected:
	int V;
	vector<int>* adjacency;

public:
	Graph2(int n_vertices) {
		V = n_vertices;
		adjacency = new vector<int>[V];
	};
	~Graph2() {
		delete[] adjacency;
	}

	void addEdge(int u, int v) {
		(adjacency+u)->push_back(v);
	}

	void topologicalSort() {
		bool* visited = new bool[V];
		stack<int> stack;

		for (int node=0; node<V; ++node)
			if (!*(visited+node))
				dfs(node, visited, stack);

		while (!stack.empty()) {
			cout << stack.top() << ' ';
			stack.pop();
		}

		delete[] visited;
	}

private:
	void dfs(int node, bool visited[], stack<int>& stack) {
		*(visited+node) = true;
		for (int neighbour: *(adjacency+node)) 
			if (!*(visited+neighbour))
				dfs(neighbour, visited, stack);
		stack.push(node);
	}
};


int main()
{
	// Create a graph given in the above diagram
	Graph2 g(6);
	g.addEdge(5, 2);
	g.addEdge(5, 0);
	g.addEdge(4, 0);
	g.addEdge(4, 1);
	g.addEdge(2, 3);
	g.addEdge(3, 1);
	// {0:[], 1:[], 2:[3], 3:[1], 4:[0,1], 5:[0,2]}

	cout << "Topological sort of the given graph: \n";

	g.topologicalSort();

	return 0;
}
