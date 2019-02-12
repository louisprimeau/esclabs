#include <stdlib.h>
#include <stdio.h>

struct ll{
  int dat;
  int *next;
};
typedef struct ll ll;

int main(void){
  ll abc;

  abc.next = malloc(*int)(sizeof(int));

  return(0);
}
