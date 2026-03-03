from turtle import *
import random
import time
import os
# set up
bgcolor("lightgreen")
setup(650, 550)
pensize(2.5)
speed(0)
# map
bgpic(r"TreasureMap.gif")
# random position for treasure
target_x = random.randint(-220, 220)
target_y = random.randint(-170, 170)
target_range = 30   # How close they need to be
def treasureMark():
    # stamp
    penup()
    shape("turtle")
    goto(-175,235)
    right(60)
    color("red")
    stamp()
def treasure_text():
    # write top
    penup()
    goto(0, 230)
    write("Tracy's Treasure Hunt!",align="center",font=("Arial", 26, "bold"))
    # write bottom
    penup()
    color("black")
    goto(0, -250)
    write("Can you find her gold doubloon??",align="center",font=("Arial", 12, "italic"))
def hit_target(x, y):
    return abs(x - target_x) < target_range and abs(y - target_y) < target_range

# Intro
print("welcome to Treasure Hunt\nGood Luck...\n")
treasureMark()
treasure_text()
repeat = True
giveup = 0
while repeat == True:
    print(target_x, target_y)
    # Ask user
    x = int(textinput("What are the coordinates for the treasure on the x-axis?", "Most likely between -220 and 220: "))
    y = int(textinput("What are the coordinates for the treasure on the y-axis?", "Most likely between -170 and 170: "))
    print("\nYou dug here",x ,",", y)
    # Move Turtle to Guess

    # check for the treasure
    if hit_target(x, y):
        hideturtle
        print("You found the doubloon!")
        color("black")
        # Move Turtle to Guess
        penup()
        goto(x, y)
        pendown()
        begin_fill()
        circle(15)  
        color("gold")
        end_fill()
        penup()
        forward(15)
        color("black")
        write(":D", font=("Monospace", 12, "italic"))
        repeat = False
        if repeat == False:
            break

    else:
        hideturtle()
        print("Miss! Try again :(")
        color("red")
        # Move Turtle to Guess
        penup()
        goto(x, y)
        pendown()
        circle(15) 
        penup()
        forward(15)
        color("black")
        write(":(", font=("Monospace", 12, "italic"))    
        time.sleep(2)# Allows you to see your coodinates
        giveup += 1
        if giveup == 5:
            backout = textinput("Giving up?", "Do you want to give up? (yes or no): ")
            if backout == "yes":
                print("The treasure was at", target_x, ",", target_y)
                break
        else:
            continue

hideturtle()
# keep the window open
done()