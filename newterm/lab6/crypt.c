unsigned char prng(unsigned char x, unsigned char pattern) {
  unsigned char output = (((x & 0x1) << 7) | (x >> 1)) ^ pattern;
  return(output);
}
int crypt(char *data,unsigned int size,unsigned char password) {
  int i;
  for(i = 0; i < size; i++){
    data[i] ^= prng(password, 0xb8);
  }
  return(0);
}
