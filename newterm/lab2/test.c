#include <stdio.h>
#include <stdlib.h>

struct bstNode {
   int val;
   struct bstNode *l;
   struct bstNode *r;
};
typedef struct bstNode bstNode;

struct bstQ {
   bstNode *value;
   struct bstQ *next;
};
typedef struct bstQ bstQ;


int bstenq(bstQ **root, bstNode *next){
  bstQ *copy = NULL;
  if(root == NULL){return(-1);}
  if(*root == NULL){
    *root = (bstQ *)malloc(sizeof(bstQ));
    (*root)->next = NULL;
    (*root)->value = next;
  }else{
    copy = *root;
    while( (copy)->next != NULL){
      copy = (copy)->next;
    }
    (copy)->next = (bstQ *)malloc(sizeof(bstQ));
    if((copy)->next == NULL){return(-1);}
    ((copy)->next)->next = NULL;
    ((copy)->next)->value = next;
  }
  return(0);
}
int bstdeq(bstQ **root,bstNode **value){
  if(root == NULL){return(-1);}
  if(value == NULL){return(-1);}
  if(*root == NULL){return(-1);}
  *value = (*root)->value;
  *root = (*root)->next;
  return(0);
}
int printlevelorder(bstNode *node){
  bstQ *q = NULL;
  bstNode *holder;
  if(node == NULL){return(-1);}
  bstenq(&q,node);
  while(q != NULL){
    bstdeq(&q, &holder);
    printf("%d ", holder->val);
    if(holder->l != NULL)
      bstenq(&q, holder->l);
    if(holder->r != NULL)
      bstenq(&q, holder->r);
  }
  return(0);
}

int printinorder(bstNode *root){
  if(root == NULL){return(-1);}
  printinorder(root->l);
  printf("%d\n",root->val);
  printinorder(root->r);
  return(0);
}

int add_bst(bstNode **root,int val) {
   if (root == NULL) { return -1; }
   if (*root == NULL) {
      *root = (bstNode *)malloc(sizeof(bstNode));
      (*root)->val = val;
      (*root)->l = NULL;
      (*root)->r = NULL;
    } else {
      if(val > (*root)->val){
        add_bst( &((*root)->r) , val );
      }else if(val < (*root)->val){
        add_bst( &((*root)->l) , val );
      }
   }
   return(0);
}



int main(void){
  bstNode *root=NULL;
  add_bst(&root,5);
  add_bst(&root,3);
  add_bst(&root,1);
  add_bst(&root,4);
  add_bst(&root,7);
  add_bst(&root,6);
  add_bst(&root,8);
  printinorder(root);
  printlevelorder(root);
  //printbreadthfirst(&a);
  return(0);
}
int print(bstNode *root){
return(0);
}
