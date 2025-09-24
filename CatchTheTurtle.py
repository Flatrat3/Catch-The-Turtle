import turtle


#Screen settings
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Catch the Turtle")
wn.setup(width=800, height=600)

#Turtle
catchTheTurtle = turtle.Turtle()
catchTheTurtle.shape("turtle")
catchTheTurtle.color("green")


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
time_turtle.write(f"Time: {score} ", align="center", font=("Arial", 24, "normal"))


wn.mainloop()