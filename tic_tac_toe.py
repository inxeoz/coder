import os

def print_arr(arr):
    print("-------------")
    print("|",arr[0],"|", arr[1],"|",arr[2],"|")
    print("-------------")
    print("|",arr[3],"|", arr[4],"|",arr[5],"|")
    print("-------------")
    print("|",arr[6],"|", arr[7],"|",arr[8],"|")
    print("-------------")



def run_tic_toe():
    arr = [" "] * 9
    starter = input("Enter x or o to Start First : ").lower()[0:1]
    starter_is_cross = starter == "x"

    ender = "e"

    if starter_is_cross:
        ender  = "o"
    elif starter == "o":
        ender = "x"
    else:
        print("please Select Starter as x (alphabet x) or o (alphabet O) ")
        run_tic_toe()
        return


    for i in range(9):
        os.system("clear")
        print_arr(arr)

        turn_type = starter if i % 2 == 0 else ender

        winner_declared = take_input(arr=arr, turn_type=turn_type, starter=starter, ender=ender)
        os.system("clear")
        print_arr(arr)

        if winner_declared:

            print("Winner ", turn_type)
            return




def take_input(arr,turn_type, starter, ender):

    cell_number = -1

    cell_number = int(input(f"Enter Cell number to mark {turn_type} : "))

    if cell_number > 9 or cell_number < 1:
        print("Wrong cell Number 1 to 9 only")
        return take_input(arr=arr, turn_type=turn_type, starter=starter, ender=ender)

    if arr[cell_number - 1] != " ":
        print(f"cell number {cell_number} is Not empty")
        return take_input(arr=arr, turn_type=turn_type, starter=starter, ender=ender)

    arr[cell_number - 1] = turn_type

    return check_winner(arr=arr, turn_type=turn_type)


def check_winner(arr, turn_type):

    top_horizontal = arr[0] == arr[1] == arr[2] == turn_type
    mid_horizontal = arr[3] == arr[4] == arr[5] == turn_type
    bottom_horizontal = arr[6] == arr[7] == arr[8] == turn_type

    left_vertical= arr[0] == arr[3] == arr[6] == turn_type
    mid_vertical = arr[1] == arr[4] == arr[7] == turn_type
    right_vertical = arr[2] == arr[5] == arr[8] == turn_type

    top_left_to_bottom_right_diagonal = arr[0] == arr[4] == arr[8] == turn_type
    top_right_to_bottom_left_diagonal = arr[2] == arr[4] == arr[6] ==  turn_type


    return top_horizontal or mid_horizontal or bottom_horizontal or left_vertical or mid_vertical or right_vertical or top_left_to_bottom_right_diagonal or top_right_to_bottom_left_diagonal

    

run_tic_toe()
