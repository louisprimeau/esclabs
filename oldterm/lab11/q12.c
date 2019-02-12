#include <stdio.h>
#include <stdlib.h>
struct histbin{
  int valid;
  int value;
  int frequency;
};
int main(void){return(0);}
int histogram(int *n, struct histbin *m, int s){
  int i = 0;
  int j = 0;
  if(n == NULL || m == NULL){return(-1);}
  for(i=0;i<s;i++){
    for(j=0;j<s;j++){
      if(n[i] == (m[i]).value && (m[i]).valid == 1){
        (m[i]).frequency += 1;
      }
    }
    for(j=0;j<s;j++){
      if((m[j]).valid != 1){
        (m[j]).valid = 0;
        (m[j]).frequency = 1;
        (m[j]).value = n[j];
      }
    }
  }
  return(0);
}
