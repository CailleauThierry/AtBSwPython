# global scope ------------------
spam = 42 # global variable
 # function's local scope --------
def eggs():
    spam = 42 #local variable
 # end of function's local scope --------
print('Some code here')
print('Some more code')
# end of global scope ------------------

""" 
PS C:\Users\tcailleau\Documents\Python\AtBSwPython> & C:/ProgramData/Anaconda3/python.exe c:/Users/tcailleau/Documents/Python/AtBSwPython/Functions/GlobalLocalScope.py 
Some code here
Some more code 
"""