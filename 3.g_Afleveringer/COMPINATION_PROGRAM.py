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
        Subtask = input("What Subtask do you want to start? 1 or 2?: ")
        if Subtask == '1' or Subtask == '2':
            break
        print("false input. Please only enter 1 or 2 (:")
        print("")

    #Subtask = '2'
    
    def Subtask_1(): #Function to complete Subtask 1
        """
        First I assign the first, second, and third letter of the combination a value.
        The reason for this is that my inspiration for it was binary.
        example:
        000 = 0
        001 = 1
        010 = 2
        011 = 3
        but mine is not a base 2 but base 3.
        example:
        000 = aaa
        001 = aab
        002 = aac
        010 = aba
        
        To achieve this I have just assigned the first, second and third letters a value of 0, and then just plused 1 on the third letter
        until it reached 3, because each loop it checks the third letter to see if it is equal to 3.
        When third_letter == 3, it does third_letter == 0 and second_letter += 1, So now second_letter== 1 and adds 'b' to the list.
        This is to get the binary effect.
        I also made sure to put checking of the letters equaling 3 inside the if statement of the last letter so that no unnecessary checks happen.
        
        """
        """bonusopgave"""
        Total_compinations = 0
        """bonusopgave"""
        list_of_letters = []

        first_letter = 0
        second_letter = 0
        third_letter = 0

        while True:
            #if first_letter < 4:
                #print(third_letter)
            if first_letter == 0:
                list_of_letters.append('a')
            elif first_letter == 1:
                list_of_letters.append('b')
            elif first_letter == 2:
                list_of_letters.append('c')
            #if second_letter < 4:
            if second_letter == 0:
                list_of_letters.append('a')
            elif second_letter == 1:
                list_of_letters.append('b')
            elif second_letter == 2:
                list_of_letters.append('c')
                
            if third_letter == 0:
                list_of_letters.append('a')
            elif third_letter == 1:
                list_of_letters.append('b')
            elif third_letter == 2:
                list_of_letters.append('c')
            third_letter += 1
                    
        
            print(list_of_letters)
            list_of_letters = []
            
            """bonusopgave"""
            Total_compinations += 1 
            """bonusopgave"""
            
            if third_letter == 3:
                third_letter = 0
                second_letter += 1
                if second_letter == 3:
                    second_letter = 0
                    first_letter += 1
                    if first_letter == 3:
                        print(Total_compinations)
                        break
    
    
    
    
    
    def Subtask_2():
        """
        The "Subtask_2" function is a wrapper function for the actual function that does the work.
        It used to get the 2 calls i need to calculate the total combinations into 1 function.
        Also so i dont need to call 2 functions for 1 task if i have to use it, since it is much easier to type:
        "Subtask_2()" instead of "Combination(['a','b','c'])" and "Combination(['a','c','b'])"
        
        """
        
        def Combination(Letters_to_use):
            """
            Makes the combination and prints it.
            The functions takes a list of 3 letters(can also not be letters as long as there is 3) which in this case are:
            ['a','b','c']
            and
            ['a','c','b']
            It takes this list and in the for loop appends the letter of the index so the first is:
            Letters_to_use[0] = 'a'
            It then does the same under but minus 2, this is because lists kinda work like a circle if you go backwards so that:
            -3 and 0 = a
            -2 and 1 = b
            -1 and 2 = c
            If you went farther that any of these either in the negative or positive it would be out of index range
            It then returns the total combination value so we can get the total amount of possible combinations.
            
            
            
            """
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
        Subtask_1()
    else:
        Subtask_2()
    
    
    
    
    
    

if __name__ == "__main__":
    main()