class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root){
        invertTree(root->left);
        invertTree(root->right);
        TreeNode *p=root->left;
        root->left=root->right;
        root->right=p;
        }
        return root;
    }
};