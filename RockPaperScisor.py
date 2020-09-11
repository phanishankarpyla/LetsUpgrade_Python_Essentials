import random
def game():
    
    BotPoints=0
    UserPoints=0
    UserChoice=1
    def Printing():
        print("Your choice is: ",UserChoice)
        print("Computer choice is: ",computerChoice)
        print("Your points: ",UserPoints)
        print("Bot points: ",BotPoints)
    
    while UserChoice!="0":
        lst=["r","p","s"]
        UserChoice=input("Enter your choice(Rock-r/Paper-p/Scissor-s,to End Game-0):")
        computerChoice=random.choice(lst)
        if UserChoice==computerChoice:
            print("Tie")
            Printing()
            
        elif UserChoice=="r" and computerChoice=="p":
            print("You Lost")
            BotPoints+=1
            Printing()
            
        elif UserChoice=="p" and computerChoice=="r":
            print("You Won")
            UserPoints+=1
            Printing()
            
        elif UserChoice=="p" and computerChoice=="s":
            print("You Lost")
            BotPoints+=1
            Printing()
            
        elif UserChoice=="s" and computerChoice=="p":
            print("You Won")
            UserPoints+=1
            Printing()
            
        elif UserChoice=="s" and computerChoice=="r":
            print("You Lost")
            BotPoints+=1
            Printing()
            
        elif UserChoice=="r" and computerChoice=="s":
            print("You Won")
            UserPoints+=1
            Printing()
        elif UserChoice=="0":
            continue
        else:
            print("Wrong Input!!, Try Again")
            
    if UserPoints>BotPoints:
        print("You Won the Game")
    elif UserPoints<BotPoints:
        print("You Lost The Game")
    else:
        print("Game ended in Tie")
    print("Thanks For Playing")
        

game()
        

           
