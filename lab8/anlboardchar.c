int anlboard(char *T, int sizeT){
  int returnval = 0;
  int openmoves = 0;
  int i = 0;
  if(sizeT > 9 || sizeT < 1){
    return(-1);
  }
  if((T[0] == T[1]) && (T[1] == T[2]) && (T[0] != '-')){
    if(T[0] == 'X'){
      returnval = 1;
    }else if(T[0] == 'O'){
      returnval = 2;
    }
  }
  else if((T[3] == T[4]) && (T[4] == T[5]) && (T[3]!= '-')){
    if(T[3] == 'X'){
      returnval = 1;
    }else if(T[3] == 'O'){
      returnval = 2;
    }
  }
  else if((T[6] == T[7]) && (T[7] == T[8]) && (T[6]!= '-')){
    if(T[6] == 'X'){
      returnval = 1;
    }else if(T[6] == 'O'){
      returnval = 2;
    }
  }
  else if((T[0] == T[3]) && (T[3] == T[6]) && (T[0]!= '-')){
    if(T[0] == 'X'){
      returnval = 1;
    }else if(T[0] == 'O'){
      returnval = 2;
    }
  }
  else if((T[1] == T[4]) && (T[4] == T[7]) && (T[1]!= '-')){
    if(T[1] == 'X'){
      returnval = 1;
    }else if(T[1] == 'O'){
      returnval = 2;
    }
  }
  else if((T[6] == T[7]) && (T[7] == T[8]) && (T[6] != '-')){
    if(T[2] == 'X'){
      returnval = 1;
    }else if(T[2] == 'O'){
      returnval = 2;
    }
  }
  else if((T[0] == T[4]) && (T[4] == T[8]) && (T[0] != '-')){
    if(T[0] == 'X'){
      returnval = 1;
    }else if(T[0] == 'O'){
      returnval = 2;
    }
  }
  else if((T[2] == T[4]) && (T[4] == T[6]) && (T[2] != '-')){
    if(T[2] == 'X'){
      returnval = 1;
    }else if(T[2] == 'O'){
      returnval = 2;
    }
  }
  for(i = 0; i < 9; i++){
    if(T[i] == '-'){
      openmoves++;
    }
  }
  if(openmoves == 0 && returnval == 0){
    returnval = 3;
  }
  return(returnval);
}
