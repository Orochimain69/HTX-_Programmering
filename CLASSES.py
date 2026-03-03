#classes


class data_container:
    value1 = 10
    value2 = 20


data_container.new_var = 5


print("global scope")
print(data_container.new_var)



global_var = 7

def my_function():
    #print(data_container.new_var)
    print("local scope")
    
    #print(global_var)
    #global_var = 5
    #print(global_var)
    """virker ikke"""
    
    """virker"""
    print(data_container.new_var)
    data_container.new_var = 8
    print(data_container.new_var)


    
my_function()