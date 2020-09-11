
# Question-1 Sublist

lst1=[1,5,6,4,1,2,5,4,12,1,5,2]
lst2=[3,2,1,5,1,1,5,2,6,9,8,12]
sublst=[1,1,5]

def check(a,b):
    for i in range(len(a)):
        if i==len(a)-1 or i==len(a)-2:
            break
        else:
            for j in range(len(b)):
                if j==len(b)-1 or j==len(b)-2:
                    print("Its Gone")
                    break
                elif a[i]==b[j]:
                    if a[i+1]==b[j+1]:
                        if a[i+2]==b[j+2]:
                            print("Its a Match")
                            break
                else:
                    continue

check(sublst,lst1)
check(sublst,lst2)

# Question-2 Primenumbers with Filter

listP=range(1,2500)
ListRef=[]
def prime(a):
    if a>4:
        for j in range(2,a):
            if a%j==0:
                break
        else:    
            return True
    else:
        return True
            
Primelist=list(filter(prime,listP))
print(Primelist)


# Question-3 Lambda Function

Capital=lambda sentance: print(sentance.upper())
Phrases=["lets go and achieve it","how are you dng","Im impressed"]
list(map(Capital,Phrases))

