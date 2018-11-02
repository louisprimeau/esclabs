#include <stdio.h>

int fibo(int n);

int main(void) {
   int i = 0;
   int arg = 0;
   printf("Enter a number:\n");
   scanf("%d",&arg);
   for (i=0;i<arg;i=i+1){
      int f = fibo(i);
      printf("fibo(%d)=%d\n",i,f);
   }

   return 0;
}

int fibo(int n){
   if((n == 0) || (n == 1)){
     return(1);
   }else{
   return(fibo(n - 1) + fibo(n - 2));}
}
