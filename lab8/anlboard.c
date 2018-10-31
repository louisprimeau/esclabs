int anlboard(int *T, int sizeT){
  int returnval = 0;
  if((sizeT > 9) || (sizeT < 1)){
    returnval = 0;
  }
  else if((T[0] == T[1]) && (T[1] == T[2]) && (T[0] != 0)){
    if(T[0] == 'X'){
      returnval = 1;
    }else if(T[0] == 'O'){
      returnval = 2;
    }
  }
  else if((T[3] == T[4]) && (T[4] == T[5]) && (T[3] != 0)){
    if(T[3] == 'X'){
      returnval = 1;
    }else if(T[3] == 'O'){
      returnval = 2;
    }
  }
  else if((T[6] == T[7]) && (T[7] == T[8]) && (T[6] != 0)){
    if(T[6] == 'X'){
      returnval = 1;
    }else if(T[6] == 'O'){
      returnval = 2;
    }
  }
  else if((T[0] == T[3]) && (T[3] == T[6]) && (T[0] != 0)){
    if(T[0] == 'X'){
      returnval = 1;
    }else if(T[0] == 'O'){
      returnval = 2;
    }
  }
  else if((T[1] == T[4]) && (T[4] == T[7]) && (T[1] != 0)){
    if(T[1] == 'X'){
      returnval = 1;
    }else if(T[1] == 'O'){
      returnval = 2;
    }
  }
  else if((T[2] == T[5]) && (T[5] == T[8]) && (T[2] != 0)){
    if(T[2] == 'X'){
      returnval = 1;
    }else if(T[2] == 'O'){
      returnval = 2;
    }
  }
  else if((T[0] == T[4]) && (T[4] == T[8]) && (T[0] != 0)){
    if(T[0] == 'X'){
      returnval = 1;
    }else if(T[0] == 'O'){
      returnval = 2;
    }
  }
  else if((T[2] == T[4]) && (T[4] == T[6]) && (T[2] != 0)){
    if(T[2] == 'X'){
      returnval = 1;
    }else if(T[2] == 'O'){
      returnval = 2;
    }
  }
  return(returnval) 
}
