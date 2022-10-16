def suy (arr,n):
    c1=0
    c2=0
    for i in range(0,n):
        if(arr[i]==0):
            c1=c1+1
        else:
            c2=c2+1
arr=[0,0,0,1,0,0,1,1,1,0,0,1,0,0,1,0,1]
n=len(arr)
suy(arr,n)
