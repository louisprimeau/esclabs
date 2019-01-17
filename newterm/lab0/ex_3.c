#include <stdio.h>
#include <stdlib.h>


struct intlist {
   int *x;
   int end;
   int len;
};

int init(struct intlist *l,int len) {
   if (l==NULL) { return -1; }
   (l->x) = (int *)malloc(len * sizeof(int));
   if ((l->x) == NULL) { return -1; }
   l->end = -1;
   l->len=len;
   return 0;
}

int add_to_end(struct intlist *l,int val){
  int i;
  if(l==NULL){return -1;}
  (l->x)[l->end + 1] = val;
  l->end += 1;
  return(0);

}

int add_to_start(struct intlist *l,int val){
  int i;
  if(l==NULL){return -1;}
  for(i = l->end - 1; i > 0; i--){
    (l->x)[i] = (l->x)[i-1];
  }
  (l->x)[0] = val;
  l->end += 1;
  return(0);
}

int insert_after(struct intlist *l,int insert_val,int val){
  int i;
  if(l==NULL){return -1;}
   for(i = insert_val;i<l->len;i++){
     (l->x)[i+1] = (l->x)[i];
   }
   (l->x)[l->end] = val;
   l->end = l->end + 1;
   return(0);
}

int main(void){
  return(0);
}
