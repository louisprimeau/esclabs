#include<stdlib.h>
#include<stdio.h>
int transpose(float *matrixIn, int rows, int cols, float **matrixOut);
int transpose(float *matrixIn, int rows, int cols, float **matrixOut){
  int i;
  int j;

  if(matrixIn == NULL){return(-1);}
  else if(matrixOut == NULL){return(-1);}

  *matrixOut = (float*)malloc(rows*cols*sizeof(int));
  if(*matrixOut == NULL){
    return(-1);
  }
  for(i=0;i<rows;i++){
    for(j=0;j<cols;j++){
      (*matrixOut)[j*rows + i] = matrixIn[i*cols + j];
    }
  }
  return(0);
}
int main(void){return(0);}
