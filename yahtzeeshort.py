import random
play = 'yes'
yn = ['y', 'n']

def rules(yesorno = ['yes', 'no','y','n']):
    rule = input("Do you want to see the rules of the game (probably a little different than normal Yahtzee)? yes or no? ")
    if rule == 'yes':
        rule = 'y'
    while rule not in yesorno:
        print("Please type yes or no (you can also type y or n)")
        rule = input("\nDo you want to see the rules of the game? yes or no? ")
    if rule == 'y':
        print("\nEach player has 5 dice and rolls 3 times. The first two times you can select which dice you want to keep,")
        print("the other dice will be rolled again. The dice you keep cannot be rolled again (for now, I will add that feature in the future).")
        print("The dice will be added for points and you can earn extra points by getting certain combinations:")
        print("")
        print("2 of a kind (pair) is 5 extra points.")
        print("2 pairs is 10 extra points.")
        print("3 of a kind is 15 extra points.")
        print("4 of a kind is 20 extra points.")
        print("A full house (a pair and a 3 of a kind) is 25 extra points.")
        print("A low straight(1 to 5) is 30 extra points.")
        print("A high straight(2 to 6) is 35 extra points.")
        print("A Yahtzee(5 of the same) is 50 extra points.")
        print("Good luck!")
        input("Press Enter to go back to the game..")

def roll():
    dye = random.randint(1,6)
    return dye

def turn1():
    keep = []
    input("First roll, please press Enter to roll your dice....")
    dye1 = roll()
    dye2 = roll()
    dye3 = roll()
    dye4 = roll()
    dye5 = roll()
    diceroll = [dye1,dye2,dye3,dye4,dye5]
    print("You've rolled:",diceroll)
    for dye in diceroll:
        print("Do you want to keep this dye:",dye,"? (y)es or (n)o:")
        yorn = input()
        while yorn not in yn:
            print("Please type y or n")
            print("Do you want to keep this dye:",dye,"? (y)es or (n)o:")
            yorn = input()
        if yorn == 'y':
            keep.append(dye)
    return keep

def keepdice():
    length = len(keep)
    dye1 = roll()
    dye2 = roll()
    dye3 = roll()
    dye4 = roll()
    dye5 = roll()
    if length == 0:
        diceroll = [dye1,dye2,dye3,dye4,dye5]
    elif length == 1:
        diceroll = [dye1,dye2,dye3,dye4]
    elif length == 2:
        diceroll = [dye1,dye2,dye3]
    elif length == 3:
        diceroll = [dye1,dye2]
    elif length == 4:
        diceroll = [dye1]
    print("You've rolled:",diceroll)
    if turn < 3:
        for dye in diceroll:
            print("Do you want to keep this dye:",dye,"? (y)es or (n)o:") 
            yorn = input()
            while yorn not in yn:
                print("Please type y or n")
                print("Do you want to keep this dye:",dye,"? (y)es or (n)o:")
                yorn = input()
            if yorn == 'y':
                keep.append(dye)
    else:
        for dye in diceroll:
            keep.append(dye)
    return keep

def turn2():
    input("Second roll, please press Enter to roll your dice....")
    keepdice()
    return keep

def turn3():
    input("Final roll, please press Enter to roll your dice....")
    keepdice()
    return keep

def score1():
    score1 = sum(keep)
    print("First we add all dice together: Your first score is:",score1)
    input("Press Enter to continue...")
    return score1

def score2():
    score2 = 0
    keep.sort()
    print(keep)
    if len(set(keep)) == 1:
        print("Yahtzee!!! You've got 5 equal dice! That's 50 extra points!")
        score2 += 50

    elif len(set(keep)) == 2:
        if keep[0] == keep[3] or keep[1] == keep[4]:
            print("You have four of a kind! That's 20 points extra!")
            score2 += 20
        else:
            score2 += 25
            print("You have a full house! You've scored 25 extra points!")

    elif len(set(keep)) == 5:
        if sum(keep) == 20:
            print("You have a high straight! That's 35 extra points!")
            score2 += 35
        elif sum(keep) == 15:
            print("You have a low straight! That's 30 extra points!")
            score2 += 30
        else:
            print("You have nothing, no extra points...")

    elif len(set(keep)) == 3:
        if keep[0] == keep[2] or keep[1] == keep[3] or keep[2] == keep[4]:
            score2 += 15
            print("You have three of a kind! That's 15 extra points!")
        else:
            score2 += 10
            print("You have 2 pairs! That's 10 extra points!")
    else:
        score2 += 5
        print("You have one pair, that's 5 extra points!")
    input("Press Enter to continue...")
    return score2

def newgame(yesorno = ['yes', 'no']):
    play = input("Do you want to play another game? yes or no? ")
    while play not in yesorno:
        print("Please type yes or no")
        play = input("Do you want to play another game? yes or no? ")
    if play == 'yes':
        print("Great! Have fun!")
    return play

