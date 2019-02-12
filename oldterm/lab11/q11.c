int isPrime(int a){
  int i;
  if(a <= 1){return(-1);}
  for(i=2;i<a;i++){
    if(i % a == 0){return(-1);}
  }
  return(0);
}
int isPrimeProduct(int a){
  int i;
  int j;
  for(i = 0; i<a; i++){
    for(j = 0; j < a; j++){
      if(i * j == a && isPrime(i) == 0 && isPrime(j) == 0){
        return(-1);
      }
    }
  }
  return(0);
}
int main(void){return(0);}
