import math



# print("nQuees")

result = [];
n = 4;



def place_queen():

    for i in range(n * n):
        if check_col(i) == False:
            result.append(i)

        i += 1




# returns true if safe to place in row
def check_row(pos):
    row = math.floor(pos / n)
    col = pos % n

    try:
        if result[row]:
            return True
    except:
        return False


# [ 0][ 1][ 2][ 3]
# [ 4][ 5][ 6][ 7]
# [ 8][ 9][10][11]
# [12][13][14][15]



def check_col(pos):
    row = math.floor(pos / n)
    col = pos % n


    nums = []

    for i in range(n):

        x = pos + (i * n)
        if  x < n * n:
            nums.append(x)

        x = pos - (i * n)
        if x > -1:
            nums.append (x)

    for n in nums:
        if pos == n:
            return True

    return False


# place_queen()
check_col(9)

# print(check_col(0))
