/*
For the same computer as the prior question, how many bytes are needed to store
(a) a linked list of 100 integers, and
(b) an array of 100 integers. Show all work.
*/
#include <stdio.h>
struct llnode{
  int store;
  struct llnode *next;
};

int main(void){
  printf("%lu\n",sizeof(int) * 100 + sizeof(struct llnode *) * 101);
  printf("%lu\n",sizeof(struct llnode[100]));
}
