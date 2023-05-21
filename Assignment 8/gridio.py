# A program to take a 9x9 list from user and print out the value at each given coordinates.
# 24 May 2021


def main():   
    array = [[], [], [], [], [], [], [], [], []]
    row = 0
    col = 0
    print("Enter an array:")
    # Store each single number in an array
    for row_index in range(9):
        arr_str = input()
        if len(arr_str.strip()) == 9 and arr_str.isdigit():
            for char in arr_str:
                array[row_index].append(eval(char))
        else:
            pass    
    # Print the value at each given coordinates
    while  row >= 0 and col >= 0:
        row, col = input("Enter coordinates:\n").split()
        row = eval(row)
        col= eval(col)
        if row >= 0 and col >= 0:
            print("Value =",array[row][col])
        else:
            print("DONE")


if __name__ == "__main__":
    main()


