int anlboard(int *T, int sizeT){
  int openmoves = 0;
  int i = 0;
  int returnval = 0;

  if(sizeT > 9 || sizeT < 1){
    return(-1);
  }
  returnval = 0;
  if((T[0] == T[1]) && (T[1] == T[2]) && (T[0] != 0)){
    returnval = T[0];
  }else if((T[3] == T[4]) && (T[4] == T[5]) && (T[3] != 0)){
    returnval = T[3];
  }else if((T[6] == T[7]) && (T[7] == T[8]) && (T[6] != 0)){
    returnval = T[6];
  }else if((T[0] == T[3]) && (T[3] == T[6]) && (T[6] != 0)){
    returnval = T[0];
  }else if((T[1] == T[4]) && (T[4] == T[7]) && (T[1] != 0)){
    returnval = T[1];
  }else if((T[2] == T[5]) && (T[5] == T[8]) && (T[2] != 0)){
    returnval = T[2];
  }else if((T[0] == T[4]) && (T[4] == T[8]) && (T[0] != 0)){
    returnval = T[0];
  }else if((T[2] == T[4]) && (T[4] == T[6]) && (T[2] != 0)){
    returnval = T[2];
  }
  openmoves = 0;
  for(i = 0; i < 9; i++){
    if(T[i] == 0){
      openmoves++;
    }
    /*printf("%d\n",*(&T[i]));*/
  }
  /*printf("%d\n",openmoves);*/
  if(openmoves == 0 && returnval == 0){
    returnval = 3;
  }
  return(returnval);
}
