#include <stdio.h>
#include <stdlib.h>

struct stack {
   char value;
   struct stack *next;
};
typedef struct stack stack;

int push(stack **x, char value){
  stack *newHead;
  if (x == NULL){return -1;}
  newHead = (stack *)malloc(sizeof(stack));
  if(newHead == NULL){return -1;}
  (newHead)->value = value;
  (newHead)->next = *x;
  *x = newHead;
  return(0);
}
int pop(stack **x, char *value){
  if(x == NULL){return(-1);}
  if(*x == NULL){return(-1);}
  if(value == NULL){return(-1);}
  *value = (*x) -> value;
  *x = (*x) -> next;
  return(0);
}


struct queue {
  char value;
  struct queue *next;
};
typedef struct queue queue;

int enqueue(queue **x, char value){
  queue *newHead;
  if (x == NULL){return -1;}
  newHead = (queue *)malloc(sizeof(stack));
  if(newHead == NULL){return -1;}
  (newHead)->value = value;
  (newHead)->next = *x;
  *x = newHead;
  return(0);
}

int dequeue(queue **x, char *value){
  queue *traverse;
  if(x==NULL){return(-1);}
  if(value==NULL){return(-1);}
  traverse = *x;
  while((traverse->next)->next != NULL){
    traverse = traverse->next;
  }
  *value = traverse->value;
  free(traverse->next);
  traverse->next = NULL;
  return(0);
}
int main(void){return(0);}
