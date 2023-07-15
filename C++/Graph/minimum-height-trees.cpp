 
#include <iostream>
#include <vector>
#include <list>

using std::cout;
using std::endl;
using std::vector;
using std::list;


vector<int> findMinHeightTrees(int n, vector<vector<int>> edges) 
{
    // initialize adjacency list as a pointer to the 
    // first element of an array of list<int> objects
    list<int>* adj = new list<int>[n];

    // populate adjacency list
    for (auto edge: edges) {
        int a = edge[0], b = edge[1];
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    // group the initial leaves
    vector<int> leaves;
    for (int i=0; i<n; ++i) {
        if (adj[i].size() == 1) {
            leaves.push_back(i);
        }
    }

    // eat up all the leaves at once until one or two leaves remain,
    // these two leaves are the answer to the problem, so we simply return.
    while (n>2) {
        n -= (leaves.size());
        vector<int> newLeaves;
        for (int leaf:leaves) {
            int branch = adj[leaf].front();

            // after hours of debugging, I realized that we have to remove the 
            // leaf from the branch's array in the actual adjacency list, 
            // and previously I naively removed it from a copy (hard facepalm...)
            list<int>* branch_arr = &(adj[branch]);
            branch_arr->remove(leaf);
            if (branch_arr->size() == 1){
                newLeaves.push_back(branch);
            }
        }
        leaves = newLeaves;
    }
    return leaves;
}



void display(auto arr) {
    for (auto x:arr) 
        cout << '(' << x << ") ";
    cout << endl;
}



int main() 
{
    display(findMinHeightTrees(4, vector<vector<int>>{{1,0},{1,2},{1,3}}));
    display(findMinHeightTrees(6, vector<vector<int>>{{3,0},{3,1},{3,2},{3,4},{5,4}}));

    return 0;
}