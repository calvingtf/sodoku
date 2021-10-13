import time
'''
using backtracking algorithm
1. find some empty space
2. Attempt to place the digits 1-9 in that space
3. Check if that digit is valid in the current spot based on the current board
4a If the digit is valid, recursively attempt to fill the board using steps 1-3.
b. If it is not valid, reset the square you just filled and go back to the previous step.
5. Once the board is full by the definition of this algorithm we have found a solution.
'''

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(bo):
    #print(bo)
    # keep backtracking until reach the valid solution
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    #loop through 1-10. if valid we add to board
    #  we call function solve again until the number is valid then true
    # if we can't finish with the value..we continue to loop through
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check each element in the row
    # check if the num we just insert then we will ingore the position
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check  column vertically
    # check the number for other position
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    # Checking each box
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    #pritn out the layout
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
            #print horizonal line every third time

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                #check if it is the thrid of the element

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
                # stay on the same line

# find the empty square
# return to the position whatever we call it from

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
start = time.time()
solve(board)
print("_______Solution________")
end=time.time()
print_board(board)
print(end - start)

