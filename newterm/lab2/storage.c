struct bstqueue {
   bstNode value;
   struct bstqueue *next;
};
typedef struct bstqueue bstqueue;

int bstenqueue(bstqueue **x, bstNode value){
  bstqueue *newHead;
  if (x == NULL){return -1;}
  newHead = (bstqueue *)malloc(sizeof(bstqueue));
  if(newHead == NULL){return -1;}
  (newHead)->value = value;
  (newHead)->next = *x;
  *x = newHead;
  return(0);
}
int bstdequeue(bstqueue **x, bstNode *value){
  bstqueue *copy = *x;
  if(x == NULL){return(-1);}
  if(*x == NULL){return(-1);}
  if(value == NULL){return(-1);}
  while((*x)->next != NULL){
      printf("dequeueing");
      copy = (*x)->next;
  }
  value = &(copy->value);
  return(0);
}

int printdepthfirst(bstNode *node){
    if(node == NULL){return(-1);}
    printf("%d\n",node->val);
    printdepthfirst(node->l);
    printdepthfirst(node->r);
    return(0);
}
int printbreadthfirst(bstNode *node){
  bstqueue *queue = NULL;
  bstNode holder;
  if(node == NULL){return(-1);}
  bstenqueue(&queue,*node);
  while(queue != NULL){
    printf("breadthing");
    bstdequeue(&queue, &holder);
    if(holder.l != NULL)
      bstenqueue(&queue,*(holder.l));
    if(holder.r != NULL)
      bstenqueue(&queue,*(holder.r));
    printf("%d\n", holder.val);
  }
  return(0);
}
