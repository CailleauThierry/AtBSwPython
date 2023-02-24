#! python3

import re

batRegex = re.compile(r'Bat(wo)?man') # equivalent to (Batman|Batwoman)
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

# PS C:\Users\tcailleau\Documents\Python\AtBSwPython> & C:/tools/Anaconda3/python.exe c:/Users/tcailleau/Documents/Python/AtBSwPython/10.RegularExpressions/RegexRepetition.py
# <re.Match object; span=(18, 24), match='Batman'>
# Batman
# Batwoman
# None
# Traceback (most recent call last):
#   File "c:/Users/tcailleau/Documents/Python/AtBSwPython/10.RegularExpressions/RegexRepetition.py", line 20, in <module>
#     print(mo.group())
# AttributeError: 'NoneType' object has no attribute 'group'
# PS C:\Users\tcailleau\Documents\Python\AtBSwPython> 

phoneRegex = re.compile(r'(\(\d\d\d\))? \d\d\d-\d\d\d\d')
# "
# (\(\d\d\d\))? \d\d\d-\d\d\d\d
# "
# gm
# 1st Capturing Group (\(\d\d\d\))?
# ? matches the previous token between zero and one times, as many times as possible, giving back as needed (greedy)
# \( matches the character ( with index 4010 (2816 or 508) literally (case sensitive)
# \d matches a digit (equivalent to [0-9])
# \d matches a digit (equivalent to [0-9])
# \d matches a digit (equivalent to [0-9])
# \) matches the character ) with index 4110 (2916 or 518) literally (case sensitive)
#   matches the character   with index 3210 (2016 or 408) literally (case sensitive)
# \d matches a digit (equivalent to [0-9])
# \d matches a digit (equivalent to [0-9])
# \d matches a digit (equivalent to [0-9])
# - matches the character - with index 4510 (2D16 or 558) literally (case sensitive)
# \d matches a digit (equivalent to [0-9])
# \d matches a digit (equivalent to [0-9])
# \d matches a digit (equivalent to [0-9])
# \d matches a digit (equivalent to [0-9])
# Global pattern flags 
# g modifier: global. All matches (don't return after first match)
# m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)
# ----------------------------------------------
# match,group,is_participating,start,end,content
# 1,0,yes,17,26, 147-1234
# 2,0,yes,61,75,(080) 147-4321
# 2,1,yes,61,66,(080)
# from<https://regex101.com/>

mo = phoneRegex.search('This is my number 147-1234 if you want my other number it is (080) 147-4321')
print(mo)
print(mo.group())
mo = phoneRegex.findall('This is my number 147-1234 if you want my other number it is (080) 147-4321')
print(mo)

# PS C:\Users\tcailleau\Documents\Python\AtBSwPython> & C:/tools/Anaconda3/python.exe c:/Users/tcailleau/Documents/Python/AtBSwPython/10.RegularExpressions/RegexRepetition.py
# <re.Match object; span=(18, 24), match='Batman'>
# Batman
# Batwoman
# None
# <re.Match object; span=(17, 26), match=' 147-1234'>
#  147-1234
# ['', '(080)']