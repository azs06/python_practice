import re

validNumber = re.compile(r'^(\d{1,3}(,\d{3})*)?$')

test1 = validNumber.search('1,234')
print(test1)
test2 = validNumber.search('1,234,567')
print(test2)