int main(void){return(0);}
int fibo3(int n){
  if(n == 0 || n == 1 || n == 2){
    return(1);
  }else{
    return(fibo3(n-1));
  }
}
