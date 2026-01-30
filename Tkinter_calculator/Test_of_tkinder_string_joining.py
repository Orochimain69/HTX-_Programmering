
list_of_numbers = ['0','1','2','3','4','5','6','7','8','9']


def output(number):
    entrytext.insert(tk.END,
                         number
                         )
  



for i in list_of_numbers:
    btn = tk.Button(root, text=i, command=output(i))
    btn.pack()
