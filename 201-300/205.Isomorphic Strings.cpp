class Solution {
public:
    bool isIsomorphic(string s, string t) {
        return trans(s)==trans(t);
    }
    string trans(string s){
    	char temp='0';
    	vector<char> count(128,0);
    	for(int i=0;i<s.size();i++){
    		if(count[s[i]]==0){
    			count[s[i]]=temp++;
    		}
    		s[i]=count[s[i]];
    	}
    }
};