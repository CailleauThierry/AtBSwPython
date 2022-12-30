# this print the global variable from the local scope of the function
def spam():
    print(eggs)

eggs = 42
spam()

# this print the local variable from the local scope of the function
def spam():
    eggs = 'Hello' # an assignment on a variable makes the local scope prioritary
    print(eggs)

eggs = 42
spam()
print(eggs) # we are back in the global scope

def spam():
    global eggs # thisd instructs the function to override the assignment and use the global variable instead
    eggs = 'Hello' # an assignment on a variable makes the local scope prioritary
    print(eggs)

eggs = 42
spam()
print(eggs) # we are back in the global scope

