'''
import array
arr=array.array('i',[])
print(arr,type(arr))
arr.append(10)
arr.append(20)  
arr.append(30)
print(arr)
arr.insert(2,25)
print(arr)
'''
'''
 li=[12,25.4,3+5j,"Hello",12,25.4]
li.append("World")
print(li[::-1])
li.append(100)
print(li)
li.insert(2,"Python")
print(li)
li.insert(-20,"python")
print(li)
'''
#read the number from user and display number of digits in number
'''
input:1234
output:4
'''
'''
n=int(input())
count=0
while n>0:
    n=n
    count+=1
    
print(count)
'''
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr))
print(np.zeros(5))
print(np.ones(5))
print(np.arange(1,10,2))
n=int(input())
ele=list(map(int,input("enter elements: ").split()))
print(ele)
