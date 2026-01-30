import tkinter as tk

root = tk.Tk()
entrytext = tk.Entry(root)
entrytext.pack()
entrytext.insert(0,'meow')
print(entrytext.get())

def output():
    print('hello')


button = tk.Button(root, text='meow2', command=output)
button.pack()



def main():
    
    
    """
    while true to make sure the program keeps going,
    instead of having to start it constantly
    """
    while True:
        print("you can enter End at any point to stop the program")
        print("")
        
        number_1 = first_number()
        if number_1 == "End" and "end" and "END":
            break
        operation1 = operation()
        if operation1 == "End" and "end" and "END":
            break
        number_2 = second_number()
        if number_2 == "End" and "end" and "END":
            break
        result = calculation(number_1, number_2, operation1)
        return result 	

#def check_for_end(end):
"""
meant to check for multiple types of "end" in the inputs to check if the user wants to stop the program.
(sadly didnt work bc 'break outside loop") 
"""
        
    #if end == "End" or "end" or "END":
        #break


def first_number(): #the first number entered
    
    while True:
        """
        couldnt make the test work on this
        """
        number_1 = input('Number 1  >')
        if number_1.isnumeric() == True:
            return number_1
            break
        else:
            print('pls enter a numeric value')
            print('')
         
        
def operation(): #the operation entered
    operation1 = input('Operation +-*/  >')
    
    #check_for_end(operation)
        
        
    return operation1

def second_number():#same as first number
    
    while True:
        """
        couldnt make the test work on this, tried making a variable that could be true or false and that would be what it was looking for but it didnt work
        """
        number_2 = input('Number 2  >')
        #T_or_F = number_2.isnumeric()
        #return T_or_F
        if number_2.isnumeric() == True:
            return number_2
            break
        else:
            print('pls enter a numeric value')
            print('')


def calculation(number_1, number_2, operation): #does the calculation and prints the result
    
    if operation == '+':
            result = float(number_1) + float(number_2)
    if operation == '-':
            result = float(number_1) - float(number_2)
    if operation == '*':
            result = float(number_1) *  float(number_2)
    if operation == '/':
        if number_1 == '0':
            result = 'undefined'
        else:
                if number_2 == '0':
                    result = 'undefined'
                else:
                    result = float(number_1) / float(number_2)
            
            
    if result == 'undefined':
        print('undefined')
        return result
    else:    
        if result-int(result) == result - result:
            print("")
            print("________")
            print(int(result))
            print("________")
            print("")
            return result
        else:
            result = int(result * 100)/100
            
            
            print("")
            print("________")
            print(result)
            print("________")
            print("")
            return result
        
root.mainloop()

#if __name__ == '__main__':
    #main()
#result = main()