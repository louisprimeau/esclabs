#include<stdio.h>
#include<stdlib.h>
int append();
int appendhead();
int print();
struct llnode{
  int val;
  struct llnode *next;
};
typedef struct llnode llnode;
int llfree(llnode **next){
  if(next == NULL){return(-1);}
  if((*next)->next != NULL){
    llfree(&((**next).next));
  }
  free(*next);
  return(0);
}
int append(int val,llnode **next){
  if(next == NULL){return(-1);}
  if((*next) == NULL){
    (*next) = (llnode*)malloc(sizeof(llnode));
    (*next)->next = NULL;
    (*next)->val = val;
    return(0);
  }else{
    return(append(val, &((**next).next)));
  }
}
int appendhead(int val,llnode **next){
  llnode *node = NULL;
  if(next == NULL){return(-1);}
  node = (llnode *)malloc(sizeof(llnode));
  (*node).val = val;
  (*node).next = *next;
  *next = node;
  return(0);
}
int print(llnode *next){
  if(next == NULL){return(-1);}
  printf("%d ",next->val);
  if(next->next == NULL){
    printf("\n");
    return(0);
  }else{
    return(print(next->next));
  }
}
int main(void){
  llnode *root = NULL;
  root = (llnode *)malloc(sizeof(llnode));
  root->val = 5;
  root->next = NULL;
  print(root);
  append(6,&root);
  appendhead(7,&root);
  print(root);
  llfree(&root);
}
