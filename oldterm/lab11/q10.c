#include <stdlib.h>
int nsum(float* a, float* b, int n, float** c);
int main(void){return(0);}
int nsum(float* a, float* b, int n, float** c){
  // n is the size of a and b, and therefore c

  int i = 0;
  if(a == NULL || b == NULL || c == NULL){return(-1);}
  *c = (float *)malloc(sizeof(float)*n);
  for(i = 0; i < n; i++){
    (*c)[i] = a[i] + b[i];
  }
  return(0);
}
