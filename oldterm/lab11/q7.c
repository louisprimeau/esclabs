#include <stdio.h>

int main(void) {
  int *b;
  int **a;
  int c = 10;
  int d = 20;
  int q = 30;
  b = &c;
  a = &b;
  q = **a;
  *b = 0;
  d = c + 100;
  q = q + 100;
  /* HERE */
  printf("a points to %p which is b\nb points to %p which is c\nc: %d,d: %d,q: %d\n",a,b,c,d,q);
  return 0;
}
