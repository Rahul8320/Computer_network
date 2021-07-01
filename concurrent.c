#include<stdio.h>
#include<unistd.h>

int sum;
int main(){
	int i;
	sum=0;
	fork();
	for(i=1;i<=100;i++){
		printf("The value of i is %d \n",i);
		sum += i;
		}
	printf("The sum is %d \n",sum);
}
