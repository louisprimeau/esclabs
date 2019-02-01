#include "avlrot.c"
#include <stdio.h>

int main(void){
  avlNode *root = NULL;
  add_bst(&root,20);
  add_bst(&root,10);
  add_bst(&root,25);
  add_bst(&root,15);
  add_bst(&root,12);
  add_bst(&root,16);

  printlevelorder(root);
  printf("\n");
  dblrotate(&root, 0);
  printlevelorder(root);
  printf("\n");
  return(0);
}
