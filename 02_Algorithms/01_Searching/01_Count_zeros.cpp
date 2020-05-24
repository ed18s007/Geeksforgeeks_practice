/*you are required to complete this method*/
int countZeroes(int A[MAX][MAX],int N)
{
//Your code here
int cnt=0;
for(int  i=0;i<N;i++){
    int j=0;
    while(j<N){
        if(A[i][j]==0){
            cnt =cnt+ 1;
        }
        if(A[i][j]==1){
            j=N;
        }
        j = j+1;
    }
}
return cnt;
}