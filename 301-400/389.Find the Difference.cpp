class Solution {
public:
    char findTheDifference(string s, string t) {
        char x=0;
        for(int i=0;i<s.size();i++){
            x ^= s[i];
        }
        for(int j=0;j<t.size();j++){
            x ^= t[j];
        }
        return x;
    }
};
// a^a=''