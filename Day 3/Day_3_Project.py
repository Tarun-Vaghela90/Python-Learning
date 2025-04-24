print ("Welcome to Treasure Island.Your mission is to find the treasure")

direction = input("Where Do You Want  to Go Left  Or Right Type type left or right \n").lower()

if(direction == "right"):
    print("You Fall  into Hall  . GAME OVER")
elif direction  == "left":
    print("You Came Near  lake")
    swim = input("Are You ghonna Swim or wait ? Type swim or wait \n").lower()
    if  swim   == "swim":
        print("Attacked by trout.   Game Over")
    elif swim  == "wait":
        door = input("while you waiting you see Three doors Red , Blue And Yellow  which door through you like to go Type Door  Name ? \n").lower()
        if  door  == "red":
            print("Burned by fire. Game Over.")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        elif door == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.   Game Over")
else:
    print("You Fall  into Hall  . GAME OVER")

    
