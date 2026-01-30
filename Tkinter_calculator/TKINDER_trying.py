import tkinter as tk
"""
This program is a follow up to our other assignment about making a calculator in python.
The objectiv is to make a GUI for a calculator that actually works.
To do this we will use Tkinter, which is a module that can make a GUI
"""


"""
first we make a main function to get everything in one function
"""
def main():

    root = tk.Tk()
    
    #def validation_of_key_entry(text):
        #return text.isdecimal()
    
    #entrytext = tk.Entry(root,
                         #validate='key',
                         #validatecommand=(root.register(validation_of_key_entry), '%S')
                         #)
    entrytext = tk.Entry(root)
    
    entrytext.pack()
    entrytext.insert(tk.END,'')
    #print(entrytext.get())
    """
    above we have decided to call tk.Tk() for root. tk.Tk() is what starts our Tkinter program, and at the end is a root(tk.Tk()).mainloop() function
    this is what finishes the loop so that the program works.

    then we also just make an entrytext with is a text that can be wrote inside of.
    we then pack it because of Tkinters need to pack things before getting visualized.


    """
    def output(number):
        entrytext.insert(tk.END,
                             number
                             )
  
    
    list_of_numbers = ['0','1','2','3','4','5','6','7','8','9']


    """
    Lambda are anonymous functions that doesnt have a name, and therefore can not be called but rather they are used instantly.
    """
    for i in list_of_numbers:
        btn = tk.Button(root, text=i, command=lambda i=i: output(i))
        btn.pack()

    def calculation_of_string():
        Result_before_split = entrytext.get()
        List_for_calc = Result_before_split.split
        
        
    

    def result():
        Result_window = tk.Toplevel(root)
        Result_window.title('Result Window')
        #Result_text = entrytext.get()
        
        Result_label = tk.Label(Result_window,
                                text=calculation_of_string()
                                )
        
        Result_label.pack()
        print(entrytext.get())
        #print(entrytext.get())
        


    button_result= tk.Button(root, text='enter', command=result)
    button_result.pack()


    root.mainloop()


if __name__ == '__main__':
    main()
    
