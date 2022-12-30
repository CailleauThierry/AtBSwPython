def spam():
    eggs = 99

spam()
#this print will error out as eggs is only defined in the local scope
print(eggs)


# PS C:\Users\tcailleau\Documents\Python\AtBSwPython> & C:/ProgramData/Anaconda3/python.exe c:/Users/tcailleau/Documents/Python/AtBSwPython/Functions/LocalScope.py
# Traceback (most recent call last):
#   File "c:/Users/tcailleau/Documents/Python/AtBSwPython/Functions/LocalScope.py", line 6, in <module>
#     print(eggs)
# NameError: name 'eggs' is not defined
