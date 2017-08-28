bool check(struct TreeNode* node1, struct TreeNode* node2) {
        if (node1 == NULL && node2 == NULL) {
            return true;
        }
        if (node1 == NULL || node2 == NULL) {
            return false;
        }
        if (node1->val != node2->val) {
            return false;
        } else {
            return check(node1->left, node2->right)
                    && check(node1->right, node2->left);
        }
}
bool isSymmetric(struct TreeNode* root) {
     if (root == NULL) {
            return true;
        }

        return check(root->left, root->right);
    }
