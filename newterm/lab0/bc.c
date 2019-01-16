/* This is an example of how to use a linked list as a
 * dynamic container to store data that is input with an
 * unknown number of items.
 *
 * Note how we get the data:
 * -while loop (because the number of iterations is unknown)
 * -scanf returns EOF, or End-Of-File, when "nothing" has been input
 * -for each iteration, we stuff the input data into a linked list
 *
 * Usage:
 * gcc getData.c
 * echo "1 2 3 4 5 6 7 8     9      10" | ./a.out
 * should report 10 items read and dump it out
 * -> white space is ignored (space, tab, return)
 *
 * Assignment:
 * -modify this code so that it handles input "char" data
 *  rather than ints (trivial modification)
 * echo "abcdef" | ./a.out
 * should report 7 items read
 * (white space is representable by the char hence the
 * final return you enter is stored as a char)
 */

#include <stdio.h>
#include <stdlib.h>

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

int main(void) {
   int n=0;
   char value='0';
   char left='0';
   int rvalue=0;
   int success = 0;
   stack *input_list=NULL;
   while (scanf("%c",&value) != EOF) {
      if(value == '{' || value == '(' || value == '['){
        success = push(&input_list,value);
      }

      else if(value == '}' || value == ')' || value == ']'){
        success = pop(&input_list,&left);
        if(success == 0){
          if(!((left == '{' && value == '}') || (left == '(' && value == ')') || (left == '[' && value == ']'))){
            printf("FAIL\n");
            break;
          }
        }else{
          printf("FAIL\n");
          break;
        }
      }

    }
    if(input_list != NULL){
      printf("FAIL\n");
    }else{
      printf("PASS\n");
    }
    return(0);
}
