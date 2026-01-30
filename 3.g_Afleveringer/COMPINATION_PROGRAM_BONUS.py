"""
COMBINATIONS PROGRAM
"""
"""
The point of this program is to make combinations of 3 letters, a, b, and c.
I got assigned 2 subtasks which are:
1. "Letters can be reused, so that aaa is a valid combination"
2. "Letters can not be reused, so that aaa is NOT a valid combination"
With this I made 2 functions that do each of these subtasks, properly named "Subtask_1" and "Subtask_2"
When you start the program, you will be prompted to choose which one to run, as to make it easier to see which function does what output.
There is also 2 bonus task, in which one of them is in another program.
The tasks are as follows:
1. Calculate the number of combinations for their respective tasks
2. Make a new program that can take 1, 2, and 4 letters.
"""


def main(): #main function. Not needed but nice to have.

    while True:
        #Subtask = input("What Subtask do you want to start? 1 or 2?: ")
        Subtask = '1'
        if Subtask == '1' or Subtask == '2':
            break
        print("false input. Please only enter 1 or 2 (:")
        print("")

    #Subtask = '2'
    
    def Subtask_1(combination_list): #Function to complete Subtask 1
        """bonusopgave"""
        Total_compinations = 0
        """bonusopgave"""
        list_of_letters = []

        first_letter = 0
        second_letter = 0
        third_letter = 0


        while True :
            while_loop_breaker = False 
            #if first_letter < 4:
                #print(third_letter)
            for combination_amount in range(len(combination_list)-1):
                
                if first_letter == combination_amount:
                for Letter_in_list in range(len(combination_list)):
                    for i in range(len(combination_list)-1):
                        for List_size in range(len(combination_list)-1):
                            list_of_letters.append(combination_list[Letter_in_list])
                        list_of_letters.append(combination_list[Letter_in_list+i])
                        print(list_of_letters)
                        list_of_letters = []
                
                #list_of_letters.append(combination_list[first_letter])
                #if second_letter == combination_amount:
                #list_of_letters.append(combination_list[second_letter])
                #if third_letter == combination_amount:
                #list_of_letters.append(combination_list[third_letter])
                #third_letter += 1
            
        
                #print(list_of_letters)
                #list_of_letters = []
        
                """bonusopgave"""
                Total_compinations += 1 
                """bonusopgave"""
                
                if third_letter == len(combination_list):
                    third_letter = 0
                    second_letter += 1
                    if second_letter == len(combination_list):
                        second_letter = 0
                        first_letter += 1
                        if first_letter == len(combination_list):
                            print(Total_compinations)
                            while_loop_breaker = True
                            break 

            if while_loop_breaker == True:
                break
    
    
    
    def Subtask_2():
        """
        The "Subtask_2" function is a wrapper function for the actual function that does the work.
        It used to get the 2 calls i need to calculate the total combinations into 1 function.
        Also so i dont need to call 2 functions for 1 task if i have to use it, since it is much easier to type:
        "Subtask_2()" instead of "Combination(['a','b','c'])" and "Combination(['a','c','b'])"
        
        """
        
        def Combination(Letters_to_use):
            
            List_of_letters = []
            Total_combination = 0

            for compination in range(3):
                List_of_letters.append(Letters_to_use[compination])
                List_of_letters.append(Letters_to_use[compination-2])
                List_of_letters.append(Letters_to_use[compination-1])
                print(List_of_letters)
                List_of_letters = []
                Total_combination += 1
                
                
            return Total_combination
        
        combination_1 = Combination(['a','b','c'])
        

        combination_2 = Combination(['a','c','b'])
        Total_combination = combination_1 + combination_2
        print(Total_combination)

        
        
        
    if Subtask == '1':
        Subtask_1(['a','b','c','d'])
    else:
        Subtask_2()
    
    
    
    
    
    

if __name__ == "__main__":
    main()