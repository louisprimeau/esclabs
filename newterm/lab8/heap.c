typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
   int (*compare)(int x,int y);
} intHeap_T;

int store(intHeap_T* heap,int value){
  if(heap->end == heap->size){return(-1);}
  int index;
  int swap;
  (heap->store)[heap->end] = value;
  index = heap->end;
  while(1){
    if((heap->compare)((heap->store)[index],(heap->store)[index/2])){
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
  int index = 0;
  int swap;
  *rvalue = (heap->store)[0];
  (heap->store)[0] = (heap->store)[heap->end - 1];
  heap->end = heap->end - 1;
  while(1){
    if((index*2 + 1 < heap->end) && (index*2 < heap->end)){
      if((heap->compare)(heap->store[index],heap->store[index*2]) || (heap->compare)(heap->store[index],heap->store[index*2+1])){
        if((heap->compare)(heap->store[index*2],heap->store[index*2+1])){
          swap = (heap->store)[index];
          (heap->store)[index] = (heap->store)[index*2];
          (heap->store)[index*2] = swap;
          index = index * 2;
        }else{
          swap = (heap->store)[index];
          (heap->store)[index] = (heap->store)[index*2+1];
          (heap->store)[index*2+1] = swap;
          index = index * 2 + 1;
        }
      }else{break;}
    }
  }

  return(0);
}
