#include<stdio.h>
#include<stdbool.h> 
int findSequencePeriod(int sequence[], int length);
int main(){
    int N=100;
    int a[N], b[N];
    a[0]=0, a[1]=0, a[2]=1;
    b[0]=0, b[1]=0, b[2]=1;
    for(int i=3; i<100; i++){
        a[i]= (a[i-2]+2*a[i-3])%3;   //Q_1(x) = x^3 - 0*x^2 -x -2
        if(a[i]<0)a[i]+=3;
        b[i]= (b[i-2]+b[i-3])%2;     //Q_2(x) = x^3 - 0*x^2 -x -1
        if(b[i]<0)b[i]+=2;
    }
    int Ta=findSequencePeriod(a, 100), Tb=findSequencePeriod(b,100);
    printf("a的週期 = %d\n", Ta);
    for(int i=0; i<Ta; i++){
       printf("%d ", a[i]); 
    } printf("\n");
    printf("b的週期 = %d\n", Tb);
    for(int i=0; i<Tb; i++){
       printf("%d ", b[i]); 
    }
    printf("\n");
}

int findSequencePeriod(int sequence[], int length) {
    bool found = false;
    int period = 1;
    for (int i = 1; i <= length / 2; i++) {
        found = true;
        for (int j = 0; j < length - i; j++) {
            if (sequence[j] != sequence[j + i]) {
                found = false;
                break;
            }
        }
        if (found) {
            period = i;
            break;
        }
    }
    return period;
}