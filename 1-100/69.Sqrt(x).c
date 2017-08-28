int mySqrt(int x){
	if(x<0){
		return NULL;
	}
    if(x>=(46340*46340)){
        return 46340;  //最大的int为2147483647，检测不到46341的平方，要单独说明
    }
	for(int i=0;i<1000000000;i++){
		if((i*i)==x){
			return i;
		}
		if(x<((i+1)*(i+1))){
			return i;
		}
	}
	return 10000;
}