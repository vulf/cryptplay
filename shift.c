#include <stdio.h>
#include <string.h>

int shift();

void main(){
    
    shift();

}

int shift(){

    int k,i,t;
    char m[50],res[50],opt;

    printf("enter message and key: ");
    scanf("%s %d", &m, &k);
    printf("encrypt or decrypt?(e/d): ");
    scanf(" %c", &opt);
    if(opt=='e'){
       for(i=0;i<strlen(m);i++){
           t = m[i] - 97;
           res[i] = ( (t + k)%26 ) + 97;
       } 
       printf("secret: %s", &res);
    }
    else if(opt=='d'){
        for(i=0;i<strlen(m);i++){
            t = m[i] - 97;
            res[i] = ( (t - k)%26 ) + 97;
        }
        printf("message: %s", &res);
    }
    return 0;
}
