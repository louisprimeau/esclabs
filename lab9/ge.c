#include <stdio.h>
#include <stdlib.h>
int ge_fw();
int print();
int main(void){
  float x[3*3] = {1,5,1,2,4,3,3,9,4};
  float y[3*3] = {0,0,0,0,0,0,0,0,0};
  int i = 0;
  int j = 0;

  ge_fw(x,3,3,y);
  print(x,3,3);
  print(y,3,3);
  return(0);
}
int print(float *m, int rows, int cols){
  int i = 0;
  int j = 0;

  for(i=0;i<rows;i++){
    for(j=0;j<cols;j++){
      printf("%f ",m[i*cols + j]);
    }
    printf("\n");
  }
  return(1);
}
int ge_fw(float *matrix, int rows, int cols, float *matrix_out){
  int i = 0;
  int j = 0;
  float *submatrix= NULL;
  float *submatrixhold = NULL;
  float *hold = NULL;

  //Checks:
  if(matrix == NULL){
    return(-1);
  }
  else if(matrix_out == NULL){
    return(-1);
  }

  //Copy matrix into matrix_out:

  for(i = 0; i < rows; i++){
    for(j = 0; j < cols; j++){
      matrix_out[cols*i + j] = matrix[cols*i + j];
    }
  }

  //STEP 1:
  for(i = 0; i<rows; i++){
    if(matrix_out[cols*i] != 0.0){

      hold = (float *)malloc(cols * sizeof(float));
      for(j=0; j<cols; j++){
        hold[j] = matrix_out[i*cols + j];
        matrix_out[j] = matrix_out[i*cols + j];
      }
      for(j=0; j<cols;j++){
        matrix_out[i*cols + j] = hold[j];
      }

      break;
    }
  }
  if(matrix_out[0] == 0.0){return(0);}

  //STEP 2:

  for(i=1;i<rows;i++){
    for(j=1;j<cols;j++){
        matrix_out[cols*i + j] = matrix_out[cols*i + j] - matrix_out[cols*i] / matrix_out[0] * matrix_out[j];
    }
    matrix_out[cols*i] = 0;
  }
  //STEP 3:

  //Make Submatrix
  submatrix = (float *)malloc((rows-1)*(cols-1)*sizeof(float));
  submatrixhold = (float *)malloc((rows-1)*(cols-1)*sizeof(float));
  for(i=1;i<rows;i++){
    for(j=1;j<cols;j++){
      submatrix[(i-1)*(cols-1) + (j-1)] = matrix_out[i * cols + j];
    }
  }

  //Assign it
  ge_fw(submatrix, rows-1,cols-1, submatrixhold);

  //Stick it in matrix_out
  for(i=0; i<(rows-1); i++){
    for(j=0; j<(cols-1); j++){
      matrix_out[(i+1)*cols + (j+1)] = submatrixhold[i*cols + j];
    }
  }

  return(1);
}
