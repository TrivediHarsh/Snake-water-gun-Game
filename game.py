import random
print( "welcome to snake, water, gun game \n")
cpoint =0
upoint =0
def game():
    global upoint
    global cpoint
    if (user == 's' and cc == 's'):
        print("\ngame is draw\n")
    elif (user == 's' and cc == 'w'):
        print("\nuser win!\n")
        upoint = upoint + 1
    elif (user == 's' and cc == 'g'):
        print("\ncomputer win!\n")
        cpoint =cpoint+1
    elif (user == 'w' and cc == 'w'):
        print("\ngame is draw\n")
    elif (user == 'w' and cc == 's'):
        print("\ncomputer win!\n")
        cpoint = cpoint + 1
    elif (user == 'w' and cc == 'g'):
        print("\nuser win!\n")
        upoint = upoint + 1
    elif (user == 'g' and cc == 'g'):
        print("\ngame is draw\n")
    elif (user == 'g' and cc == 'w'):
        print("\ncomputer  win!\n")
        cpoint = cpoint + 1
    elif (user == 'g' and cc == 's'):
        print("\nuser win!\n")
        upoint = upoint + 1
    else:
        print("Enter valid charactor")

    return print("user point:-",upoint),print("computer point",cpoint)

gametime  = 0
while(True):
    if(gametime == 5):
        if(upoint > cpoint):
            print(f"\nWinner of this game is user with {upoint} points:-")
        else:
            print(f"\nWinner of this game is computer with {cpoint} points")
        exitloop = input("\nenrer c to continue and e to exit:-")
        if(exitloop == "c"):
            upoint =0
            cpoint =0
            gametime = 0
            continue
        elif(exitloop == "e"):
            break

    user = input("Enter Your choice(s,w,g):-")
    lis = ['s','w','g']
    cc =random.choice(lis)
    print("computer chois is:-",cc)
    game()
    gametime = gametime + 1
    print("\ngame time",gametime,"\n")

