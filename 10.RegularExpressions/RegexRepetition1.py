#! python3

import re

phoneRegex = re.compile(r'(\(\d\d\d\))? (\d\d\d-\d\d\d\d)')

mo = phoneRegex.search('This is my number 147-1234 if you want my other number it is (080) 147-4321 ')
print(mo)
print(mo.group())
mobj = phoneRegex.findall('This is my number 147-1234 if you want my other number it is (080) 147-4321 ')
print(mobj)

# PS C:\Users\tcailleau\Documents\Python\AtBSwPython> & C:/tools/Anaconda3/python.exe c:/Users/tcailleau/Documents/Python/AtBSwPython/10.RegularExpressions/RegexRepetition1.py
# <re.Match object; span=(17, 26), match=' 147-1234'>
#  147-1234
# [('', '147-1234'), ('(080)', '147-4321')]

batRegex = re.compile(r'Bat(wo)*man') # equivalent to (Batman|Batwoman)
mo = batRegex.search('The Adventures of Batman')
print(mo)
print(mo.group())

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

# PS C:\Users\tcailleau\Documents\Python\AtBSwPython> & C:/tools/Anaconda3/python.exe c:/Users/tcailleau/Documents/Python/AtBSwPython/10.RegularExpressions/RegexRepetition.py
# <re.Match object; span=(18, 24), match='Batman'>
# Batman
# Batwoman

mo = batRegex.search('The Adventures of Batwowowoman')
print(mo)

# PS C:\Users\tcailleau\Documents\Python\AtBSwPython> & C:/tools/Anaconda3/python.exe c:/Users/tcailleau/Documents/Python/AtBSwPython/10.RegularExpressions/RegexRepetition1.py
# <re.Match object; span=(17, 26), match=' 147-1234'>
#  147-1234
# [('', '147-1234'), ('(080)', '147-4321')]
# <re.Match object; span=(18, 24), match='Batman'>
# Batman
# Batwoman
# <re.Match object; span=(18, 30), match='Batwowowoman'>
# PS C:\Users\tcailleau\Documents\Python\AtBSwPython> 

batRegex1 = re.compile(r'Bat(wo)+man') 
mo = batRegex1.search('The Adventures of Batman')
print(mo)
mo = batRegex1.search('The Adventures of Batwoman')
print(mo)
mo = batRegex1.search('The Adventures of Batwowowowoman')
print(mo)

#[...]
# None
# <re.Match object; span=(18, 26), match='Batwoman'>
# <re.Match object; span=(18, 32), match='Batwowowowoman'>
# PS C:\Users\tcailleau\Documents\Python\AtBSwPython> 


haRegex = re.compile(r'(Ha){3}') 
mo = haRegex.search('Ha')
print(mo)
mo = haRegex.search('HaHaHa')
print(mo)

#[...]
# None
# <re.Match object; span=(0, 6), match='HaHaHa'>

haRegex = re.compile(r'(Ha){3,5}') 
mo = haRegex.search('Ha')
print(mo)
mo = haRegex.search('He said HaHaHa')
print(mo)
mo = haRegex.search('Then he said HaHaHaHaHa')
print(mo)


digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('123456789')
print(mo)

# <re.Match object; span=(0, 5), match='12345'>  # return 5  number instead of 3 as by default Regex is set to "greedy" match

digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('123456789')
print(mo)

# <re.Match object; span=(0, 3), match='123'>  # "?" after a "section" does not mean 0 or 1 time, it means non-greedy


