#! python3

import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

print(phoneRegex)

# re.compile('\\d\\d\\d -\\d\\d\\d-\\d\\d\\d\\d')

mo = phoneRegex.findall('''This is my number 147-1234 if you want my other number it is 080-147-4321 
This is my number 147-0123 if you want my other number it is 080-147-0123 '
''')
print(mo)

# PS C:\Users\tcailleau\Documents\Python\AtBSwPython> & C:/tools/Anaconda3/python.exe c:/Users/tcailleau/Documents/Python/AtBSwPython/10.RegularExpressions/RegexCharaterClasses.py
# re.compile('\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d')
# ['080-147-4321', '080-147-0123']

phoneRegex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneRegex1.findall('''This is my number 147-1234 if you want my other number it is 080-147-4321 
This is my number 147-0123 if you want my other number it is 080-147-0123
''')
print(mo)

# PS C:\Users\tcailleau\Documents\Python\AtBSwPython> & C:/tools/Anaconda3/python.exe c:/Users/tcailleau/Documents/Python/AtBSwPython/10.RegularExpressions/RegexCharaterClasses.py
# re.compile('\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d')
# ['080-147-4321', '080-147-0123'] # return a list of strings
# [('080', '147-4321'), ('080', '147-0123')]  # if you create regex groups it returmns tupples

phoneRegex2 = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
mo = phoneRegex2.findall('''This is my number 147-1234 if you want my other number it is 080-147-4321 
This is my number 147-0123 if you want my other number it is 080-147-0123
''')
print(mo)

# [('080-147-4321', '080', '147-4321'), ('080-147-0123', '080', '147-0123')]

# now looking at Charater Classes

digitRegex = re.compile(r'(0|1|2|3|4|5|6|7|8|9)')
mo = digitRegex.search('Is there a number 3')
print(mo)

digitRegex = re.compile(r'(\d)') # the \d digital Charater Class is a huge shortcut
mo = digitRegex.search('Is there a number 3')
print(mo)

# <re.Match object; span=(18, 19), match='3'>
# <re.Match object; span=(18, 19), match='3'>

lyrics = """12 drummers drumming, 11 pipers piping, 10 lords a leaping,
9 ladies dancing, 8 maids a milking, 7 swans a swimming,
6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens,
2 turtle doves, 1 partridge in a pear tree"""

xmasReged = re.compile(r'\d{1,2} \w+')
mo = xmasReged.findall(lyrics)
print(mo)

# ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 golden', '4 calling', '3 french', '2 turtle', '1 partridge']

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall(lyrics)
print(mo)

# ['u', 'e', 'u', 'i', 'i', 'e', 'i', 'i', 'o', 'a', 'e', 'a', 'i', 'a', 'i', 'e', 'a', 'i', 'a', 'i', 'a', 'i', 'i', 'a', 'a', 'i', 'i', 'e', 'e', 'e', 'a', 'a', 'i', 'o', 'e', 'i', 'a', 'i', 'i', 'e', 'e', 'u', 'e', 'o', 'e', 'a', 'i', 'e', 'i', 'a', 'e', 'a', 'e', 'e']

vowelRegex2 = re.compile(r'[aeiouAEIOU]{2}')
mo = vowelRegex2.findall(lyrics)
print(mo)

# ['ea', 'ie', 'ai', 'ee', 'ea', 'ee']

consonantsRegex = re.compile(r'[^aeiouAEIOU]')
mo = consonantsRegex.findall(lyrics)
print(mo)

# ['1', '2', ' ', 'd', 'r', 'm', 'm', 'r', 's', ' ', 'd', 'r', 'm', 'm', 'n', 'g', ',', ' ', '1', '1', ' ', 'p', 'p', 'r', 's', ' ', 'p', 'p', 'n', 'g', ',', ' ', '1', '0', ' ', 'l', 'r', 'd', 's', ' ', ' ', 'l', 'p', 'n', 'g', ',', '\n', '9', ' ', 'l', 'd', 's', ' ', 'd', 'n', 'c', 'n', 'g', ',', ' ', '8', ' ', 'm', 'd', 's', ' ', ' ', 'm', 'l', 'k', 'n', 'g', ',', ' ', '7', ' ', 's', 'w', 'n', 's', ' ', ' ', 's', 'w', 'm', 'm', 'n', 'g', ',', '\n', '6', ' ', 'g', 's', ' ', ' ', 'l', 'y', 'n', 'g', ',', ' ', '5', ' ', 'g', 'l', 'd', 'n', ' ', 'r', 'n', 'g', 's', ',', ' ', '4', ' ', 'c', 'l', 'l', 'n', 'g', ' ', 'b', 'r', 'd', 's', ',', ' ', '3', ' ', 'f', 'r', 'n', 'c', 'h', ' ', 'h', 'n', 's', ',', '\n', '2', ' ', 't', 'r', 't', 'l', ' ', 'd', 'v', 's', ',', ' ', '1', ' ', 'p', 'r', 't', 'r', 'd', 'g', ' ', 'n', ' ', ' ', 'p', 'r', ' ', 't', 'r']