#include <stdio.h>
#include <stdlib.h>
struct histbin{
  int valid;
  int value;
  int frequency;
};
int getmode(struct histbin *m, int *mode){
  int i = 0;
  int bigfreq = 0;
  int bigval = 0;
  if(m == NULL || mode == NULL){return(-1);}
  while((m[i]).valid != 0){
    if(bigfreq < (m[i]).frequency){
      bigval = (m[i]).value;
      bigfreq = (m[i]).frequency;
    }
  }
  *mode = bigval;
  return(0);
}

int main(void){return(0);}
