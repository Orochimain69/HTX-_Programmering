"""
READ PY FIL
"""

def main():
    file = r"C:\HTX_Programmering\3.g_Klasseopgave\Reading_of_py_file\Reading_of_py.py"

    
    open_file = open(file, 'r')
    
    content = open_file.read()
    
    print(content)
    
    
    
    
    
if __name__ == "__main__":
    main()