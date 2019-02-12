#include <stdio.h>
struct blah{
    int id;
    int val[4];
    char label[4];
    int *data;
};
typedef struct blah blah;
int main(void){
  printf("%lu\n",sizeof(blah));
  printf("%lu\n",sizeof(int) + sizeof(int[4]) + sizeof(char[4]) + sizeof(int*));
}
