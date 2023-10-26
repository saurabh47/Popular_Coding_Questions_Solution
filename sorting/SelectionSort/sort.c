#include<stdio.h>

int main(int argc,char *argv[]){
//	printf("%c",argv[1][1]);
	int n=sizeof(argv[1])/2;
	char arr[n];	
//	printf("%d",sizeof(argv[1]));
	int k=0;
	for(int i=0;i<n;i++){
		if(argv[1][i]!='a'||argv[1][i]!='e'||argv[1][i]!='i' || argv[1][i]!='o' || argv[1][i]!='u'){
				arr[k]=argv[1][i];
				k++;	
		}
	}
	for(int i=0;i<sizeof(arr)/2;i++){
		printf("%c",arr[i]);		
	}

	return 0;
}
