
# Question-1 Input using Decorator

def ArmstrongNum(InputFunction):
    print(".Enter the Interval values.")

    def Calculate():
        start,end=InputFunction()
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
    return Calculate

@ArmstrongNum
def Values():
    start=input("Starting Number:")
    end=input("Ending Number:")
    return int(start),int(end)
Values()


# Question-2 Exception Handling

file1=open("D:\JavaScript\Codes\index.js","r")

try:
    file1=write("Lets add some text")
except NameError:
    print(("Check the mode of operation of this file").upper())
finally:
    print(("I love Assignments").upper())

raise Warning("You have opened the file in READ ONLY option")
