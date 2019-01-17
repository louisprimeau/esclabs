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
