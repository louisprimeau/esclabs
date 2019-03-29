int bs(int *x,int size,int (*compare)(int,int)){
  int comparison;
  int i,j;
  while(1){
    comparison = 0;
    for(i = 0; i < size - 1; i++){
      if((*compare)(x[i],x[i+1])){
        j = x[i];
        x[i] = x[i+1];
        x[i+1] = j;
        comparison = 1;
        printarray(x,size);
      }
    }
    if(comparison == 0){
      break;
    }
  }
  return(1);
}

int gt(int x,int y) {
  if(x > y){
    return(1);
  }else{
    return(0);
  }
}
int lt(int x,int y){
  if(x < y){
    return(1);
  }else{
    return(0);
  }
}