def gameresult3p():
    scorelist = [player1total,player2total,player3total]
    scorelist.sort()
    if player1total == scorelist[2]:
        print("Player 1 won this game!!!")
        if player2total == scorelist[1]:
            print("Player 2 is second this game!")
            print("Player 3 is last this game.")
        elif player3total == scorelist[1]:
            print("Player 3 is second this game!")
            print("Player 2 is last this game.")
    elif player2total == scorelist[2]:
        print("Player 2 won this game!!!")
        if player1total == scorelist[1]:
            print("Player 1 is second this game!")
            print("Player 3 is last this game.")
        elif player3total == scorelist[1]:
            print("Player 3 is second this game!")
            print("Player 1 is last this game.")
    else:
        print("Player 3 won this game!!!")
        if player1total == scorelist[1]:
            print("Player 1 is second this game!")
            print("Player 2 is last this game.")
        elif player2total == scorelist[1]:
            print("Player 2 is second this game!")
            print("Player 1 is last this game.")

def roundresult():
    scorelist = [player1score,player2score,player3score]
    scorelist.sort()
    if player1score == scorelist[2]:
        print("Player 1 won this round!")
        if player2score == scorelist[1]:
            print("Player 2 is second this round")
            print("Player 3 is last this round.")
        elif player3score == scorelist[1]:
            print("Player 3 is second this round")
            print("Player 2 is last this round.")
    elif player2score == scorelist[2]:
        print("Player 2 won this round!")
        if player1score == scorelist[1]:
            print("Player 1 is second this round")
            print("Player 3 is last this round.")
        elif player3score == scorelist[1]:
            print("Player 3 is second this round")
            print("Player 1 is last this round.")
    else:
        print("Player 3 won this round!")
        if player1score == scorelist[1]:
            print("Player 1 is second this round")
            print("Player 2 is last this round.")
        elif player2score == scorelist[1]:
            print("Player 2 is second this round")
            print("Player 1 is last this round.")

