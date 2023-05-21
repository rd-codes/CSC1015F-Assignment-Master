# using main as the name

def life(D=5,d =5,b):
    D = input(5)
    print(D)
    return "Life is game made for everyone,"

def special():
    global  b
    b = 10
def love():
    return "and love is the price."

def needs():
    print(b)
    return """So wake me up when it's all over
when I am wiser and I am older. 
Cause all this time I was finding my self, and I didn't know I was lost.
    """

if __name__ == "__main__":
    print(life(),love(),needs())
    
    


