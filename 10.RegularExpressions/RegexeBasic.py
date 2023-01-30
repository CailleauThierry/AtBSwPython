#! python3

import re
message = 'Call me at 415-555-1011 tomorrow or at 415-555-9999 the day after'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo)
print(mo.group())

mo = phoneNumRegex.findall(message)
print(mo)


