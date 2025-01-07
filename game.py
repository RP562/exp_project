import random,time
def result(player_score,player_choice,comp_choice):
    
    if comp_choice == player_choice:
        print ("Its a Tie")
        
    elif (player_choice=='snake' and comp_choice == "water") or (player_choice=='water' and comp_choice == "gun") or (player_choice=='gun' and comp_choice == "snake"):
        print("You Win!!")
        player_score = player_score +1
        return player_score
        
    else:
        print("comp wins")
        player_score = player_score - 1
        return player_score
    


def play_game(rounds):
    choice = ["snake","water","gun"]
    
    print("Welcome to the Game")
    player_score = 0
    for i in range (1, rounds):    
        print ("Round Number :",i)
        print ("Enter your Choice")
        player_choice = input().lower()
        comp_choice = random.choice(choice)
        print ("The computer chooses {}".format(comp_choice) )
        player_score = result(player_score,player_choice,comp_choice)
        time.sleep(2)
    print("Game Over")
    print("Your Total Score:" ,player_score)
    

if __name__=="__main__":
    play_game(6)


