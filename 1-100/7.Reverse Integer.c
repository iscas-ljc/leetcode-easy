int reverse(int x) {
    int flag=x>0?1:-1;
    long result=0;
    x=x>0?x:-x;
    while(x>0){
        if((2147483647.0-x%10)/10<result)return 0;
        result=result*10+x%10;
        x=x/10;
    }
    result=flag*result;
    //if(x>1073741824){return 0;}
    return result;
}