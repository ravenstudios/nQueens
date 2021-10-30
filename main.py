import math



# print("nQuees")

result = [];
n = 4;



def place_queen():

    for i in range(n * n):
        if check_is_col_safe(i) and check_is_row_safe(i) and check_is_diag_safe(i):
            result.append(i)

        i += 1

    print(result)


def check_is_row_safe(pos):# returns true if safe to place in row
    row = math.floor(pos / n)
    col = pos % n

    try:
        if result[row]:
            return False
    except:
        return True



def check_is_col_safe(pos):
    nums = []
    row = math.floor(pos / n)
    col = pos % n

# build a list of numbers in the same col as pos.
# remove all numbers < 0 and  > n²

    # build all the numbers above pos
    for i in range(n):
        x = pos + (i * n)
        if  x < n * n and x != pos:
            nums.append(x)
        # builds all the nubers bellow pos
        x = pos - (i * n)
        if x > -1 and x != pos:
            nums.append (x)
    # returns true if result[col] is in nums
    for num in nums:
        try:
            if result[col] == num:
                return False
        except:
            return True

# # print(check_is_col_safe(0))
# [ 0][ 1][ 2][ 3]
# [ 4][ 5][ 6][ 7]
# [ 8][ 9][10][11]
# [12][13][14][15]
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


# check_is_diag_foward_safe(11)
#
place_queen()
# print(result)
# # check_is_col_safe(9)
#
