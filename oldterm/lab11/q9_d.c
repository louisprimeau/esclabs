#include <stdio.h>
#include <stdlib.h>
int fil(float *matrixIn , int rows , int cols , float **matrixOut);
int fil(float *matrixIn, int rows, int cols, float **matrixOut){
  int i = 0;
  int j = 0;
  if(matrixIn == NULL || matrixOut == NULL){
    return(-1);
  }
  *matrixOut = (float *)malloc(sizeof(int)*rows*cols);
  if(*matrixOut == NULL){return(-1);}
  for(i=0;i<rows;i++){
    for(j=0;j<cols;j++){
      matrixIn[i*rows + cols] = (*matrixOut)[i*rows + cols];
    }
  }
  return(0);
}
int main(void){return(0);}
