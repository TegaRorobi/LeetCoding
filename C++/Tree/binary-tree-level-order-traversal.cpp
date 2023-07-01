
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
	    vector<vector<int>> ans;
	    if (root == nullptr) 
	    	return ans;

	    queue<TreeNode*> stack;
	    stack.push(root);

	    while (!stack.empty()) {
	        vector<int> level;
	        int n = stack.size();
	        while (n-- > 0){

	            TreeNode* node = stack.front();
	            stack.pop();

	            level.push_back(node->val);
	            
	            if(node->left)
	                stack.push(node->left);
	            if(node->right)
	                stack.push(node->right);
	        }
	        ans.push_back(level);
	    }
	    std::reverse(ans.begin(), ans.end());
	    return ans;
	}
};