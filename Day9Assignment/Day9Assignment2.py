start=1
end=1000
def armstron(start,end):
    for i in range(start,end):
        length=len(str(i))
        num,sum1=i,0
        while num>0:
            digit=num%10
            sum1+=digit**length
            num//=10
        if sum1==i:
            yield i
        else:
            continue
lst_Armstrong=list(armstron(start,end))
print(lst_Armstrong)