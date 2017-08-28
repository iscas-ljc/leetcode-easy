int climbStairs(int n) {
    if (n < 3) return n;  
    int p = 1;  
    int q = 2;  
    for (int i = 0; i < n - 2; i++){  
        int t = p + q;  
        p = q;  
        q = t;  
    }  
    return q;  
}