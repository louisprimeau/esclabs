#include <stdio.h>
#include "ll.h"

int main(void) {
   llnode *root = NULL;
   llnode *root2 = NULL;
   llnode *hold = NULL;
   int r=0;
   int i=0;

   printf("List A\n");
   r=ll_add_to_tail(&root,100);
   r=ll_add_to_tail(&root,200);
   r=ll_add_to_tail(&root,300);
   for(i=0;i<10;i=i+1){
      r=ll_add_to_tail(&root,i*100);
   }
   r=ll_sort(&root);
   hold = (*root).next;
   r=ll_print(root);
   printf("-\n");
   r=ll_del_from_head(&root);
   root = hold;
   r=ll_print(root);
   printf("-\n");
   r=ll_insert_in_order(&root,100);
   printf("%d\n",ll_find_by_value(root,900));
   r=ll_del_from_tail(&root);
   r=ll_del_from_tail(&root);
   printf("%d\n",ll_find_by_value(root,900));
   r=ll_print(root);
   r=ll_free(root);

   printf("List B\n");
	 root2=NULL;
   r=ll_add_to_tail(&root2,100);
   r=ll_add_to_tail(&root2,200);
   r=ll_add_to_tail(&root2,300);
   for(i=0;i<10;i=i+1){
      r=ll_add_to_head(&root2,i*100);
   }
   r=ll_print(root2);
   r=ll_free(root2);
   return 0;
}
