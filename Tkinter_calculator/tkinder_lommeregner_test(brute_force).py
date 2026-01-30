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
    
    def validation_of_key_entry(text):
        return text.isdecimal()
    
    entrytext = tk.Entry(root,
                         validate='key',
                         validatecommand=(root.register(validation_of_key_entry), '%S')
                         )
    
    entrytext.pack()
    entrytext.insert(tk.END,'')
    #print(entrytext.get())
    """
    above we have decided to call tk.Tk() for root. tk.Tk() is what starts our Tkinter program, and at the end is a root(tk.Tk()).mainloop() function
    this is what finishes the loop so that the program works.

    then we also just make an entrytext with is a text that can be wrote inside of.
    we then pack it because of Tkinters need to pack things before getting visualized.


    """


    
    def output0():
        entrytext.insert(tk.END,
                         '0'
                         )
    
    def output1():
        entrytext.insert(tk.END,
                         '1'
                         )
    
    def output2():
        entrytext.insert(tk.END,
                         '2'
                         )
    
    def output3():
        entrytext.insert(tk.END,
                         '3'
                         )
    
    def output4():
        entrytext.insert(tk.END,
                         '4'
                         )
    
    def output5():
        entrytext.insert(tk.END,
                         '5'
                         )
    
    def output6():
        entrytext.insert(tk.END,
                         '6'
                         )
    
    def output7():
        entrytext.insert(tk.END,
                         '7'
                         )
    
    def output8():
        entrytext.insert(tk.END,
                         '8'
                         )
    
    def output9():
        entrytext.insert(tk.END,
                         '9'
                         )
    
    def result():
        Result_window = tk.Toplevel(root)
        Result_window.title('Result Window')
        #Result_text = entrytext.get()
        
        Result_label = tk.Label(Result_window,
                                text=entrytext.get()
                                )
        
        Result_label.pack()
        print(entrytext.get())
        #print(entrytext.get())
        

    button0 = tk.Button(root, text='0', command=output0)
    button0.pack()
    button1 = tk.Button(root, text='1', command=output1)
    button1.pack()
    button2 = tk.Button(root, text='2', command=output2)
    button2.pack()
    button3 = tk.Button(root, text='3', command=output3)
    button3.pack()
    button4 = tk.Button(root, text='4', command=output4)
    button4.pack()
    button5 = tk.Button(root, text='5', command=output5)
    button5.pack()
    button6 = tk.Button(root, text='6', command=output6)
    button6.pack()
    button7 = tk.Button(root, text='7', command=output7)
    button7.pack()
    button8 = tk.Button(root, text='8', command=output8)
    button8.pack()
    button9 = tk.Button(root, text='9', command=output9)
    button9.pack()
    button_result= tk.Button(root, text='enter', command=result)
    button_result.pack()


    root.mainloop()


if __name__ == '__main__':
    main()
    

