def eggs(chees):
    chees.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)


# PS C:\Users\tcailleau\Documents\Python\AtBSwPython> & C:/tools/Anaconda3/python.exe c:/Users/tcailleau/Documents/Python/AtBSwPython/Lists/listReferenceEx.py
# [1, 2, 3, 'Hello']

# [1, 2, 3, 'Hello'] becuase the reference to the list did modify the list even if chees get distroyed in the local scope


