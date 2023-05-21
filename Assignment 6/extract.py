# A program to extract useful data from a raw data stream obtained from a sensor.
# 01 May 2021

def location(block):
    # Use the range of the location to extract the location block
    for pos_char in range(block.find(","), len(block)):
        if block[pos_char] == " ":
            location_begin = pos_char + 1
            break
    location_end = block.find("END")-1
    location_block = block[location_begin : location_end]
    return location_block[::-1].title()


def temperature(block):
    temp_begin = block.find("BEGIN")+ len("BEGIN") # Check the position of the first number that comes after the word "BEGIN"
    temp_end = block.find("_")
    return float(block[temp_begin + 1 : temp_end])


def x_coordinate(block):
    x_begin = block.find(":")
    x_end = block.find(",")
    return block[x_begin + 1 : x_end]

def y_coordinate(block):
    y_coord = ""
    # Use the range of the y_coordinate to extract the y_coordinate
    for pos_char in range(block.find(",") + 1, len(block)):
        if not(block[pos_char] == " "):
            y_coord = y_coord + block[pos_char]
        else:
            break
    return y_coord
             

def pressure(block):
    pressure_begin = block.find("_")
    pressure_end = block.find(":")
    return float(block[pressure_begin + 1 : pressure_end])


def get_block(data):
    block_begin= data.find("BEGIN")
    block_end = data.find("END")
    return data[block_begin : block_end + len("END")]


def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))


if __name__=='__main__':
    main()
