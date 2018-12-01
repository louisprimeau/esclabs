/* Write a function that will return the average of an array of floats;
you must use the most general argument type for the array,
and ensure that your code is safe (in the context of our lectures). */
#include <stdio.h>
float avg(float *arr,int size){
  int average;
  int i;
  for(i = 0; i < size; i++){
    average += arr[i];
  }
  return(average/((float)size));
}
int main(void){
  float arr[5] = {1,2,3,4,5};
  printf("%f",avg(arr,5));
  return(0);
}
