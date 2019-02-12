/*#include <stdio.h>
int bubbleSort();
int main(void){
  int x[5] = {5,4,3,2,1};
  int i = 0;


  bubbleSort(x);
  for(i = 0; i < 5; i++){
    printf("%d",x[i]);
  }
  return(0);
}*/
int bubbleSort(int* A, int length){
  int swapped = 1;
  int hold = 0;
  int i = 0;

  while(swapped != 0){
    swapped = 0;
    for(i = 1; i < length; i++){
      if(A[i-1] > A[i]){
        hold = A[i];
        A[i] = A[i-1];
        A[i-1] = A[i];
        swapped = 1;
      }
    }
  }
  return(1);
}
