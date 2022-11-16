import random
choices=["Rock","Paper","Scissor"]
while True:
    print("*Start...Rock Paper scissor Game*")
    print("press the number of the round you want to play")
    a=int(input("enter:"))
    you=0
    computer=0
    for i in range(1,a+1):
        print("Round",i,"Start:")
        print("select the option:")
        print("1.Rock","2.Paper","3.Scissor",sep="\n")
        Y=int(input("enter the number of the option:"))
        if Y==1:
            print("you select the Rock")
            Y="Rock"
        elif Y==2:
            print("you Select Paper")
            Y="Paper"
        elif Y==3:
            print("you select the Scissor")
            Y="Scissor"
        else:
            print("invalid choice")
            break
        C=random.choice(choices)
        print("computer select :",C)
        if(Y=="Paper" and C=="Rock") or(Y=="Rock" and C=="Scissor") or (Y=="Scissor" and C=="Paper"):
            You+=1
            print("you won this Round")
        elif Y==C:
            you+=0
            computer+=0
            print("Tie the Round")
        else:
            computer+=1
            print("computer won this Round")
        if you>computer:
            print("you won the Game")
            print("Score:","your score=",you ,"   ",   "computer score=",computer,sep="")
        elif computer>you:
            print("Score","your score=",you , "computer score=",computer,sep="")
            print("you lose the Game//  **Computer won **\\")
        else:
            print("match tie")
            print("score:","Your score=",you,"computer score =",computer,sep="")
            k=int(input("you want to play again: Press 1 for yes, press 2 for NO"))
        if k==1:
            continue
        else:
            print("exit the game")
            break