#include <stdio.h>
#include <stdlib.h>
int main(void){
  int *y = NULL;
  y = malloc(5*sizeof(int));
  scanf("%d",y);
  printf("%d\n",y[0]);
  return(0);
}
