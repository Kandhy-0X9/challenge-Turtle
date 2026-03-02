from turtle import *
import random
# set up
bgcolor("lightgreen")
setup(650, 550)
pensize(2.5)
speed(0)
hideturtle()
# map
bgpic(r"TreasureMap.gif")
# write top
penup()
color("brown")
goto(0, 230)
write("Tracy's Treasure Hunt!",align="center",font=("Arial", 26, "bold"))
# write bottom
penup()
color("black")
goto(0, -250)
write("Can you find her gold doubloon??",align="center",font=("Arial", 12, "italic"))
# Random target area
target_x = random.randint(-220, 220)
target_y = random.randint(-170, 170)
target_range = 30   # How close they need to be
# Function to Check Hit (returns a boolean)
def hit_target(x, y):
    return abs(x - target_x) < target_range and abs(y - target_y) < target_range
# Intro
print("welcome to Treasure Hunt\nGood Luck...\n")
repeat = True
while repeat == True:
    # Ask user
    x = int(input("What are the coordinates for the treasure on the x-axis?\nMost likely between -220 and 220: "))
    y = int(input("What are the coordinates for the treasure on the y-axis?\nMOst likely between -170 and 170: "))
    print("\nYou dug here",x ,",", y)
    # check for the treasure
    if hit_target(x, y):
        print("You found the treasure\nTreasure was at:", target_x,",",target_y)
        penup()
        goto(x, y)
        begin_fill()
        pendown()
        circle(12)
        color("yellow")
        end_fill()
        repeat = False
        if repeat == False:
            break
    else:
        print("\nYou didn't find the treasure\n")
        color("red")
        penup()
        goto(x, y)
        pendown()
        circle(12)       
# keep the window open
done()