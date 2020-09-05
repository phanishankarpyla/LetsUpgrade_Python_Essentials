start=1042000
end=702648265
#print(len(str(start)));
for i in range(start,end):
    length=len(str(i))
    num,sum1=i,0
    while num>0:
        digit=num%10
        sum1+=digit**length
        num//=10
    if sum1==i:
        print("The first armstrong number is: ",i)
        break
    else:
        continue
