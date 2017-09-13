class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t result=0;
        for(int i=0;i<32;i++){
        	if((n&1)==1){     //n&1的括号必须要有
        		result=(result<<1)+1;	//result<<1的括号必须要有  <<>>的优先级低于+——
        		n>>=1;
        	}
        	else{
        		result<<=1;
        		n>>=1;
        	}
        }
        return result;
    }
};