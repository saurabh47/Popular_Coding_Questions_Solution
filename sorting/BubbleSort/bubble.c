#include<stdio.h>

void swap(int *a,int *b){
	int c = *a;
	*a = *b;
	*b = c;
}

int main(int argc,char *argv[]){
	if(argc==1)
		return 0;
	int arr[argc-1];
	int i =0;
	int n=argc-1,j=0;
	
	for(i=0;i<n;i++){
		arr[i] = atoi(argv[i+1]);	
	}	
	
	for(i=0;i<n-1;i++){
		for(int j=0;j<n-i-1;j++){
			if(arr[j]>arr[j+1]){
				swap(&arr[j],&arr[j+1]);				
			}
		}
	}	

	for(i=0;i<n;i++){
		printf("%d ",arr[i]);
	}
	return 0;
}
