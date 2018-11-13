#include <stdio.h>
#include <stdlib.h>
#include "ge.c"
int print();
int main(void){
  float x[3*3] = {1,2,3,4,5,6,2,4,1};
  float y[3*3] = {0,0,0,0,0,0,0,0,0};
  float z[3*3] = {0,0,0,0,0,0,0,0,0};
  int i = 0;
  int j = 0;
  ge_fw(x,3,3,y);
  ge_bw(y,3,3,z);
  printf("x is\n");
  print(x,3,3);
  printf("y is\n");
  print(y,3,3);
  printf("z is\n");
  print(z,3,3);
  return(0);
}
