#include "heap.c"
#include <stdio.h>
#include <stdlib.h>
int main(void){
  HeapType *test = (HeapType*)malloc(sizeof(HeapType));
  int *output = NULL;
  int i=0;
  int size = 0;
  initHeap(test, 13);
  for(i=12;i>=0;i--){
    addHeap(test, i);
  }
  inorder(test, &output, &size);

  for(i=0;i<size;i++){
    printf("%d ", (test->store)[i]);
  }
  printf("\n");

  delHeap(test, &size);

  for(i=0;i<test->end;i++){
    printf("%d ", (test->store)[i]);
  }
  printf("\n");
  return(0);
}
