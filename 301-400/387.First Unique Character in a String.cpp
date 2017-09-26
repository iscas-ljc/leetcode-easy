class Solution {
public:
    int firstUniqChar(string s) {
        int lens=s.size();
        int arr[26];
        for(int i=0;i<26;i++){
            arr[i]=0;
        }
        for(int i=0;i<lens;i++){
        	arr[s[i]-'a']++;
		}
		for(int i=0;i<lens;i++){
			if(arr[s[i]-'a']==1){
				return i;
			}
		}
		return -1;
    }
};