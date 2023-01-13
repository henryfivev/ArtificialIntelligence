newgame = 'y'
while (newgame == 'y'):
    correct_input = 0
    while (correct_input != 1):
        s1 = input("Player1 input:")
        s2 = input("Player2 input:")
        correct_input = 1
        if (s1 != "Rock" and s1 != "Scissors" and s1 != "Paper"):
            print("Player1请输入正确的单词\n")
            correct_input = 0
        if (s2 != "Rock" and s2 != "Scissors" and s2 != "Paper"):
            print("Player2请输入正确的单词\n")
            correct_input = 0


    if (s1 == s2):
        print("Draw")
    elif ((s1 == "Rock" and s2 == "Scissors")or\
        (s1 == "Scissors" and s2 == "Paper")or\
        (s1 == "Paper" and s2 == "Rock")):
        print("Congratulate Player1!")
    elif ((s2 == "Rock" and s1 == "Scissors")or\
        (s2 == "Scissors" and s1 == "Paper")or\
        (s2 == "Paper" and s1 == "Rock")):
        print("Congratulate Player2!")
    print("Try new game?",end="")
    newgame = input("y/n ")
    print("")