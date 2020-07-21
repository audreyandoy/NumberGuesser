import random

print("Welcome to Number Guesser")

#PROJECT PLAN W CLASS
# - Computer Number
# - Player number
# - Tries
# - TriesOver
# - Check player won
# - TypeError Handling

#global variables
comp_num = random.randint(0, 10)
tries = 3
won = False
play = True

while play == True:
  while tries > 0:
    print()
    player_num = input("Enter a number between 0-10: ")
    player_num = float(player_num)
    if player_num < 0 or player_num > 10:
      print("Bad Number")
      break
    else:
      if player_num > comp_num:
        print("Number too big")
        tries -= 1
        print("You have "+ str(tries) + " tries left")
      elif player_num < comp_num:
        print("Number too small")
        tries -= 1
        print("You have "+ str(tries) + " tries left")
      else:
        print("Correct")
        won = True
        break