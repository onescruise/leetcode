#include<stdio.h>
#include<math.h>
#include <stdlib.h>
int main() {
  int x=1534236469;
  int flag=1; if(x<0)flag=-1;
  x=abs(x);
  int rex=0;
  
  while(x){
  	rex=rex*10+x%10;
  	x/=10;
  }
  
  rex*=flag;
  if(rex>=-1*pow(2,31)&&rex<=(pow(2,31)-1)){
  	printf("%d\n",rex);
  }
  else return 0;
  
}
