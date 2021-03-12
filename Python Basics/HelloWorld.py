# This program says Hello and asks for your name

print('Hello World!')

print('What is your name?: ')
yourName = input()
print('Nice meeting you, ' + yourName)
print('The length of you name is: ')
print(len(yourName))
print('characters.')

print('And what\'s your age?: ')
yourAge = input()
print('You will be ' + str(int(yourAge) + 1) + " in a year from now!")
