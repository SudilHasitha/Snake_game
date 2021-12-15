import turtle
import random

# Define constants
WIDTH = 500
HEIGHT = 500
DELAY = 400 
FOOD_SIZE = 20

# create dictionary for offsets
offsets = {
    "up":(0,20),
    "down":(0,-20),
    "left":(-20,0),
    "right":(20,0)
}

# u cant turn 180
# define the call back functions
# def go_left():
#     global snake_direction
#     if snake_direction != "right":
#         snake_direction = "left"

# def go_right():
#     global snake_direction
#     if snake_direction != "left":
#         snake_direction = "right"

# def go_down():
#     global snake_direction
#     if snake_direction != "up":
#         snake_direction = "down"

# def go_up():
#     global snake_direction
#     if snake_direction != "down":
#         snake_direction = "up"

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"),"Up")
    screen.onkey(lambda: set_snake_direction("down"),"Down")
    screen.onkey(lambda: set_snake_direction("left"),"Left")
    screen.onkey(lambda: set_snake_direction("right"),"Right")

def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down": # no self collision 180 not possible
            snake_direction = "up"
    elif direction == "down":
        if snake_direction != "up":
            snake_direction = "down"
    elif direction == "left":
        if snake_direction != "right":
            snake_direction = "left"
    elif direction == "right":
        if snake_direction != "left":
            snake_direction = "right"

def reset():
    global score, food_position, snake, snake_direction

    # create the representation of snake as coordinates
    snake = [[0,0],[20,0],[40,0],[60,0]]
    # use a snake direction as up
    snake_direction = "up"
    score = 0
    food_position = get_food_position()
    food.goto(food_position)
    game_loop()


# create method to move the snake
def game_loop():
    # remove the existing stamps
    stamper.clearstamps()
    # get the copy of last coordiante pairs
    new_head = snake[-1].copy()
    # update the x coordiante point in the list
    new_head[0] += offsets[snake_direction][0]
    # update the y coordinate point in the list
    new_head[1] += offsets[snake_direction][1]

    # Check for the collisions with itself then with the walls
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 or new_head[1] < -HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset()
    # if there is no collision
    else:  
        # add the new head to the list
        snake.append(new_head)

        # check food collision
        if not food_collison():
            # remove the first element k
            # keep the snake same length
            snake.pop(0)

        # Draw the snake for the 1st time
        for segment in snake:
            stamper.goto(segment[0],segment[1])
            stamper.stamp()

        # render the screen
        screen.title(f"Snake Game , Score {score}")
        screen.update()

        # update the movement of the snake i.e repeat the method
        turtle.ontimer(game_loop,DELAY)

# get food collision 
def food_collison():
    global food_position,score
    if get_distance(snake[-1],food_position)<20:
        food_position = get_food_position()
        food.goto(food_position)
        score += 1
        return True
    return False

# get the food position 
# the distance between two points
def get_food_position():
    x = random.randint(-WIDTH/2+FOOD_SIZE,WIDTH/2-FOOD_SIZE)
    y = random.randint(-HEIGHT/2+FOOD_SIZE,HEIGHT/2-FOOD_SIZE)

    return (x,y)

# get the distance between two points using the pythogorous theorem
def get_distance(pos1,pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    distance = ((x2-x1)**2+(y2-y1)**2)**0.5
    return distance

# create window
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.title("Snake Game")
screen.bgcolor("pink")
screen.tracer(0) # turning off automatic animation

# create a event handler
screen.listen()
# specify the callback functions
# screen.onkey(go_up,"Up")
# screen.onkey(go_down,"Down")
# screen.onkey(go_right,"Right")
# screen.onkey(go_left,"Left")
bind_direction_keys()


# create a turtle that is not drawing on the screen
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()



# # Draw the snake for the 1st time // snake doesn't exist until reset is calledS
# for segment in snake:
#     stamper.goto(segment[0],segment[1])
#     stamper.stamp()

# Create a Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE/20)
food.penup()

# set the initial move the subsequent moves done by ontimer
reset()

# finish the execution by pressing x in the window
turtle.done()