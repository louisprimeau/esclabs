#include <stdio.h>
#include <stdlib.h>

struct bstNode {
   int val;
   struct bstNode *l;
   struct bstNode *r;
};
typedef struct bstNode bstNode;

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
