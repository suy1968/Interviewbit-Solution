f1 = open("File1.txt",'r')
f2= open("File2.txt",'r')
f3=open("File3.txt",'r')
l1=f1.read().split("\n")
l2=f2.read().split("\n")
l3=f3.read().split("\n")
res=l1+l2+l3
res.sort()
print(res)
f1.close
f2.close
f3.close
