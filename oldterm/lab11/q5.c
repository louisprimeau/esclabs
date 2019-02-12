#include<stdlib.h>
int g(char **a, int mem);
int g(char **a, int mem){
  *a = (char*)malloc(sizeof(char)*mem);
  return(0);
}
int main(void){}
