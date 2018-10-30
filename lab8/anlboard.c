int anlboard(int *T, int sizeT){
  int returnval = 0;
  if((sizeT > 9) || (sizeT < 1)){
    returnval = 0;
  }
  else if((T[0] == T[1]) && (T[1] == T[2])){
    returnval = 1;
  }
  else if((T[3] == T[4]) && (T[4] == T[5])){
    returnval = 1;
  }
  else if((T[6] == T[7]) && (T[7] == T[8])){
    returnval = 1;
  }
  else if((T[0] == T[3]) && (T[3] == T[6])){
    returnval = 1;
  }
  else if((T[1] == T[4]) && (T[4] == T[7])){
    returnval = 1;
  }
  else if((T[2] == T[5]) && (T[5] == T[8])){
    returnval = 1;
  }
  else if((T[0] == T[4]) && (T[4] == T[8])){
    returnval = 1;
  }
  else if((T[2] == T[4]) && (T[4] == T[6])){
    returnval = 1;
  }
  return(returnval) 
}
