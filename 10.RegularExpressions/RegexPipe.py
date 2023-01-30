#! python3

import re
message = 'Call me at 415-555-1011 tomorrow or at 415-555-9999 the day after'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo)
print(mo.group())

mo = phoneNumRegex.findall(message)
print(mo)

phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex2.search(message)
print(mo.group())
print(mo.group(1))
print(mo.group(2))

# PS C:\Users\tcailleau\Documents\Python\AtBSwPython> & C:/tools/Anaconda3/python.exe c:/Users/tcailleau/Documents/Python/AtBSwPython/10.RegularExpressions/RegexPipe.py  
# <re.Match object; span=(11, 23), match='415-555-1011'>
# 415-555-1011
# ['415-555-1011', '415-555-9999']
# 415-555-1011
# 415
# 555-1011 


message2 = 'Call me at (415) 555-1011 tomorrow or at (415) 555-9999 the day after'
phoneNumRegex2 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumRegex2.search(message2)
print(mo)
print(mo.group())

mo = phoneNumRegex2.findall(message2)
print(mo)


message3 = 'The Batmobile lost a wheel'
phoneNumRegex3 = re.compile(r'Bat(man|mobile|copter|bat)')
mobj = phoneNumRegex3.search(message3)
print(mobj)
print(mobj.group())

# PS C:\Users\tcailleau\Documents\Python\AtBSwPython> & C:/tools/Anaconda3/python.exe c:/Users/tcailleau/Documents/Python/AtBSwPython/10.RegularExpressions/RegexPipe.py
# <re.Match object; span=(11, 23), match='415-555-1011'>
# 415-555-1011
# ['415-555-1011', '415-555-9999']
# 415-555-1011
# 415
# 555-1011
# <re.Match object; span=(11, 25), match='(415) 555-1011'>
# (415) 555-1011
# ['(415) 555-1011', '(415) 555-9999']
# <re.Match object; span=(4, 13), match='Batmobile'>
# Batmobile

