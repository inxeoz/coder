import os
import random
import keyboard
import time

AUTO_PILOT = False
MOVE_DELAY = 0.15
last_move_time = 0

SCORE = 0

BRIGHT_GREEN = "\033[92m"
BRIGHT_RED = "\033[31m"
BG = "\033[30m"
RESET = "\033[0m"

GRID = "██"
GRID_SIZE = 20

DIRECTION = "STALL"
MAX_BOARD_HEIGHT = 10
MAX_BOARD_WIDTH = 10

MAX_SNAKE_SIZE = MAX_BOARD_HEIGHT * MAX_BOARD_WIDTH

board = [[0] * MAX_BOARD_WIDTH for _ in range(MAX_BOARD_HEIGHT)]
snake_body = [[0, 0]]

food_pos = [MAX_BOARD_HEIGHT // 2, MAX_BOARD_WIDTH //2 ]


def print_board():
    os.system("clear")

    mapping = {0: BG + GRID + RESET, 1: BRIGHT_GREEN + GRID + RESET, 2: BRIGHT_RED + GRID + RESET}

    result = "\n".join("".join(mapping[v] for v in row) for row in board)

    print(result)


def render():
    global board
    board = [[0] * MAX_BOARD_WIDTH for _ in range(MAX_BOARD_HEIGHT)]

    for block in snake_body:
        row, col = block
        board[row][col] = 1

    print(food_pos)
    row, col = food_pos
    board[row][col] = 2

    print_board()


def snake_move_carry(
    block_number: int = -1,
    updated_block_row: int = -1,
    updated_block_col: int = -1,
):
    render()

    if block_number < 0 or block_number > len(snake_body) - 1:
        return

    old_block_row, old_block_col = snake_body[block_number]

    snake_body[block_number][0] = updated_block_row
    snake_body[block_number][1] = updated_block_col

    snake_move_carry(
        block_number=block_number - 1,
        updated_block_row=old_block_row,
        updated_block_col=old_block_col,
    )


def snake_move():

    global SCORE
    render()

    if DIRECTION == "STALL":
        return
    # block_number inclusive (0, len(snake_body) - 1 )
    # print()
    #
    #

    block_number = len(snake_body) - 1
    block_row, block_col = snake_body[block_number]
    old_block_row = block_row
    old_block_col = block_col

    # print("block ", block_number, ":", block_row, block_col)
    if DIRECTION == "down":
        block_row = block_row + 1
        if block_row > MAX_BOARD_HEIGHT - 1:
            end_snake(f"out of boundary :down {block_row}")
            return

    if DIRECTION == "up":
        block_row = block_row - 1

        if block_row < 0:
            end_snake("out of boundary : up")
            return

    if DIRECTION == "left":
        block_col = block_col - 1
        if block_col < 0:
            end_snake("out of boundary :left")
            return

    if DIRECTION == "right":
        block_col = block_col + 1
        if block_col > MAX_BOARD_WIDTH - 1:
            end_snake("out of boundary :right")
            return

    render()

    if board[block_row][block_col] == 1:
        print("you hit youself")
        end_snake()


    food_row, food_col = food_pos
    if food_row == block_row and food_col == block_col:
        snake_body.append([food_row, food_col])
        SCORE += 1
        new_snake_food()

        snake_move_carry(
        block_number=block_number - 1,
        updated_block_row=old_block_row,
        updated_block_col=old_block_col,
        )



        # snake_move()
    #
    snake_body[block_number] = [block_row, block_col]

    snake_move_carry(
        block_number=block_number - 1,
        updated_block_row=old_block_row,
        updated_block_col=old_block_col,
    )
    



def new_snake_food():
    global food_pos
    food_location = []

    render()
    for row_i in range(0, MAX_BOARD_HEIGHT):
        for col_i in range(0, MAX_BOARD_WIDTH):
            if board[row_i][col_i] == 0 :
                food_location.append([row_i, col_i])
                # food_pos = [row_i, col_i]
    if len(food_location) == 0:
        end_snake() 
    
    index = random.randint(0, len(food_location)-1)
    food_pos = food_location[index]
    render()

   

       

def end_snake(message:str|None=None):

    print("Your Score : " , SCORE)

    if message:
        print(message)

    exit()

def configure():
    global AUTO_PILOT

    print("keyboard button : up / down / left / right ")
    speed_run  = input("Enable auto pilot run y/n ")[0:1].lower()
    print(speed_run == "y")
    AUTO_PILOT = speed_run == "y"

    # exit()
    


def run_snake():
    global last_move_time, DIRECTION

    configure()

    print("Press arrow keys (ESC to quit)")
    render()

    last_move_time = time.time()

    while True:
        current_time = time.time()

        # AUTO PILOT: always moves every MOVE_DELAY in current direction
        if AUTO_PILOT and current_time - last_move_time >= MOVE_DELAY:
            snake_move()
            last_move_time = current_time

        # MANUAL CONTROL:
        #   - In auto pilot: keys only change direction
        #   - In manual mode: keys both change direction and move step-by-step
        if keyboard.is_pressed("up"):
            DIRECTION = "up"
            if not AUTO_PILOT and current_time - last_move_time >= MOVE_DELAY:
                snake_move()
                last_move_time = current_time

        elif keyboard.is_pressed("down"):
            DIRECTION = "down"
            if not AUTO_PILOT and current_time - last_move_time >= MOVE_DELAY:
                snake_move()
                last_move_time = current_time

        elif keyboard.is_pressed("left"):
            DIRECTION = "left"
            if not AUTO_PILOT and current_time - last_move_time >= MOVE_DELAY:
                snake_move()
                last_move_time = current_time

        elif keyboard.is_pressed("right"):
            DIRECTION = "right"
            if not AUTO_PILOT and current_time - last_move_time >= MOVE_DELAY:
                snake_move()
                last_move_time = current_time

        if keyboard.is_pressed("esc"):
            break


run_snake()

