# Question-1 Bank Account

class Account():
    def __init__(self,Holder_Name,Account_ID,Balance):
        self.Holder_Name=Holder_Name
        self.Account_ID=Account_ID
        self.Balance=Balance
    
    def deposit(self,amount):
        self.Balance+=amount
        print ("Transacion Succesfull!\n","Account Older Name: ",self.Holder_Name,"\n Account ID: ",self.Account_ID,"\n Balance: ",self.Balance)

    def withdraw(self,amount):        
        if self.Balance>amount:
            self.Balance-=amount
            print("Transacion Succesfull!\n","Account Older Name: ",self.Holder_Name,"\n Account ID: ",self.Account_ID,"\n Balance: ",self.Balance)
        else:
            print("Transaction Failed : Insuffiecient Funds in your Account, Please Try again!")

MyAccount=Account("Phani",212121,20000)
active=1
while active!="n":
    select=input("Press 1 to Deposit\n      2 to Withdraw: ")
    unit=input("Enter the amount: ")
    if select=="1":
        MyAccount.deposit(int(unit))
    elif select=="2":
        MyAccount.withdraw(int(unit))
    else:
        print("Invalid input, Try Again!")
    active=input("Do you want to continue(y/n):")
else:
    print("\nThank you for using our service\n")


# Question-2 Cone Class

class cone():
    def __init__(self,color,radius,height):
        self.color=color
        self.radius=radius
        self.height=height
    
    def volume(self):
        Vol=(3.14*self.radius**2)*self.height/3
        return Vol
    
    def surface_area(self):
        Ar=3.14*self.radius*(self.radius+((self.height**2+self.radius**2)**(1/2)))
        return Ar

MyCone=cone("Red",10,10)
Area_MyCone=MyCone.surface_area()
Vol_MyCone=MyCone.volume()
print("Surface Area of Cone:",Area_MyCone,"\nVolume of the Cone:",Vol_MyCone)
