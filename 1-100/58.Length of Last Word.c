int lengthOfLastWord(char* s) {
    int len=strlen(s);
    int result=0;
    if(len==0){
    	return 0;
    }
    for(int i=len-1;i>=0;i--){
    	if(s[i]!=' '){break;}
    	if(s[i]=' '){
    		s[i]=0;
    	}
    }
    len=strlen(s);
    if(len==0){return 0;}
    for(int i=len-1;i>=0;i--){
    	if(s[i]!=' '){
    		result++;
    	}else{
    		return result;
    	}
    }
    return result;
}