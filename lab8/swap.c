int swap(int *a, int *b){
  int hold = *a;
  *a = *b;
  *b = hold;
  return 1;
}
