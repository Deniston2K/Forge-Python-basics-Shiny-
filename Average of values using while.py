n=1
sum1=0
print("Enter 5 values")
while n<=5:
    number=int(input())
    sum1=sum1+number
    n=n+1

average=sum1/(n-1)
print(average)