bool compare(char* l1,char* l2,int len1,int len2,int start){
    for(int i=0;i<len2;i++){
        if(l1[start]!=l2[i]){
            return false;
        }
        start++;
    }
    return true;
}
int strStr(char* haystack, char* needle) {
    int len1=strlen(haystack);
    int len2=strlen(needle);
    if(len2==0){return 0;}
    if(len1<len2){return -1;}
    if(len1==len2&&compare(haystack,needle,len1,len2,0)){return 0;}
    for (int i=0;i<len1;i++){
        if(haystack[i]==needle[0]&&compare(haystack,needle,len1,len2,i)){
        return i;
        }
    }
    return -1;
}