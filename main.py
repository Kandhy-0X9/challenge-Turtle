from turtle import *
import random
#set up
setup(480,480)
speed(0)
# Target Area
# Random target area
posX = window_width() // 2
posY = window_height() // 2
target_x = random.randint(-posX, posX)
target_y = random.randint(-posY, posY)
target_range = 30   # How close they need to be

print(target_x, target_y)# for me to check the treasure

# Function to Check Hit (returns a boolean)
def hit_target(x, y):
    return abs(x - target_x) < target_range and abs(y - target_y) < target_range

# Intro
print("welcome to Treasure Hunt\nGood Luck...\n")
repeat = True

while repeat == True:
    # Ask user
    x = int(input("What are the coordinates for the treasure on the x-axis\nBetween -240 and 240: "))
    y = int(input("What are the coordinates for the treasure on the y-axis\nBetween -240 and 240: "))
    # check for the treasure
    if hit_target(x, y):
        print("\nYou found the treasure\n")
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