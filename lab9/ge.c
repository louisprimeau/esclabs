#include <stdlib.h>
#include <stdio.h>
int print(float *m, int rows, int cols){
  int i = 0;
  int j = 0;

  for(i=0;i<rows;i++){
    for(j=0;j<cols;j++){
      printf("%f ",m[i*cols + j]);
    }
    printf("\n");
  }
  printf("\n");
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

  if(matrix_out[0] == 0.0){return(1);}

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
      matrix_out[(i+1)*(cols) + (j+1)] = submatrixhold[i*(cols-1) + j];
    }
  }

  return(1);
}

int ge_bw(float *matrix, int rows, int cols, float *matrix_out){
  int i = 0;
  int j = 0;
  float *submatrix= NULL;
  float *submatrixhold = NULL;
  float *hold = NULL;
  float f = 0.0;
  int lastnonzero = 0.0;
  int firstelement = 0.0;

  //Checks:
  if(matrix_out == NULL){
    return(-1);
  }
  else if(matrix_out == NULL){
    return(-1);
  }

  //Initialize matrix_out
  for(i = 0; i < rows; i++){
    for(j = 0; j < cols; j++){
      matrix_out[cols*i + j] = matrix[cols*i + j];
    }
  }

  if(rows <= 1){
    return(0);
  }
  print(matrix,rows,cols);
  lastnonzero = 0;
  firstelement = 0;
  for(i = 0; i < rows; i++){
    for(j = cols; j >= 0; j--){
      if(matrix_out[i*cols + j] != 0.0){
        lastnonzero = i;
        firstelement = j;
      }
    }
  }
  print(matrix,rows,cols);
  for(i = 0;i<cols;i++){ //Normalize last nonzero row
    matrix_out[lastnonzero*cols + i] = matrix_out[lastnonzero*cols + i] / matrix_out[lastnonzero*cols + firstelement];
  }

  for(i=0;i<lastnonzero;i++){ //Zero out nonzero row lead zero column
    for(j=0;j<cols;j++){
      matrix_out[i*cols + j] = matrix_out[i*cols + j] - (matrix_out[cols * i + firstelement] / matrix_out[lastnonzero*cols + firstelement]) * matrix_out[lastnonzero*cols+j];
    }
  }

  submatrix = (float *)malloc((rows-1)*(cols-1)*sizeof(float)); //assign submatrix memory stuff
  submatrixhold = (float *)malloc((rows-1)*(cols-1)*sizeof(float));

  //Assign submatrix
  for(i=0;i < lastnonzero; i++){
    for(j=0;j < firstelement;j++){
      f = (float)matrix_out[i*cols + j];
      submatrix[i*(cols-1) + j] = (float)f;
    }
    for(j=firstelement + 1;j<rows;j++){
      submatrix[i*cols + (j-1)] = matrix_out[i*cols + j];
    }
}
  print(submatrix,rows-1,cols-1);
  for(i=lastnonzero + 1;i < rows; i++){
    for(j=0;j< firstelement;j++){
      submatrix[(i-1)*cols + j] = matrix_out[i*cols + j];
    }
    for(j=firstelement + 1;j<rows;j++){
      submatrix[(i-1)*cols + (j-1)] = matrix_out[i*cols + j];
    }
  }

  ge_bw(submatrix,rows-1,cols-1,submatrixhold);
  print(matrix,rows,cols);
  for(i=0;i<lastnonzero;i++){
    for(j=1;j<firstelement;j++){
      matrix_out[i*cols + j] = submatrixhold[i*(cols-1) + j];
    }
    for(j=firstelement + 1;j<cols;j++){
      matrix_out[i*cols + j] = submatrixhold[i*(cols-1) + (j-1)];
    }
  }
  for(i=0 + 1;i<rows;i++){
    for(j=1; j<firstelement;j++){
      matrix_out[(i+lastnonzero+1)*cols + j] = submatrixhold[i*(cols-1) + j];
    }
    for(j=firstelement + 1;j<cols;j++){
      matrix_out[(i+lastnonzero+1)*cols + j] = submatrixhold[i*(cols-1) + (j-1)];
    }
  }
  print(matrix,rows,cols);
  print(matrix_out,rows,cols);

  return(1);
}
