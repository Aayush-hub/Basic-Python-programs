import random

print("\n\n"+"Welcome to Rock, Paper, Scissor GAME".center(46, "-"))
win, lose, tie = 0, 0, 0

while True:   
    ai = random.randint(1, 3)   # Taking random input
    
    # Show results
    print("\nWIN = {0}  LOSE = {1}  TIE = {2}".format(win, lose, tie))
    print("\nEnter (r)ock, (p)aper, (s)cissor or (q)uit\n")
    
    inp = input()   # User input
    if (inp == "r"):
        print("Rock verses...")
    elif (inp == "p"):
        print("Paper verses...")
    elif (inp == "s"):
        print("Scissor verses...")
    elif (inp == "q"):
        break
    else:
        print("ENTER VALID INPUT")
        continue
    
    # Displaying pc's move
    if ai == 1:
        print("Rock")
        ai = "r"
    elif ai == 2:
        print("Paper")
        ai = "p"
    elif ai == 3:
        print("Scissor")
        ai = "s"
        
    # Checking conditions
    if inp == ai:
        print("\nIt's a TIE.")
        tie += 1
    elif inp == "r" and ai == 's':
        print("\nYou WIN.")
        win += 1
    elif inp == 'p' and ai == 'r':
        print("\nYou WIN.")
        win += 1
    elif inp == 's' and ai == 'p':
        print("\nYou WIN.")
        win += 1
    elif inp == 'r' and ai == 'p':
        print("\nYou LOSE.")
        lose += 1
    elif inp == 's' and ai == 'r':
        print("\nYou LOSE.")
        lose += 1
    elif inp == 'p' and ai == 's':
        print("\nYou LOSE.")
        lose += 1
