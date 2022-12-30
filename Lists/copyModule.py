
import copy

spam = ['A','B','C','D']
cheese = copy.deepcopy(spam)
cheese.append('Hello')
print(spam)
print(cheese)