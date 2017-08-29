*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 class Solution {
 public:
 	vector<vector<int>> levelOrderBottom(TreeNode* root) {
 		vector<vector<int>> res;
 		if (!root) return res;
 		queue<TreeNode*> q;
 		q.push(root);
 		while (!q.empty()) {
 			vector<int> lev;
 			int _size = q.size();
 			for (int i = 0; i < _size; i++) {
 				TreeNode *temp = q.front();
 				q.pop();
 				lev.push_back(temp -> val);
 				if (temp -> left) q.push(temp -> left);
 				if (temp -> right) q.push(temp -> right);
 			}
 			res.push_back(lev);
 		}
 		reverse(res.begin(), res.end());
 		return res;
 	}
 };