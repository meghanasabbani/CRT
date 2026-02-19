'''
sample input:
1234
sample output:
4

sample input:
45
sample output:2

n=int(input())
count=0
while n>0:
    last_digit=n%10
    count+=1
    n=n//10
print(count)


n=int(input())
count=0 
while n>0:
    count+=1
    n=n//10
print(count)
# or                  
print(len(str(n)))
input:
1565
output: 17
 input: 1234
output: 10
'''
'''
n=int(input())
temp=n
s=0
while n>0:
    lastdigit=n%10
    s=s+lastdigit
    n=n//10
print(s)
print(sum(map(int,str(temp))))

n=int(input())
even=0
odd=0
while n>0:
    if n%2==0:
        even+=1
    else:
        odd+=1
    n=n//10
print(even,odd)

n=int(input())
sum=0
while n>0:
    lst_digit=n%10
    sum+=lst_digit
    n=n//10
while sum>9:
    sum=sum%10+sum//10
print(sum)

n=int(input())
while n>9:
    n=sum(map(int,str(n)))
print(n)
'''
n=int(input())
n=str(n)
print(n[::-1])

