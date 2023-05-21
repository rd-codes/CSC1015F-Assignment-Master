# A program to take a list of values and print it out in the exact given order excluding duplicates
# 23 May 2021


def main():
    print("Enter strings (end with DONE):")
    list_val = []
    while "DONE" not in list_val:
        val = input()
        # Add each unique value entered by user to a list 
        if val not in list_val:
            list_val.append(val)
    list_val.remove("DONE")                  # Remove DONE since it shouldn't be part of list
    print()
    print("Unique list:")
    for i in range(len(list_val)):
        print(list_val[i])
        

if __name__ == "__main__":
    main()

