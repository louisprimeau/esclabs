#include <stdio.h>
#include <stdlib.h>
typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
   int (*compare)(int x,int y);
} intHeap_T;

int printarray(int *x,int size){
  int i = 0;
  for(i = 0; i < size; i++){
    printf("%d ",x[i]);
  }
  printf("\n");
  return(1);
}
int store(intHeap_T* heap,int value){
  if(heap->end == heap->size){return(-1);}
  int index;
  int swap;
  (heap->store)[heap->end] = value;
  index = heap->end;
  while(1){
    if((heap->compare)((heap->store)[index/2],(heap->store)[index])){
      swap = (heap->store)[index];
      (heap->store)[index] = (heap->store)[index/2];
      (heap->store)[index/2] = swap;
      index = index / 2;
    }else{
      break;
    }
  }
  heap->end = heap->end + 1;
  return(1);
}

int retrieve(intHeap_T* heap,int *rvalue){
  if(heap->end == 0){return(-1);}
  int index = 1;
  int swap;
  *rvalue = (heap->store)[0];
  (heap->store)[0] = (heap->store)[heap->end - 1];
  heap->end = heap->end - 1;
  while(1){
    if((index*2 < heap->end) && (index*2 - 1 < heap->end)){
      if((heap->compare)(heap->store[index - 1],heap->store[index*2 - 1]) || (heap->compare)(heap->store[index - 1],heap->store[index*2])){
        if((heap->compare)(heap->store[index*2],heap->store[index*2 - 1])){
          swap = (heap->store)[index - 1];
          (heap->store)[index - 1] = (heap->store)[index*2 - 1];
          (heap->store)[index*2 - 1] = swap;
          index = index * 2;
        }else{
          swap = (heap->store)[index - 1];
          (heap->store)[index - 1] = (heap->store)[index*2];
          (heap->store)[index*2] = swap;
          index = index * 2 + 1;
        }
      }else{break;}
    }else{break;}
  }

  return(0);
}
int lt(int x,int y){
  if(x < y){
    return(1);
  }else{
    return(0);
  }
}
int gt(int x,int y) {
  if(x > y){
    return(1);
  }else{
    return(0);
  }
}
int hs(int *x,int size,int (*compare)(int x,int y)){
  intHeap_T heap;
  int i;
  heap.store=(int *)malloc(size*sizeof(int));
  heap.size=size;
  heap.end=0;
  heap.compare = compare;
  for(i = 0; i < size; i++){
    store(&heap,x[i]);
  }
  printarray(heap.store,heap.end);
  for(i=0;i<size;i++){
    retrieve(&heap,&(x[i]));
  }
  return(0);
}

int main(void){
  int x[10] = {6,7,4,5,8,19,2,412,23,1};
  hs(x, 10, lt);
  printarray(x,10);
  return(0);
}
