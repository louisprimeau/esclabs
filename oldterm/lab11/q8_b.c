#include <stdlib.h>
#include <stdio.h>
struct poly{
  int n;
  float *coefficients;
};

float integrate(struct poly *a){
  if(a == NULL){return(-1);}
  int i = 0;
  for(i=0;i<a->n;i++){
    (a->coefficients)[i] = (a->coefficients)[i] / (a->n-i);
  }
  return(0);
}


int main(void){
  int i = 0;
  float coefficents[] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f};
  struct poly a = {
    .n = 5,
    .coefficients = coefficents
  };
  integrate(&a);
  for(i=0;i<5;i++){
    printf("%f \n", (a.coefficients)[i]);
  }
}
