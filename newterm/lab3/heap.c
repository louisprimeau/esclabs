#include <stdio.h>
#include <stdlib.h>
typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
} HeapType;

int initHeap(HeapType *pHeap,int size){
  pHeap->size = size;
  pHeap->end = 0;
  pHeap->store = (int *)malloc(sizeof(int)*size);
  return(0);
}

int inrecurse(int *subList, int listSize, int index, int **list, int *end){
  if(2*index + 1 < listSize){
    inrecurse(subList, listSize, 2*index + 1, list, end);
  }
  (*list)[*end] = subList[index];
  *end += 1;
  if(2 * index + 2 < listSize){
    inrecurse(subList, listSize, 2*index + 2, list, end);
  }
  return(0);
}

int inorder(HeapType *pHeap, int **output, int *o_size){
  *o_size = 0;
  *output = (int *)malloc(sizeof(int) * pHeap->end);
  inrecurse(pHeap->store, pHeap->end, 0, output, o_size);
  return(0);
}

int postrecurse(int *subList, int listSize, int index, int **list, int *end){
  if(2*index + 1 < listSize){
    inrecurse(subList, listSize, 2*index + 1, list, end);
  }
  if(2 * index + 2 < listSize){
    inrecurse(subList, listSize, 2*index + 2, list, end);
  }
  (*list)[*end] = subList[index];
  *end += 1;
  return(0);
}

int postorder(HeapType *pHeap, int **output, int *o_size){
  *o_size = 0;
  *output = (int *)malloc(sizeof(int) * pHeap->end);
  inrecurse(pHeap->store, pHeap->end, 0, output, o_size);
  return(0);
}

int prerecurse(int *subList, int listSize, int index, int **list, int *end){
  (*list)[*end] = subList[index];
  *end += 1;
  if(2*index + 1 < listSize){
    inrecurse(subList, listSize, 2*index + 1, list, end);
  }
  if(2 * index + 2 < listSize){
    inrecurse(subList, listSize, 2*index + 2, list, end);
  }

  return(0);
}

int preorder(HeapType *pHeap, int **output, int *o_size){
  *o_size = 0;
  *output = (int *)malloc(sizeof(int) * pHeap->end);
  inrecurse(pHeap->store, pHeap->end, 0, output, o_size);
  return(0);
}

int addHeap(HeapType *pHeap, int key){
  int added = pHeap->end;
  int swap = 0;
  (pHeap->store)[pHeap->end] = key;
  while((pHeap->store)[added] > (pHeap->store)[(int)((added - 1) / 2)]){
    swap = (pHeap->store)[(int)((added - 1) / 2)];
    (pHeap->store)[(int)((added - 1) / 2)] = (pHeap->store)[added];
    (pHeap->store)[added] = swap;
    added = (int)((added - 1) / 2);
  }
  pHeap->end += 1;
  return(0);
}
 int findHeap(HeapType *pHeap, int key){
   int i;
   if(pHeap == NULL){return(-1);}
   for(i = 0; i < pHeap->end; i++){
     if(key == (pHeap->store)[i]){
       return(1);
     }
   }
   return(0);
 }
 int delHeap(HeapType *pHeap, int *key){
   int swap = 0;
   int current = 0;
   int childval;
   int child = -1;
   *key = (pHeap->store)[0];
   (pHeap->store)[0] = (pHeap->store)[pHeap->end];
   pHeap->end -= 1;
   while(1){
    if(2*current + 1 < pHeap->end){
      if((pHeap->store)[2*current + 1] > (pHeap->store)[current]){
        child = 0;
        childval = (pHeap->store)[2*current + 1];
      }
    }
    if(2*current + 2 < pHeap->end){
      if((pHeap->store)[2*current + 2] > childval){
        child = 1;
        childval = (pHeap->store)[2*current + 2];
      }
    }

    if(child != -1){
      swap = (pHeap->store)[2*current + 1 + child];
      (pHeap->store)[2*current + 1 + child] = (pHeap->store)[current];
      (pHeap->store)[current] = swap;
      current = 2*current + 1 + child;
      child = -1;
    }else{
      break;
    }
  }
  return(0);
 }
