print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats!')
    elif int(numCats) < 0:
        print('I am not talking about the cats you gave away!')
    else:
        print('One never has enough cats!')
except ValueError:
    print('You did not enter an Number!')