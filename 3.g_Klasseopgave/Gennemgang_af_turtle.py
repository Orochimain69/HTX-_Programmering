"""

recursive turtle function

"""

import turtle


pen = turtle.Turtle()

LENGTH = 100
ANGLE = 60

def main():
    
    pen.speed(0)
    recursive_function(max_level = 10,level = 0, length = LENGTH, angle = ANGLE)

    pen.done()

def recursive_function(max_level,level, length, angle):
    pen.forward(length)
    if level == max_level:
        return
    pen.forward(length)
    pen.left(angle)
    pen.forward(length)
    pen.right(angle*2)
    pen.forward(length)
    pen.left(angle)
    
    recursive_function(max_level, level+1, length/2, angle)
    
    


if __name__ == "__main__":
    main()
