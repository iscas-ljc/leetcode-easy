class Solution {
public:
    string convertToTitle(int n) {
        string result="";
        while(n){
            result=char((n-1)%26+'A')+result;
            n=(n-1)/26;
        }
        return result;
    }
};