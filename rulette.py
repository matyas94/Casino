import random
import os
import time
jatek = input("Mit szeretnél játszan? (roulette)\n")
ujra = "y"
while jatek == "roulette" and ujra == "y":

    egyenleg = 20



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
