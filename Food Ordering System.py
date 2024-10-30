import turtle
from Modules import main_menu

########################
###  WELCOME WINDOW  ###
########################

wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Food Ordering System - Welcome Page")
tess = turtle.Turtle()
tess.hideturtle()
tess.penup()
tess.color('black')
tess.goto(-75, 200)
tess.pendown()
tess.speed(10)
for i in [0, 1, 2, 3, 4]:
    tess.forward(100)
    tess.right(144)

tess.penup()
tess.goto(-180, 90)
tess.pendown()
style1 = ('Courier', 30, 'bold')
tess.write('W E L C O M E', font=style1)

tess.penup()
tess.goto(-300, 10)
tess.pendown()

style2 = ('Courier', 20, 'italic')
tess.write("\nYou are using Food Ordering System", font=style2)

tess.penup()
tess.goto(100, -50)
tess.pendown()

tess.speed(7)

tess.color('brown')
style3 = ('Courier', 10, 'italic')
tess.write("Click to continue...", font=style3)

tess.speed(10)
tess.penup()
tess.backward(20)
tess.pendown()
tess.forward(200)
tess.hideturtle()

wn.exitonclick()


#######################
###  MAIN FUNCTION  ###
#######################

main_menu()


