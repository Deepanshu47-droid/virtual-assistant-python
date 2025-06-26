import os
import random
import time

lst=[' ',' ',' ',' ',' ',' ',' ',' ',' ','g']


def intro(): 
    os.system("cls")
    print("=================")
    print("   TIC TAC TOE   ") 
    print("=================\n")
def board(): 

    print(f" {lst[0]} | {lst[1]} | {lst[2]} ")
    print("-----------")
   
    print(f" {lst[3]} | {lst[4]} | {lst[5]} ")
    print("-----------")
    print(f" {lst[6]} | {lst[7]} | {lst[8]} ")

def check(): 
    flag=0
    if(lst[0]==lst[1]==lst[2]!=' ' or lst[3]==lst[4]==lst[5]!=' ' or lst[6]==lst[7]==lst[8]!=' ' or 
       lst[0]==lst[4]==lst[8]!=' ' or lst[2]==lst[4]==lst[6]!=' ' or lst[0]==lst[3]==lst[6]!=' ' or 
       lst[1]==lst[4]==lst[7]!=' ' or lst[2]==lst[5]==lst[8]!=' '): 
        flag=1
    elif lst[0]!=' ' and lst[1]!=' ' and lst[2]!=' ' and lst[3]!=' ' and lst[4]!=' ' and lst[5]!=' ' and lst[6]!=' ' and lst[7]!=' ' and lst[8]!=' ':
        flag=2
    return flag

def mode(): 
    a=input("Press 1 for 1 player mode & 2 for 2 player mode! ")
    if a=="1": 
        play1(0)
    elif a=="2": 
        play2(0)
    else: 
        print("sorry mode not available!\nPress any key")
        input()
        mode()

def play1(i):
    intro()
    board()
    t=10
    if i==0:
        t=int(input(f"player's turn!\nPlease Choose an index "))
        if t<1 or t>9 or lst[t-1]!=' ':
            os.system("cls")
            print("Wrong index!")
            input("Press any key")
            play1(i)
        lst[t-1]='X'
    else:
        time.sleep(1)
        print("computer's turn!")
        while(lst[t-1]!=' '):
            t=random.randint(1,9)
        lst[t-1]='O'
    if(check()==0):
        play1((i+1)%2)
    elif(check()==2):
       
        intro()
        board()
        print("Match Draw!")
        input()
    else: 
       lst.append(i+1)

def play2(i):
    intro()
    board()
    t=int(input(f"player {i+1}'s turn!\nPlease Choose an index "))
    if   t<1 or t>9 or lst[t-1]!=' ':
        os.system("cls")
        print("Wrong index!")
        input("Press any key")
        play2(i) 
    else: 
        if i==0:
            lst[t-1]='X'
        else:
            lst[t-1]='O'
    if(check()==0):
        play2((i+1)%2)
    elif(check()==2):
        intro()
        board()
        print("Match Draw!")
    else: 
       lst.append(i+1)

if __name__=='__main__': 
    intro()
    a=mode()
    if(check()==1):
        intro()
        board()
        print(f"player {lst[10]} won!")
        input()
    print("Thankyou! Hope you enjoyed the game.")
    
    

    

