#! python3

import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

print(phoneRegex)

# PS C:\Users\tcailleau\Documents\Python\AtBSwPython> python 
# Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> exit()
# PS C:\Users\tcailleau\Documents\Python\AtBSwPython> py
# Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import re
# >>> beginsWithHello = re.compile(r'^Hello, my name is Thierry!') 
# >>> beginsWithHello = re.compile(r'^Hello')                      
# >>> print(beginsWithHello) 
# re.compile('^Hello')
# >>> beginsWithHello.search('Hello there! My name is Thierry!')
# <re.Match object; span=(0, 5), match='Hello'>
# >>> 

