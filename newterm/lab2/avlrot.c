#include <stdlib.h>
#include <stdio.h>

struct avlNode {
   int balance; /* -1 Left, 0 balanced, +1 Right */
   int val;
   struct avlNode *l;
   struct avlNode *r;
};
typedef struct avlNode avlNode;

struct qNode {
   avlNode *pval;
   struct qNode *nxt;
};
typedef struct qNode qNode;



int isAVL(avlNode **root);
int depth(avlNode *root);
int rotate(avlNode **root,unsigned int Left0_Right1);
int dblrotate(avlNode **root,unsigned int MajLMinR0_MajRMinL1);
int printinorder(avlNode *root);
int printlevelorder(avlNode *root);


int bstenq(qNode **root, avlNode *nxt){
  qNode *copy = NULL;
  if(root == NULL){return(-1);}
  if(*root == NULL){
    *root = (qNode *)malloc(sizeof(qNode));
    (*root)->nxt = NULL;
    (*root)->pval = nxt;
  }else{
    copy = *root;
    while( (copy)->nxt != NULL){
      copy = (copy)->nxt;
    }
    (copy)->nxt = (qNode *)malloc(sizeof(qNode));
    if((copy)->nxt == NULL){return(-1);}
    ((copy)->nxt)->nxt = NULL;
    ((copy)->nxt)->pval = nxt;
  }
  return(0);
}
int bstdeq(qNode **root,avlNode **pval){
  if(root == NULL){return(-1);}
  if(pval == NULL){return(-1);}
  if(*root == NULL){return(-1);}
  *pval = (*root)->pval;
  *root = (*root)->nxt;
  return(0);
}

int printlevelorder(avlNode *node){
  qNode *q = NULL;
  avlNode *holder;
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

int depth(avlNode *root){
  if(root == NULL){return(-1);}
  int r = depth((root)->r);
  int l = depth((root)->l);
  if(l > r){
    return(l + 1);
  }else{
    return(r + 1);
  }
}


int isAVL(avlNode **root){
  if(root == NULL){return(-1);}
  if((depth((*root)->l) > depth((*root)->r) + 1) || (depth((*root)->l) < depth((*root)->r) + 1)){
    return(-1);
  }else{
    return(0);
  }
}

int rotate(avlNode **root,unsigned int Left0_Right1){
  avlNode *newroot;
  avlNode *sw;
  if(Left0_Right1 == 1){
    newroot = (*root)->l;
    sw = newroot->r;
    newroot->r = *root;
    (*root)->l = sw;
  }else if(Left0_Right1 == 0){
    newroot = (*root)->r;
    sw = newroot->l;
    newroot->l = *root;
    (*root)->r = sw;
  }else{
    return(-1);
  }
  *root = newroot;
  return(0);
}

int add_bst(avlNode **root,int val) {
   if (root == NULL) { return -1; }
   if (*root == NULL) {
      *root = (avlNode *)malloc(sizeof(avlNode));
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

int dblrotate(avlNode **root,unsigned int MajLMinR0_MajRMinL1){
  if(root == NULL){return(-1);}
  if(MajLMinR0_MajRMinL1 == 0){
    rotate(&((*root)->r),1);
    rotate(&((*root)),0);
  }else if(MajLMinR0_MajRMinL1 == 1){
    rotate(&((*root)->l),0);
    rotate(root,1);
  }else{return(-1);}
  return(0);
}

int printinorder(avlNode *root){
  if(root == NULL){return(-1);}
  printinorder(root->l);
  printf("%d\n",root->val);
  printinorder(root->r);
  return(0);
}
