import random
def gambling(stake , goal , trails):
    win =0

    for i in range(trails):
        money = stake

        while money>0 and money <goal :
            if random.random() <0.5:
                money+=1
            else:
                money-=1

        if money == goal:
            win +=1

    print("No  of wins :" , win)
    print("No of trails :" , trails)
    print("Winning % :" , (win/trails)*100)
    print("Lossing % :", ((trails-win)/trails)*100)






stake = int(input("Enter the stake :"))
goal = int(input("Enter the goal :"))
trails = int(input("Enter the number of times u want to play"))
gambling(stake , goal , trails)
