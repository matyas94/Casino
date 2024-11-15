import random
import time
import os
os.system('cls')
egyenleg = 100
opcio = "jatek"
while opcio == "jatek":
    jatek = input("Mit szeretnél játszan? (number guesser, plinko, roulette, xo, coinflip)\n")
    ujra = "y"
    while jatek == "number guesser" and ujra == "y":
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print("Gondolj egy számra egytől tízig.")
        time.sleep(2)
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        bet = int(input("Mennyit szeretnél rakni? "))

        while bet > egyenleg:
            print("Nem tudsz ennyit rakni.")
            bet = int(input("Mennyit szeretnél rakni? "))
        egyenleg -= bet
        wins = 0
        time.sleep(0.2)
        os.system('cls')
        for i in range(1,11):
            print(f"Egyenleg: {egyenleg}\n")
            gondolat = input(f"A szám amire gondoltál a(z) {i}?(y/n) ")
            if gondolat == "y":
                win = i
                wins += 1
            time.sleep(0.3)
            os.system('cls')

        if wins > 1:
            print(f"Egyenleg: {egyenleg}\n")
            print("Több számra nem gondolhatsz, vesztettél.")
        elif wins == 0:
            print(f"Egyenleg: {egyenleg}\n")
            print("Hazudsz, nem tudsz nem gondolni számra, vesztettél.")
        else:
            print(f"Egyenleg: {egyenleg}\n")
            print(f"A te számod: {win}, kitaláltam, vesztettél.")
        ujra = input("\nSzeretnél még játszani?(y/n)\n")   

    while jatek == "plinko" and ujra == "y":
        e_1 = "."

        k_1 = "."
        k_2 = "."

        h_1 = "."
        h_2 = "."
        h_3 = "."

        n_1 = "."
        n_2 = "."
        n_3 = "."
        n_4 = "."

        o_1 = "."
        o_2 = "."
        o_3 = "."
        o_4 = "."
        o_5 = "."

        ha_1 = "."
        ha_2 = "."
        ha_3 = "."
        ha_4 = "."
        ha_5 = "."
        ha_6 = "."

        he_1 = "."
        he_2 = "."
        he_3 = "."
        he_4 = "."
        he_5 = "."
        he_6 = "."
        he_7 = "."
        os.system('cls')


        print(f"Egyenleg: {egyenleg}\n")

        print(f"      {e_1}\n     {k_1} {k_2}\n    {h_1} {h_2} {h_3}\n   {n_1} {n_2} {n_3} {n_4}\n  {o_1} {o_2} {o_3} {o_4} {o_5}\n {ha_1} {ha_2} {ha_3} {ha_4} {ha_5} {ha_6}\n{he_1} {he_2} {he_3} {he_4} {he_5} {he_6} {he_7}\n3 2 1 0 1 2 3")

        bet = int(input("\nMennyit szeretnél rakni? "))

        while bet > egyenleg:
            print("Nem tudsz ennyit rakni.")
            bet = int(input("Mennyit szeretnél rakni? "))

        egyenleg -= bet

        os.system('cls')
        e_1 = "O"
        print(f"Egyenleg: {egyenleg}\n")
        print(f"      {e_1}\n     {k_1} {k_2}\n    {h_1} {h_2} {h_3}\n   {n_1} {n_2} {n_3} {n_4}\n  {o_1} {o_2} {o_3} {o_4} {o_5}\n {ha_1} {ha_2} {ha_3} {ha_4} {ha_5} {ha_6}\n{he_1} {he_2} {he_3} {he_4} {he_5} {he_6} {he_7}\n3 2 1 0 1 2 3")
        time.sleep(1)

        if random.randint(1,2) == 1:
            k_1 = "O"
        else:
            k_2 = "O"

        os.system('cls')
        e_1 = "."
        print(f"Egyenleg: {egyenleg}\n")
        print(f"      {e_1}\n     {k_1} {k_2}\n    {h_1} {h_2} {h_3}\n   {n_1} {n_2} {n_3} {n_4}\n  {o_1} {o_2} {o_3} {o_4} {o_5}\n {ha_1} {ha_2} {ha_3} {ha_4} {ha_5} {ha_6}\n{he_1} {he_2} {he_3} {he_4} {he_5} {he_6} {he_7}\n3 2 1 0 1 2 3")
        time.sleep(1)

        if k_1 == "O":
            if random.randint(1,2) == 1:
                h_1 = "O"
            else:
                h_2 = "O"
        else:
            if random.randint(1,2) == 1:
                h_2 = "O"
            else:
                h_3 = "O"

        os.system('cls')
        k_1 = "."
        k_2 = "."
        print(f"Egyenleg: {egyenleg}\n")
        print(f"      {e_1}\n     {k_1} {k_2}\n    {h_1} {h_2} {h_3}\n   {n_1} {n_2} {n_3} {n_4}\n  {o_1} {o_2} {o_3} {o_4} {o_5}\n {ha_1} {ha_2} {ha_3} {ha_4} {ha_5} {ha_6}\n{he_1} {he_2} {he_3} {he_4} {he_5} {he_6} {he_7}\n3 2 1 0 1 2 3")
        time.sleep(1)

        if h_1 == "O":
            if random.randint(1,2) == 1:
                n_1 = "O"
            else:
                n_2 = "O"
        elif h_2 == "O":
            if random.randint(1,2) == 1:
                n_2 = "O"
            else:
                n_3 = "O"
        else:
            if random.randint(1,2) == 1:
                n_3 = "O"
            else:
                n_4 = "O"

        os.system('cls')
        h_1 = "."
        h_2 = "."
        h_3 = "."
        print(f"Egyenleg: {egyenleg}\n")
        print(f"      {e_1}\n     {k_1} {k_2}\n    {h_1} {h_2} {h_3}\n   {n_1} {n_2} {n_3} {n_4}\n  {o_1} {o_2} {o_3} {o_4} {o_5}\n {ha_1} {ha_2} {ha_3} {ha_4} {ha_5} {ha_6}\n{he_1} {he_2} {he_3} {he_4} {he_5} {he_6} {he_7}\n3 2 1 0 1 2 3")
        time.sleep(1)

        if n_1 == "O":
            if random.randint(1,2) == 1:
                o_1 = "O"
            else:
                o_2 = "O"
        elif n_2 == "O":
            if random.randint(1,2) == 1:
                o_2 = "O"
            else:
                o_3 = "O"
        elif n_3 == "O":
            if random.randint(1,2) == 1:
                o_3 = "O"
            else:
                o_4 = "O"
        else:
            if random.randint(1,2) == 1:
                o_4 = "O"
            else:
                o_5 = "O"

        os.system('cls')
        n_1 = "."
        n_2 = "."
        n_3 = "."
        n_4 = "."
        print(f"Egyenleg: {egyenleg}\n")
        print(f"      {e_1}\n     {k_1} {k_2}\n    {h_1} {h_2} {h_3}\n   {n_1} {n_2} {n_3} {n_4}\n  {o_1} {o_2} {o_3} {o_4} {o_5}\n {ha_1} {ha_2} {ha_3} {ha_4} {ha_5} {ha_6}\n{he_1} {he_2} {he_3} {he_4} {he_5} {he_6} {he_7}\n3 2 1 0 1 2 3")
        time.sleep(1)

        if o_1 == "O":
            if random.randint(1,2) == 1:
                ha_1 = "O"
            else:
                ha_2 = "O"
        elif o_2 == "O":
            if random.randint(1,2) == 1:
                ha_2 = "O"
            else:
                ha_3 = "O"
        elif o_3 == "O":
            if random.randint(1,2) == 1:
                ha_3 = "O"
            else:
                ha_4 = "O"
        elif o_4 == "O":
            if random.randint(1,2) == 1:
                ha_4 = "O"
            else:
                ha_5 = "O"
        else:
            if random.randint(1,2) == 1:
                ha_5 = "O"
            else:
                ha_6 = "O"

        os.system('cls')
        o_1 = "."
        o_2 = "."
        o_3 = "."
        o_4 = "."
        o_5 = "."
        print(f"Egyenleg: {egyenleg}\n")
        print(f"      {e_1}\n     {k_1} {k_2}\n    {h_1} {h_2} {h_3}\n   {n_1} {n_2} {n_3} {n_4}\n  {o_1} {o_2} {o_3} {o_4} {o_5}\n {ha_1} {ha_2} {ha_3} {ha_4} {ha_5} {ha_6}\n{he_1} {he_2} {he_3} {he_4} {he_5} {he_6} {he_7}\n3 2 1 0 1 2 3")
        time.sleep(1)

        if ha_1 == "O":
            if random.randint(1,2) == 1:
                he_1 = "O"
            else:
                he_2 = "O"
        elif ha_2 == "O":
            if random.randint(1,2) == 1:
                he_2 = "O"
            else:
                he_3 = "O"
        elif ha_3 == "O":
            if random.randint(1,2) == 1:
                he_3 = "O"
            else:
                he_4 = "O"
        elif ha_4 == "O":
            if random.randint(1,2) == 1:
                he_4 = "O"
            else:
                he_5 = "O"
        elif ha_4 == "O":
            if random.randint(1,2) == 1:
                he_5 = "O"
            else:
                he_6 = "O"
        else:
            if random.randint(1,2) == 1:
                he_6 = "O"
            else:
                he_7 = "O"

        time.sleep(0.5)

        if he_1 == "O" or he_7 == "O":
            egyenleg += (bet*3)
        elif he_2 == "O" or he_6 == "O":
            egyenleg += (bet*2)
        elif he_3 == "O" or he_5 == "O":
            egyenleg += (bet*1)
        else:
            egyenleg += (bet*0) 

        os.system('cls')
        ha_1 = "."
        ha_2 = "."
        ha_3 = "."
        ha_4 = "."
        ha_5 = "."
        ha_6 = "."
        print(f"Egyenleg: {egyenleg}\n")
        print(f"      {e_1}\n     {k_1} {k_2}\n    {h_1} {h_2} {h_3}\n   {n_1} {n_2} {n_3} {n_4}\n  {o_1} {o_2} {o_3} {o_4} {o_5}\n {ha_1} {ha_2} {ha_3} {ha_4} {ha_5} {ha_6}\n{he_1} {he_2} {he_3} {he_4} {he_5} {he_6} {he_7}\n3 2 1 0 1 2 3")
        time.sleep(1)

        ujra = input("\nSzeretnél még játszani?(y/n)\n")

    while jatek == "roulette" and ujra == "y":




        if 1 == 1:
            r0 = "0"
            r1 = "1"
            r2 = "2"
            r3 = "3"
            r4 = "4"
            r5 = "5"
            r6 = "6"
            r7 = "7"
            r8 = "8"
            r9 = "9"
            r10 = "10"
            r11 = "11"
            r12 = "12"
            r13 = "13"
            r14 = "14"
            r15 = "15"
            r16 = "16"
            r17 = "17"
            r18 = "18"
            r19 = "19"
            r20 = "20"
            r21 = "21"
            r22 = "22"
            r23 = "23"
            r24 = "24"
            r25 = "25"
            r26 = "26"
            r27 = "27"
            r28 = "28"
            r29 = "29"
            r30 = "30"
            r31 = "31"
            r32 = "32"
            r33 = "33"
            r34 = "34"
            r35 = "35"
            r36 = "36"
            r37 = "[1-18]"
            r38 = "[19-36]"
            r39 = "[EVEN]"
            r40 = "[ODD]"
            r41 = "[RED]"
            r42 = "[BLACK]"
            r43 = "[1ST 12]"
            r44 = "[2ND 12]"
            r45 = "[3RD 12]"
            r46 = "[1ST COL]"
            r47 = "[2ND COL]"
            r48 = "[3RD COL]"



            rr0 = [0]
            rr1 = [1]
            rr2 = [2]
            rr3 = [3]
            rr4 = [4]
            rr5 = [5]
            rr6 = [6]
            rr7 = [7]
            rr8 = [8]
            rr9 = [9]
            rr10 = [10]
            rr11 = [11]
            rr12 = [12]
            rr13 = [13]
            rr14 = [14]
            rr15 = [15]
            rr16 = [16]
            rr17 = [17]
            rr18 = [18]
            rr19 = [19]
            rr20 = [20]
            rr21 = [21]
            rr22 = [22]
            rr23 = [23]
            rr24 = [24]
            rr25 = [25]
            rr26 = [26]
            rr27 = [27]
            rr28 = [28]
            rr29 = [29]
            rr30 = [30]
            rr31 = [31]
            rr32 = [32]
            rr33 = [33]
            rr34 = [34]
            rr35 = [35]
            rr36 = [36]
            rr37 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
            rr38 = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
            rr39 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
            rr40 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
            rr41 = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
            rr42 = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
            rr43 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            rr44 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
            rr45 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
            rr46 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
            rr47 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
            rr48 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
        print(f"Egyenleg: {egyenleg}")
        print(f"""
|--------------|
|       {r0}      |
|--------------|
|  {r1} |  {r2} |  {r3} |
|--------------|
|  {r4} |  {r5} |  {r6} |
|--------------|
|  {r7} |  {r8} |  {r9} |
|--------------|
| {r10} | {r11} | {r12} |
|--------------|
| {r13} | {r14} | {r15} |
|--------------|
| {r16} | {r17} | {r18} |
|--------------|
| {r19} | {r20} | {r21} |
|--------------|
| {r22} | {r23} | {r24} |
|--------------|
| {r25} | {r26} | {r27} |
|--------------|
| {r28} | {r29} | {r30} |
|--------------|
| {r31} | {r32} | {r33} |
|--------------|
| {r34} | {r35} | {r36} |
|--------------|

{r37}
{r38}
{r39}
{r40}
{r41}
{r42}
{r43}
{r44}
{r45}
{r46}
{r47}
{r48}
Ha kell segítség akkor :'help', ha nem nyomj entert.""")

        help = input("")
        if help == "help":
            print("""
        [1-18]: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
        [19-36]: 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36
        [EVEN]: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35
        [ODD]: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36
        [RED]: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
        [BLACK]: 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35
        [1ST 12]: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
        [2ND 12]: 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24
        [3RD 12]: 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36
        [1ST COL]: 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34
        [2ND COL]: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35
        [3RD COL]: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36""")
        time.sleep(0.3)

        bet = int(input("Mennyit szeretnél rakni? "))

        while bet > egyenleg:
            print("Nem tudsz ennyit rakni.")
            bet = int(input("Mennyit szeretnél rakni? "))
        time.sleep(0.2)
        egyenleg -= bet
        szam = input("\nHova szeretnél tenni? ")

        os.system('cls')

        for i in range(1,4):


            
            print(f"Egyenleg: {egyenleg}")
            print(f"""
        |--------------|
        |       {r0}      |
        |--------------|
        |  {r1} |  {r2} |  {r3} |
        |--------------|
        |  {r4} |  {r5} |  {r6} |
        |--------------|
        |  {r7} |  {r8} |  {r9} |
        |--------------|
        | {r10} | {r11} | {r12} |
        |--------------|
        | {r13} | {r14} | {r15} |
        |--------------|
        | {r16} | {r17} | {r18} |
        |--------------|
        | {r19} | {r20} | {r21} |
        |--------------|
        | {r22} | {r23} | {r24} |
        |--------------|
        | {r25} | {r26} | {r27} |
        |--------------|
        | {r28} | {r29} | {r30} |
        |--------------|
        | {r31} | {r32} | {r33} |
        |--------------|
        | {r34} | {r35} | {r36} |
        |--------------|

        {r37}
        {r38}
        {r39}
        {r40}
        {r41}
        {r42}
        {r43}
        {r44}
        {r45}
        {r46}
        {r47}
        {r48}
        """)
            print(f"Sorsolas{"."*i}")
            time.sleep(1)
            os.system('cls')
        nyero = random.randint(0,36)

        if nyero == szam:
            egyenleg += (bet*36)
        elif (szam == "[1-18]" or szam == "[19-36]" or szam == "[EVEN]" or szam == "[ODD]" or szam == "[RED]" or szam == "[BLACK]") and (nyero in rr37 or nyero in rr38 or nyero in rr39 or nyero in rr40 or nyero in rr41 or nyero in rr42):
            egyenleg += (bet*2)
        elif (szam == "[1ST 12]" or szam == "[2ND 12]" or szam == "[3RD 12]" or szam == "[1ST COL]" or szam == "[2ND COL]" or szam == "[3RD COL]") and (nyero in rr43 or nyero in rr44 or nyero in rr45 or nyero in rr46 or nyero in rr47 or nyero in rr48):
            egyenleg += (bet*3)

        print(f"Egyenleg: {egyenleg}")
        print(f"""|--------------|
        |       {r0}      |
        |--------------|
        |  {r1} |  {r2} |  {r3} |
        |--------------|
        |  {r4} |  {r5} |  {r6} |
        |--------------|
        |  {r7} |  {r8} |  {r9} |
        |--------------|
        | {r10} | {r11} | {r12} |
        |--------------|
        | {r13} | {r14} | {r15} |
        |--------------|
        | {r16} | {r17} | {r18} |
        |--------------|
        | {r19} | {r20} | {r21} |
        |--------------|
        | {r22} | {r23} | {r24} |
        |--------------|
        | {r25} | {r26} | {r27} |
        |--------------|
        | {r28} | {r29} | {r30} |
        |--------------|
        | {r31} | {r32} | {r33} |
        |--------------|
        | {r34} | {r35} | {r36} |
        |--------------|

        {r37}
        {r38}
        {r39}
        {r40}
        {r41}
        {r42}
        {r43}
        {r44}
        {r45}
        {r46}
        {r47}
        {r48}
        """)
        print(f"A sorsolás erdménye: {nyero}")
        time.sleep(1)
        ujra = input("\nSzeretnél még játszani?(y/n)\n")

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

    while jatek == "slot" and ujra == "y":
        os.system('cls')
        slot = 0

        segy = random.randint(1,9)
        sketto = random.randint(1,9)
        sharom = random.randint(1,9)

        ssegy = random.randint(1,9)
        ssketto = random.randint(1,9)
        ssharom = random.randint(1,9)

        slista = [segy, sketto, sharom,]
        sslista = [ssegy, ssketto, ssharom,]
        print(f"Egyenleg: {egyenleg}\n")
        bet = int(input("\nMennyit szeretnél rakni? "))

        while bet > egyenleg:
            print("Nem tudsz ennyit rakni.")
            bet = int(input("Mennyit szeretnél rakni? "))
        
        egyenleg -= bet

        for i in range(0,2):
            if slista[i] != sslista[i]:
                slot += 1

        while slot <= 9:
            os.system('cls')
            print(f"Egyenleg: {egyenleg}\n")
            print(f"{"-"*13}\n| {sslista[0]} | {sslista[1]} | {sslista[2]} |\n{"-"*13}")

            for i in range(0,2):
                if slista[i] == sslista[i]:
                    slot += 1
                else:
                    sslista[i] += 1

            if sslista[0] > 9:
                sslista[0] -= 9
            if sslista[1] > 9:
                sslista[1] -= 9
            if sslista[2] > 9:
                sslista[2] -= 9

            time.sleep(1)

        sssegy = sslista[0]
        sssketto = sslista[1]
        sssharom = sslista[2]
        os.system('cls')
        if sssegy == sssketto and sssketto == sssharom:
            egyenleg += (bet*10)
            print(f"Egyenleg: {egyenleg}\n")
            print("Big win")
        elif sssegy == sssketto or sssketto == sssharom or sssegy == sssharom:
            egyenleg += (bet*2)
            print(f"Egyenleg: {egyenleg}\n")
            print("smol win")
        else:
            print(f"Egyenleg: {egyenleg}\n")
            print("lose")
        time.sleep(1)

        ujra = input("\nSzeretnél még játszani?(y/n)\n")

    while jatek == "coinflip" and ujra == "y":
        os.system('cls')
        coin = input("Mire szeretnél rakni?(f,i) ")
        print(f"Egyenleg: {egyenleg}\n")
        bet = int(input("\nMennyit szeretnél rakni? "))

        while bet > egyenleg:
            print("Nem tudsz ennyit rakni.")
            bet = int(input("Mennyit szeretnél rakni? "))
        
        egyenleg -= bet

        ctime = 0.01

        while time != 2:
            os.system('cls')
            print(f"Egyenleg: {egyenleg}\n")
            print("f")
            time.sleep(ctime)
            ctime += ctime
            os.system('cls')
            print(f"Egyenleg: {egyenleg}\n")
            print("i")
            time.sleep(ctime)
            ctime += ctime
        flip = random.randint(1,2)
        if flip == 1:
            os.system('cls')
            print(f"Egyenleg: {egyenleg}\n")
            print("f")
            winner = "f"
        else:
            os.system('cls')
            print(f"Egyenleg: {egyenleg}\n")
            print("i")
            winner = "i"

        if coin == "f" and winner == "f" or coin == "i" and winner == "i":
            os.system('cls')
            egyenleg += (bet*2)
            print(f"Egyenleg: {egyenleg}\n")
            print("Nyertél!")
        else:
            os.system('cls')
            print(f"Egyenleg: {egyenleg}\n")
            print("Vesztettél!")
        time.sleep(1)

        ujra = input("\nSzeretnél még játszani?(y/n)\n")

