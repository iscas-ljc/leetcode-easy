class Solution {
public:
    string addBinary(string a, string b) {
        int sizea = a.size();
        int sizeb = b.size();
        if(sizea < sizeb)
            return addBinary(b, a);
        string zeros(sizea-sizeb, '0');
        b = zeros + b;
        int carry = 0;
        for(int i = sizea-1; i >= 0; i --)
        {
            int sum = (a[i]-'0') + (b[i] - '0') + carry;
            if(sum == 1)
            {a[i] = '1';carry = 0;}
            else if(sum == 2)
            {a[i] ='0';carry = 1;}
            else if(sum ==3)
            {a[i] = '1';carry = 1;}
        }
        if(carry == 1)
            a = "1" + a;
        return a;
    }
};