/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 	正确解，但是超时了
    int result=0;
    if(root==NULL){return result;};
    if(root!=NULL){
    	result++;
    	if(maxDepth(root->left)>maxDepth(root->right)){
    		return result+maxDepth(root->left);
    	else{
    			return result+maxDepth(root->right);
    		}
    	}
    }
    return result;
}
*/
int maxDepth(struct TreeNode* root) {
    int left=0;
    int right=0;
    if(root==NULL){return 0;}
    else{
    	left=1;
    	right=1;
    	left=left+maxDepth(root->left);
    	right=right+maxDepth(root->right);
    }
    if(left>=right){return left;}
    else{
    	return right;
    }
}