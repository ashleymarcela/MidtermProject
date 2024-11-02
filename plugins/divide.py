'''Module responsible for division functions in the Advanced Python Calculator'''
def divide(x,y):
    '''returns the quotient of x and y'''
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
