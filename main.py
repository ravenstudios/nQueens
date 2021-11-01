# Robert Dodson RavenStudios 11/1/21
import math



# print("nQuees")

result = [];
n = 4;



def place_queen(row):
    if row > n:
        return
# loop through each col in a row and try to place a queen
#  if backtracking start the loop at the next col that the previous result

    for_start = row * n
    for_stop = row * n + n

    if len(result) > row:

        for_start = result[row] + 1
        result.pop()


    for i in range(for_start, for_stop, 1):
        if check_is_col_safe(i) and check_is_row_safe(i) and check_is_diag_safe(i):
            # if we can place a queen the we place it and call place again with new row
                    result.append(i)
                    if len(result) == n:
                        print(result)
                        return

                    place_queen(row + 1)
                    return
    place_queen(row - 1)



def check_is_row_safe(pos):# returns true if safe to place in row
    row = math.floor(pos / n)
    col = pos % n

    if pos in result:
            return False

    return True



def check_is_col_safe(pos):

    nums = []
    row = math.floor(pos / n)
    col = pos % n

    for i in range(n):
        nums.append(col + (i * n))

    for num in nums:
        if num in result:
            return False

    return True


def check_is_diag_safe(pos):
    # check result list against pos
    nums = []
    row = math.floor(pos / n)
    col = pos % n

    for i in range(len(result)):
        temp_pos = result[i]
        temp_pos_row = math.floor(temp_pos / n)
        temp_pos_col = temp_pos % n

        delta_row = abs(row - temp_pos_row)
        delta_col = abs(col - temp_pos_col)

        # print("delta row: ", delta_row, " deltaCol: ", delta_col)
        if delta_row == delta_col:
            return False

    return True;


place_queen(0)
