import turtle

# Set up the screen
sc = turtle.Screen()
sc.title("Pinging Pongning")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("blue")
left_pad.shapesize(stretch_wid=6)
left_pad.penup()
left_pad.goto(-400, 0)

# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("red")
right_pad.shapesize(stretch_wid=6)
right_pad.penup()
right_pad.goto(400, 0)

# Ball
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("black")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Score
left_player = 0
right_player = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("orange")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Left Player: 0  Right Player: 0", align="center", font=("Courier", 24, "normal"))

# Function to update the score
def update_score():
    score_display.clear()
    score_display.write("Left Player: {}  Right Player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))

# Function to move the left paddle up
def paddle_up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)

# Function to move the left paddle down
def paddle_down():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)

# Function to move the right paddle up
def paddle_b_up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)

# Function to move the right paddle down
def paddle_b_down():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)

# Keyboard bindings
sc.listen()
sc.onkeypress(paddle_up, "w")
sc.onkeypress(paddle_down, "s")
sc.onkeypress(paddle_b_up, "Up")
sc.onkeypress(paddle_b_down, "Down")

sc.update()

# Main game loop
while True:
    sc.update()

    # Move the ball
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Border checking
    if hit_ball.ycor() > 290:
        hit_ball.sety(290)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -290:
        hit_ball.sety(-290)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 490:
        hit_ball.goto(0, 0)
        hit_ball.dx *= -1
        left_player += 1
        update_score()

    if hit_ball.xcor() < -490:
        hit_ball.goto(0, 0)
        hit_ball.dx *= -1
        right_player += 1
        update_score()

    # Paddle and ball collisions
    if (hit_ball.dx > 0) and (350 > hit_ball.xcor() > 340) and (right_pad.ycor() + 50 > hit_ball.ycor() > right_pad.ycor() - 50):
        hit_ball.color("red")
        hit_ball.setx(340)
        hit_ball.dx *= -1

    elif (hit_ball.dx < 0) and (-350 < hit_ball.xcor() < -340) and (left_pad.ycor() + 50 > hit_ball.ycor() > left_pad.ycor() - 50):
        hit_ball.color("blue")
        hit_ball.setx(-340)
        hit_ball.dx *= -1

