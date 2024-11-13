import os
import random
import time
egyenleg = 100
jatek = input("Mit szeretnél játszan? (plinko)\n")
ujra = "y"
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