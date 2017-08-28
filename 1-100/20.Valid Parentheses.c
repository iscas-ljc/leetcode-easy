bool isValid(char* s) {
    char stack[1000000];  
    int top=-1;  
    while(*s){  
        if(*s==')'){  
            if(top>=0 && stack[top]=='(')top--;  
            else return false;  
        }else if(*s=='}'){  
            if(top>=0 && stack[top]=='{')top--;  
            else return false;  
        }else if(*s==']'){  
            if(top>=0 && stack[top]=='[')top--;  
            else return false;  
        }else stack[++top]=*s;  
        s++;  
    }  
    return top==-1;  
}