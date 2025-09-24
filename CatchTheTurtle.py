import turtle
import random

#Screen settings
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Catch the Turtle")
wn.setup(width=800, height=600)

#Turtle
catchTheTurtle = turtle.Turtle()
catchTheTurtle.shape("turtle")
catchTheTurtle.color("green")
catchTheTurtle.penup()


#Score text
score = 0
score_turtle = turtle.Turtle()
score_turtle.color("red")
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0,260)
score_turtle.write(f"Score: {score} ", align="center", font=("Arial", 24, "normal"))

#Timeline
time_left = 10
time_turtle = turtle.Turtle()
time_turtle.color("red")
time_turtle.penup()
time_turtle.hideturtle()
time_turtle.goto(0,230)
time_turtle.write(f"Time: {time_left} ", align="center", font=("Arial", 24, "normal"))


# move_turtle
def move_turtle():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_turtle.clear()
        time_turtle.write(f"Time: {time_left} ", align="center", font=("Arial", 24, "normal"))
        rand_x = random.randint(-250, 250)
        rand_y = random.randint(-250, 250)
        catchTheTurtle.goto(rand_x, rand_y)
        wn.ontimer(move_turtle, 1000)
    else:
        game_over()


#Click turtle to increase score
def click_turtle(x,y):
    global score
    score+=1
    score_turtle.clear()
    score_turtle.write(f"Score: {score} ", align="center", font=("Arial", 24, "normal"))

catchTheTurtle.onclick(click_turtle)

#Game Over Function
def game_over():
        catchTheTurtle.hideturtle()
        score_turtle.goto(0, 0)
        score_turtle.clear()
        time_turtle.clear()
        score_turtle.write(f"Oyun bitdi!\nSon Score: {score}", align="center", font=("Arial", 24, "bold"))


move_turtle()

wn.mainloop()