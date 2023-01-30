def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0

spam()
#this print will error out as eggs is only defined in the local scope
