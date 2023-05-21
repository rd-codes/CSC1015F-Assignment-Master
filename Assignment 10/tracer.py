# A program that assist with debugging Python programs, by adding trace statements
# 09 June 2021


print("***** Program Trace Utility *****")
pfilename = input("Enter the name of the program file: ").strip()
file = open(pfilename, 'r')
tempf = open("tempf.py", 'w')  # For temporarily writing a file with/without debugging statements   

count = 0
posFunction = 0

# Make a copy of a python file given by user and add trace statements in it only if it does not have them
first_line = file.readline()
if first_line != "\"\"\"DEBUG\"\"\"\n":
    for line in file:
        count += 1
        # Insert trace statement in the first line, and move all the characters on the line to the next line unchanged
        if count == 1:
            print("\"\"\"DEBUG\"\"\"\n", first_line, line, file=tempf, sep="", end="")
            # Read the name of a function and position of a line after a signature line of each function
        elif "def " in line:
            f_name = ""
            line_chars = line.strip().split(" ")
            for char in line_chars[1]:
                if char != "(" and char != " ":
                    f_name += char
                else:
                    break
            print(line, file=tempf, sep="", end="")
            posFunction = count + 1

        # Insert  trace statement after a signature line of a function, indented with 4 spaces
        # along with a semicolon and a print statement to print the function name
        elif count == posFunction:
            print("    \"\"\"DEBUG\"\"\"", ";", "print('{}')\n".format(f_name), line, file=tempf, sep="", end="")
        else:
            print(line, file=tempf, sep="", end="")
    file.close()
    tempf.close()
    # Overwrite the function with its copy that has trace statements
    new_tempf = open("tempf.py", 'r')
    new_file = open(pfilename, "w")
    for char in new_tempf:
        new_file.write(char)

    print("Inserting...Done")

    new_tempf.close()
    new_file.close()

# Remove trace statements if a function already has them
else:
    print("Program contains trace statements")
    # Rewrite the file in a temporarily file without its trace statements
    for line in file:
        if "\"\"\"DEBUG\"\"\"" not in line:
            print(line, file=tempf, sep="", end="")
        else:
            pass
    file.close()
    tempf.close()
    # Overwrite the function with its original copy that has no trace statement
    new_tempf = open("tempf.py", 'r')
    original_f = open(pfilename, 'w')
    for char in new_tempf:
        original_f.write(char)
    print("Removing...Done")
    new_tempf.close()
    original_f.close()
