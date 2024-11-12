import os
import random
import time
jatek = input("Mit szeretnél játszan? (xo)\n")
ujra = "y"
while jatek == "xo" and ujra == "y":
    egy = " "
    ketto = " "
    harom = " "
    negy = " "
    ot = " "
    hat = " "
    het = " "
    nyolc = " "
    kilenc = " "
    egyenleg = 20
    os.system('cls')
    print(f"Egyenleg: {egyenleg}\n")
    print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")
    time.sleep(1)

    rakott = []
    robot1 = []
    robot2 = []

    robot1_w = " "
    robot2_w = " "

    turn = 0
    most = random.randint(0,1)
    most_volt = ""

    win = input("Kire szeretnél rakni?(X,O)\n")
    bet = int(input("Mennyit szeretnél rakni? "))

    while bet > egyenleg:
        print("Nem tudsz ennyit rakni.")
        bet = int(input("Mennyit szeretnél rakni? "))

    egyenleg -= bet

    
    
    kezdo = "X"
    masodik = "O"
    #000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    while robot1_w == " " and robot2_w == " " and most == 0:
        most += 1
        most_volt = 0
        while turn in rakott:
            turn = random.randint(1,9)
        rakott.append(turn)
        robot2.append(turn)
        if turn == 1:
            egy = masodik
        elif turn == 2:
            ketto = masodik
        elif turn == 3:
            harom = masodik
        elif turn == 4:
            negy = masodik
        elif turn == 5:
            ot = masodik
        elif turn == 6:
            hat = masodik
        elif turn == 7:
            het = masodik
        elif turn == 8:
            nyolc = masodik
        else:
            kilenc = masodik
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")
        if ((1 in robot1) and (2 in robot1) and (3 in robot1)) or ((4 in robot1) and (5 in robot1) and (6 in robot1)) or ((7 in robot1) and (8 in robot1) and (9 in robot1)) or ((1 in robot1) and (5 in robot1) and (9 in robot1)) or ((3 in robot1) and (5 in robot1) and (7 in robot1)) or ((1 in robot1) and (4 in robot1) and (7 in robot1)) or ((2 in robot1) and (5 in robot1) and (8 in robot1)) or ((3 in robot1) and (6 in robot1) and (9 in robot1)):
            robot1_w = "win"
            robot2_w = "lose"
        elif ((1 in robot2) and (2 in robot2) and (3 in robot2)) or ((4 in robot2) and (5 in robot2) and (6 in robot2)) or ((7 in robot2) and (8 in robot2) and (9 in robot2)) or ((1 in robot2) and (5 in robot2) and (9 in robot2)) or ((3 in robot2) and (5 in robot2) and (7 in robot2)) or ((1 in robot2) and (4 in robot2) and (7 in robot2)) or ((2 in robot2) and (5 in robot2) and (8 in robot2)) or ((3 in robot2) and (6 in robot2) and (9 in robot2)):
            robot1_w = "lose"
            robot2_w = "win"
    
        time.sleep(1)
    #111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    while robot1_w == " " and robot2_w == " " and most == 1:
        most += 1
        most_volt = 1
        turn = random.randint(1,2)
        rakott.append(turn)
        robot1.append(turn)
        if turn == 1:
            egy = kezdo
        elif turn == 2:
            ketto = kezdo
        elif turn == 3:
            harom = kezdo
        elif turn == 4:
            negy = kezdo
        elif turn == 5:
            ot = kezdo
        elif turn == 6:
            hat = kezdo
        elif turn == 7:
            het = kezdo
        elif turn == 8:
            nyolc = kezdo
        else:
            kilenc = kezdo
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")
        if ((1 in robot1) and (2 in robot1) and (3 in robot1)) or ((4 in robot1) and (5 in robot1) and (6 in robot1)) or ((7 in robot1) and (8 in robot1) and (9 in robot1)) or ((1 in robot1) and (5 in robot1) and (9 in robot1)) or ((3 in robot1) and (5 in robot1) and (7 in robot1)) or ((1 in robot1) and (4 in robot1) and (7 in robot1)) or ((2 in robot1) and (5 in robot1) and (8 in robot1)) or ((3 in robot1) and (6 in robot1) and (9 in robot1)):
            robot1_w = "win"
            robot2_w = "lose"
        elif ((1 in robot2) and (2 in robot2) and (3 in robot2)) or ((4 in robot2) and (5 in robot2) and (6 in robot2)) or ((7 in robot2) and (8 in robot2) and (9 in robot2)) or ((1 in robot2) and (5 in robot2) and (9 in robot2)) or ((3 in robot2) and (5 in robot2) and (7 in robot2)) or ((1 in robot2) and (4 in robot2) and (7 in robot2)) or ((2 in robot2) and (5 in robot2) and (8 in robot2)) or ((3 in robot2) and (6 in robot2) and (9 in robot2)):
            robot1_w = "lose"
            robot2_w = "win"
    
        time.sleep(1)
        #222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
    while robot1_w == " " and robot2_w == " " and most == 2:
        most += 1
        while turn in rakott:
            turn = random.randint(1,9)
        rakott.append(turn)
        robot2.append(turn)
        if turn == 1:
            egy = masodik
        elif turn == 2:
            ketto = masodik
        elif turn == 3:
            harom = masodik
        elif turn == 4:
            negy = masodik
        elif turn == 5:
            ot = masodik
        elif turn == 6:
            hat = masodik
        elif turn == 7:
            het = masodik
        elif turn == 8:
            nyolc = masodik
        else:
            kilenc = masodik
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")
        if ((1 in robot1) and (2 in robot1) and (3 in robot1)) or ((4 in robot1) and (5 in robot1) and (6 in robot1)) or ((7 in robot1) and (8 in robot1) and (9 in robot1)) or ((1 in robot1) and (5 in robot1) and (9 in robot1)) or ((3 in robot1) and (5 in robot1) and (7 in robot1)) or ((1 in robot1) and (4 in robot1) and (7 in robot1)) or ((2 in robot1) and (5 in robot1) and (8 in robot1)) or ((3 in robot1) and (6 in robot1) and (9 in robot1)):
            robot1_w = "win"
            robot2_w = "lose"
        elif ((1 in robot2) and (2 in robot2) and (3 in robot2)) or ((4 in robot2) and (5 in robot2) and (6 in robot2)) or ((7 in robot2) and (8 in robot2) and (9 in robot2)) or ((1 in robot2) and (5 in robot2) and (9 in robot2)) or ((3 in robot2) and (5 in robot2) and (7 in robot2)) or ((1 in robot2) and (4 in robot2) and (7 in robot2)) or ((2 in robot2) and (5 in robot2) and (8 in robot2)) or ((3 in robot2) and (6 in robot2) and (9 in robot2)):
            robot1_w = "lose"
            robot2_w = "win"
    
        time.sleep(1)
        #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    while robot1_w == " " and robot2_w == " " and most == 3:
        most += 1
        while turn in rakott:
            turn = random.randint(1,9)
        rakott.append(turn)
        robot1.append(turn)
        if turn == 1:
            egy = kezdo
        elif turn == 2:
            ketto = kezdo
        elif turn == 3:
            harom = kezdo
        elif turn == 4:
            negy = kezdo
        elif turn == 5:
            ot = kezdo
        elif turn == 6:
            hat = kezdo
        elif turn == 7:
            het = kezdo
        elif turn == 8:
            nyolc = kezdo
        else:
            kilenc = kezdo
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")
        if ((1 in robot1) and (2 in robot1) and (3 in robot1)) or ((4 in robot1) and (5 in robot1) and (6 in robot1)) or ((7 in robot1) and (8 in robot1) and (9 in robot1)) or ((1 in robot1) and (5 in robot1) and (9 in robot1)) or ((3 in robot1) and (5 in robot1) and (7 in robot1)) or ((1 in robot1) and (4 in robot1) and (7 in robot1)) or ((2 in robot1) and (5 in robot1) and (8 in robot1)) or ((3 in robot1) and (6 in robot1) and (9 in robot1)):
            robot1_w = "win"
            robot2_w = "lose"
        elif ((1 in robot2) and (2 in robot2) and (3 in robot2)) or ((4 in robot2) and (5 in robot2) and (6 in robot2)) or ((7 in robot2) and (8 in robot2) and (9 in robot2)) or ((1 in robot2) and (5 in robot2) and (9 in robot2)) or ((3 in robot2) and (5 in robot2) and (7 in robot2)) or ((1 in robot2) and (4 in robot2) and (7 in robot2)) or ((2 in robot2) and (5 in robot2) and (8 in robot2)) or ((3 in robot2) and (6 in robot2) and (9 in robot2)):
            robot1_w = "lose"
            robot2_w = "win"
    
        time.sleep(1)
    while robot1_w == " " and robot2_w == " " and most == 4:
        most += 1
        #444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        while turn in rakott:
            turn = random.randint(1,9)
        rakott.append(turn)
        robot2.append(turn)
        if turn == 1:
            egy = masodik
        elif turn == 2:
            ketto = masodik
        elif turn == 3:
            harom = masodik
        elif turn == 4:
            negy = masodik
        elif turn == 5:
            ot = masodik
        elif turn == 6:
            hat = masodik
        elif turn == 7:
            het = masodik
        elif turn == 8:
            nyolc = masodik
        else:
            kilenc = masodik
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")
        if ((1 in robot1) and (2 in robot1) and (3 in robot1)) or ((4 in robot1) and (5 in robot1) and (6 in robot1)) or ((7 in robot1) and (8 in robot1) and (9 in robot1)) or ((1 in robot1) and (5 in robot1) and (9 in robot1)) or ((3 in robot1) and (5 in robot1) and (7 in robot1)) or ((1 in robot1) and (4 in robot1) and (7 in robot1)) or ((2 in robot1) and (5 in robot1) and (8 in robot1)) or ((3 in robot1) and (6 in robot1) and (9 in robot1)):
            robot1_w = "win"
            robot2_w = "lose"
        elif ((1 in robot2) and (2 in robot2) and (3 in robot2)) or ((4 in robot2) and (5 in robot2) and (6 in robot2)) or ((7 in robot2) and (8 in robot2) and (9 in robot2)) or ((1 in robot2) and (5 in robot2) and (9 in robot2)) or ((3 in robot2) and (5 in robot2) and (7 in robot2)) or ((1 in robot2) and (4 in robot2) and (7 in robot2)) or ((2 in robot2) and (5 in robot2) and (8 in robot2)) or ((3 in robot2) and (6 in robot2) and (9 in robot2)):
            robot1_w = "lose"
            robot2_w = "win"
    
        time.sleep(1)
        #55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
    while robot1_w == " " and robot2_w == " " and most == 5:
        most += 1
        while turn in rakott:
            turn = random.randint(1,9)
        rakott.append(turn)
        robot1.append(turn)
        if turn == 1:
            egy = kezdo
        elif turn == 2:
            ketto = kezdo
        elif turn == 3:
            harom = kezdo
        elif turn == 4:
            negy = kezdo
        elif turn == 5:
            ot = kezdo
        elif turn == 6:
            hat = kezdo
        elif turn == 7:
            het = kezdo
        elif turn == 8:
            nyolc = kezdo
        else:
            kilenc = kezdo
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")
        if ((1 in robot1) and (2 in robot1) and (3 in robot1)) or ((4 in robot1) and (5 in robot1) and (6 in robot1)) or ((7 in robot1) and (8 in robot1) and (9 in robot1)) or ((1 in robot1) and (5 in robot1) and (9 in robot1)) or ((3 in robot1) and (5 in robot1) and (7 in robot1)) or ((1 in robot1) and (4 in robot1) and (7 in robot1)) or ((2 in robot1) and (5 in robot1) and (8 in robot1)) or ((3 in robot1) and (6 in robot1) and (9 in robot1)):
            robot1_w = "win"
            robot2_w = "lose"
        elif ((1 in robot2) and (2 in robot2) and (3 in robot2)) or ((4 in robot2) and (5 in robot2) and (6 in robot2)) or ((7 in robot2) and (8 in robot2) and (9 in robot2)) or ((1 in robot2) and (5 in robot2) and (9 in robot2)) or ((3 in robot2) and (5 in robot2) and (7 in robot2)) or ((1 in robot2) and (4 in robot2) and (7 in robot2)) or ((2 in robot2) and (5 in robot2) and (8 in robot2)) or ((3 in robot2) and (6 in robot2) and (9 in robot2)):
            robot1_w = "lose"
            robot2_w = "win"
    
        time.sleep(1)
        #6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
    while robot1_w == " " and robot2_w == " " and most == 6:
        most += 1
        while turn in rakott:
            turn = random.randint(1,9)
        rakott.append(turn)
        robot2.append(turn)
        if turn == 1:
            egy = masodik
        elif turn == 2:
            ketto = masodik
        elif turn == 3:
            harom = masodik
        elif turn == 4:
            negy = masodik
        elif turn == 5:
            ot = masodik
        elif turn == 6:
            hat = masodik
        elif turn == 7:
            het = masodik
        elif turn == 8:
            nyolc = masodik
        else:
            kilenc = masodik
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")
        if ((1 in robot1) and (2 in robot1) and (3 in robot1)) or ((4 in robot1) and (5 in robot1) and (6 in robot1)) or ((7 in robot1) and (8 in robot1) and (9 in robot1)) or ((1 in robot1) and (5 in robot1) and (9 in robot1)) or ((3 in robot1) and (5 in robot1) and (7 in robot1)) or ((1 in robot1) and (4 in robot1) and (7 in robot1)) or ((2 in robot1) and (5 in robot1) and (8 in robot1)) or ((3 in robot1) and (6 in robot1) and (9 in robot1)):
            robot1_w = "win"
            robot2_w = "lose"
        elif ((1 in robot2) and (2 in robot2) and (3 in robot2)) or ((4 in robot2) and (5 in robot2) and (6 in robot2)) or ((7 in robot2) and (8 in robot2) and (9 in robot2)) or ((1 in robot2) and (5 in robot2) and (9 in robot2)) or ((3 in robot2) and (5 in robot2) and (7 in robot2)) or ((1 in robot2) and (4 in robot2) and (7 in robot2)) or ((2 in robot2) and (5 in robot2) and (8 in robot2)) or ((3 in robot2) and (6 in robot2) and (9 in robot2)):
            robot1_w = "lose"
            robot2_w = "win"
    
        time.sleep(1)
        #7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    while robot1_w == " " and robot2_w == " " and most == 7:
        most += 1
        while turn in rakott:
            turn = random.randint(1,9)
        rakott.append(turn)
        robot1.append(turn)
        if turn == 1:
            egy = kezdo
        elif turn == 2:
            ketto = kezdo
        elif turn == 3:
            harom = kezdo
        elif turn == 4:
            negy = kezdo
        elif turn == 5:
            ot = kezdo
        elif turn == 6:
            hat = kezdo
        elif turn == 7:
            het = kezdo
        elif turn == 8:
            nyolc = kezdo
        else:
            kilenc = kezdo
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")
        if ((1 in robot1) and (2 in robot1) and (3 in robot1)) or ((4 in robot1) and (5 in robot1) and (6 in robot1)) or ((7 in robot1) and (8 in robot1) and (9 in robot1)) or ((1 in robot1) and (5 in robot1) and (9 in robot1)) or ((3 in robot1) and (5 in robot1) and (7 in robot1)) or ((1 in robot1) and (4 in robot1) and (7 in robot1)) or ((2 in robot1) and (5 in robot1) and (8 in robot1)) or ((3 in robot1) and (6 in robot1) and (9 in robot1)):
            robot1_w = "win"
            robot2_w = "lose"
        elif ((1 in robot2) and (2 in robot2) and (3 in robot2)) or ((4 in robot2) and (5 in robot2) and (6 in robot2)) or ((7 in robot2) and (8 in robot2) and (9 in robot2)) or ((1 in robot2) and (5 in robot2) and (9 in robot2)) or ((3 in robot2) and (5 in robot2) and (7 in robot2)) or ((1 in robot2) and (4 in robot2) and (7 in robot2)) or ((2 in robot2) and (5 in robot2) and (8 in robot2)) or ((3 in robot2) and (6 in robot2) and (9 in robot2)):
            robot1_w = "lose"
            robot2_w = "win"
    
        time.sleep(1)
        #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    while robot1_w == " " and robot2_w == " " and most == 8:
        most += 1
        while turn in rakott:
            turn = random.randint(1,9)
        rakott.append(turn)
        robot2.append(turn)
        if turn == 1:
            egy = masodik
        elif turn == 2:
            ketto = masodik
        elif turn == 3:
            harom = masodik
        elif turn == 4:
            negy = masodik
        elif turn == 5:
            ot = masodik
        elif turn == 6:
            hat = masodik
        elif turn == 7:
            het = masodik
        elif turn == 8:
            nyolc = masodik
        else:
            kilenc = masodik
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")
        if ((1 in robot1) and (2 in robot1) and (3 in robot1)) or ((4 in robot1) and (5 in robot1) and (6 in robot1)) or ((7 in robot1) and (8 in robot1) and (9 in robot1)) or ((1 in robot1) and (5 in robot1) and (9 in robot1)) or ((3 in robot1) and (5 in robot1) and (7 in robot1)) or ((1 in robot1) and (4 in robot1) and (7 in robot1)) or ((2 in robot1) and (5 in robot1) and (8 in robot1)) or ((3 in robot1) and (6 in robot1) and (9 in robot1)):
            robot1_w = "win"
            robot2_w = "lose"
        elif ((1 in robot2) and (2 in robot2) and (3 in robot2)) or ((4 in robot2) and (5 in robot2) and (6 in robot2)) or ((7 in robot2) and (8 in robot2) and (9 in robot2)) or ((1 in robot2) and (5 in robot2) and (9 in robot2)) or ((3 in robot2) and (5 in robot2) and (7 in robot2)) or ((1 in robot2) and (4 in robot2) and (7 in robot2)) or ((2 in robot2) and (5 in robot2) and (8 in robot2)) or ((3 in robot2) and (6 in robot2) and (9 in robot2)):
            robot1_w = "lose"
            robot2_w = "win"
    
        time.sleep(1)
        #999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    while robot1_w == " " and robot2_w == " " and most == 9 and most_volt == 1:
        most += 1
        while turn in rakott:
            turn = random.randint(1,9)
        rakott.append(turn)
        robot1.append(turn)
        if turn == 1:
            egy = kezdo
        elif turn == 2:
            ketto = kezdo
        elif turn == 3:
            harom = kezdo
        elif turn == 4:
            negy = kezdo
        elif turn == 5:
            ot = kezdo
        elif turn == 6:
            hat = kezdo
        elif turn == 7:
            het = kezdo
        elif turn == 8:
            nyolc = kezdo
        else:
            kilenc = kezdo
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")
        if ((1 in robot1) and (2 in robot1) and (3 in robot1)) or ((4 in robot1) and (5 in robot1) and (6 in robot1)) or ((7 in robot1) and (8 in robot1) and (9 in robot1)) or ((1 in robot1) and (5 in robot1) and (9 in robot1)) or ((3 in robot1) and (5 in robot1) and (7 in robot1)) or ((1 in robot1) and (4 in robot1) and (7 in robot1)) or ((2 in robot1) and (5 in robot1) and (8 in robot1)) or ((3 in robot1) and (6 in robot1) and (9 in robot1)):
            robot1_w = "win"
            robot2_w = "lose"
        elif ((1 in robot2) and (2 in robot2) and (3 in robot2)) or ((4 in robot2) and (5 in robot2) and (6 in robot2)) or ((7 in robot2) and (8 in robot2) and (9 in robot2)) or ((1 in robot2) and (5 in robot2) and (9 in robot2)) or ((3 in robot2) and (5 in robot2) and (7 in robot2)) or ((1 in robot2) and (4 in robot2) and (7 in robot2)) or ((2 in robot2) and (5 in robot2) and (8 in robot2)) or ((3 in robot2) and (6 in robot2) and (9 in robot2)):
            robot1_w = "lose"
            robot2_w = "win"
    
        time.sleep(1)

    if (((win == "X") or (win == "x")) and robot1_w == "win") or (((win == "O") or (win == "o")) and robot2_w == "win"):
        os.system('cls')
        egyenleg += (bet*2)
        print(f"Egyenleg: {egyenleg}\n")
        print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")
        print("Nyertél!")
        time.sleep(1)
    elif (((win == "X") or (win == "x")) and robot2_w == "win") or (((win == "O") or (win == "o")) and robot1_w == "win"):
        os.system('cls')
        egyenleg += (bet*0)
        print(f"Egyenleg: {egyenleg}\n")
        print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")
        print("Vesztettél!")
        time.sleep(1)
    else:
        os.system('cls')
        egyenleg += (bet*1)
        print(f"Egyenleg: {egyenleg}\n")
        print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")
        print("Döntetlen!")
        time.sleep(1)
        
    ujra = input("\nSzeretnél még játszani?(y/n)\n")