print("\nWelcome to Yahtzee lite by Jeroen Penders\n")
rules()
while play == 'yes':
    player1score = 0
    player1total = 0
    player2score = 0
    player2total = 0
    player3score = 0
    player3total = 0
    counter = 0
    try:
        players = int(input("\nHow many players? (min 1, max 3): "))
        while players < 1: 
            print("Please enter a number from 1 to 3")
            players = int(input("How many players? (min 1, max 3): "))
            while players > 3:
                print("Please enter a number from 1 to 3")
                players = int(input("How many players? (min 1, max 3): "))
        while players > 3:
            print("Please enter a number from 1 to 3")
            players = int(input("How many players? (min 1, max 3): "))
            while players < 1: 
                print("Please enter a number from 1 to 3")
                players = int(input("How many players? (min 1, max 3): "))
    except ValueError:
        print("Please enter a number from 1 to 3")
        continue    
    print("\nGreat, a",players,"Player game!\n")
    try:
        rounds = int(input("Please enter how many rounds you want this game to last (min 1, max 10 rounds): "))
        while rounds < 1: 
            print("Please enter a number from 1 to 10")
            rounds = int(input("Please enter how many rounds you want this game to last (min 1, max 10 rounds): "))
            while rounds > 10:
                print("Please enter a number from 1 to 10")
                rounds = int(input("Please enter how many rounds you want this game to last (min 1, max 10 rounds): "))
        while rounds > 10:
            print("Please enter a number from 1 to 10")
            rounds = int(input("Please enter how many rounds you want this game to last (min 1, max 10 rounds): "))
            while rounds < 1: 
                print("Please enter a number from 1 to 10")
                rounds = int(input("Please enter how many rounds you want this game to last (min 1, max 10 rounds): "))
    except ValueError:
        print("Please enter a number from 1 to 10")
        continue   
    print("\nNice! A",rounds,"round game! Let's begin.\n") 
    if players == 1:
        while rounds > counter:
            turn = 0
            player1score = 0
            counter += 1
            turn = turn + 1
            keep = turn1()
            if len(keep) == 5:
                print("Wow! So you got lucky with the first roll?")
            else:
                print("The dice you've kept so far:",keep)
                turn = turn + 1
                turn2()
                if len(keep) == 5:
                    print("So, you got lucky the first two rolls?")
                else:
                    print("The dice you've kept so far:",keep)
                    turn = turn + 1
                    turn3()
            print("Your final result is:",keep)
            player1score = player1score + score1()
            player1score = player1score + score2()
            player1total = player1total + player1score
            print("You've scored",player1score,"points this round!!")
            player1score = 0
            if rounds > counter:
                input("Press Enter to start next round...")
        input("Press Enter to see your total points...")
        print("Your total score of this",rounds,"round game is",player1total,"points!\n")

    elif players == 2:
        while rounds > counter:
            turn = 0
            counter += 1 
            print("Player 1 goes first")
            turn = turn + 1
            keep = turn1()
            if len(keep) == 5:
                print("Wow! So you got lucky with the first roll?")
            else:
                print("The dice you've kept so far:",keep)
                turn = turn + 1
                turn2()
                if len(keep) == 5:
                    print("So, you got lucky the first two rolls?")
                else:
                    print("The dice you've kept so far:",keep)
                    turn = turn + 1
                    turn3()

            print("Your final result for this round is:",keep)
            player1score = player1score + score1()
            player1score = player1score + score2()
            player1total = player1total + player1score
            print("You've scored",player1score,"points!!")
            print("Now it's time for player 2 to set a score!")
            input("Press Enter to continue when player 2 is ready...")
            turn = 0
            player2score = 0
            turn = turn + 1
            keep = turn1()
            if len(keep) == 5:
                print("Wow! So you got lucky with the first roll?")
            else:
                print("The dice you've kept so far:",keep)
                turn = turn + 1
                turn2()
                if len(keep) == 5:
                    print("So, you got lucky the first two rolls?")
                else:
                    print("The dice you've kept so far:",keep)
                    turn = turn + 1
                    turn3()

            print("Your final result for this round is:",keep)
            player2score = player2score + score1()
            player2score = player2score + score2()
            player2total = player2total + player2score
            print("You've scored",player2score,"points!!")
            input("Press Enter to see this rounds results...")
            print("The results of this round are: Player 1:",player1score,"points and Player 2:",player2score,"points.")
            if player1score == player2score:
                print("The round is a draw!!")
            elif player1score > player2score:
                print("Player 1 won this round!")
            else:
                print("Player 2 won this round!")
            player1score = 0
            player2score = 0
            if rounds > counter:
                input("Press Enter to start next round...")
        input("Press Enter to see who won the game")
        print("The total scores of this",rounds,"round game are Player1:",player1total,"points and Player 2:",player2total,"points.\n")

        if player1total == player2total:
                print("The game is a draw!!")
        elif player1total > player2total:
                print("Player 1 won this game!")
        else:
            print("Player 2 won this game!")

    elif players == 3:
        while rounds > counter:
            turn = 0
            counter += 1 
            print("Player 1 sets his score first for this round.")
            turn = turn + 1
            keep = turn1()

            if len(keep) == 5:
                print("Wow! So you got lucky with the first roll?")
            else:
                print("The dice you've kept so far:",keep)
                turn = turn + 1
                turn2()
                if len(keep) == 5:
                    print("So, you got lucky the first two rolls?")
                else:
                    print("The dice you've kept so far:",keep)
                    turn = turn + 1
                    turn3()

            print("Your final result for this round is:",keep)
            player1score = player1score + score1()
            player1score = player1score + score2()
            player1total = player1total + player1score
            print("You've scored",player1score,"points!!")

            print("Now it's time for player 2 to set a score!")
            input("Press Enter to continue when player 2 is ready...")
            player2score = 0
            turn = 0
            turn = turn + 1
            keep = turn1()
            if len(keep) == 5:
                print("Wow! So you got lucky with the first roll?")
            else:
                print("The dice you've kept so far:",keep)
                turn = turn + 1
                turn2()
                if len(keep) == 5:
                    print("So, you got lucky the first two rolls?")
                else:
                    print("The dice you've kept so far:",keep)
                    turn = turn + 1
                    turn3()

            print("Your final result for this round is:",keep)
            player2score = player2score + score1()
            player2score = player2score + score2()
            player2total = player2total + player2score
            print("You've scored",player2score,"points!!")
            print("Now it's player 3's turn to set a score!")
            input("Player 3, press Enter when you are ready...")
            player3score = 0
            turn = 0
            turn = turn + 1
            keep = turn1()
            if len(keep) == 5:
                print("Wow! So you got lucky with the first roll?")
            else:
                print("The dice you've kept so far:",keep)
                turn = turn + 1
                turn2()
                if len(keep) == 5:
                    print("So, you got lucky the first two rolls?")
                else:
                    print("The dice you've kept so far:",keep)
                    turn = turn + 1
                    turn3()

            print("Your final result for this round is:",keep)
            player3score = player3score + score1()
            player3score = player3score + score2()
            player3total = player3total + player3score
            print("You've scored",player3score,"points!!")
            roundresult()
            if rounds > counter:
                input("Press Enter to start next round...")

            player1score = 0
            player2score = 0
            player3score = 0
        input("Press Enter to see who won the game...\n")
        print("The total scores of this",rounds,"round game are: Player 1:",player1total,"points, Player 2:",player2total,"points and Player 3:",player3total,"points.\n")
        gameresult3p()
    play = newgame() 

print("\nThank you for playing my simple take on Yahtzee, I will likely improve on this, so keep asking me for updates!")
print("I might add features like more players and a better scoring system, and maybe even some graphics in the future (When I don't suck at coding anymore).")
print("And for coders, sorry for my unorthodox style of coding (I'm just a beginner), but it works!      (c) Jeroen Penders 17-05-'21\n")    
