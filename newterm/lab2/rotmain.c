#include "avlrot.c"
#include <stdio.h>
int main(void){
  int a;
  avlNode *root = NULL;
  add_bst(&root,20);
  add_bst(&root,10);
  add_bst(&root,25);
  add_bst(&root,15);
  add_bst(&root,12);
  add_bst(&root,16);

  printf("depth: %d\n",depth(root));
  a = isAVL(&root);
  printf("%d\n",a);
  printlevelorder(root);
  printf("\n");
  rotate(&root, 0);
  printlevelorder(root);
  printf("\n");
  return(0);
}
