#include <stdio.h>
int f(int x) {
  if (x==-1) {
    return 2;
  }else{
    return x*f(x-2);
  }
}

int main(void){
  printf("%d\n",f(5));
}
