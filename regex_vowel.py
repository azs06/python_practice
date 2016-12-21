import re

vowelRegex = re.compile(r'[aeiouAEIOU]')

robocop = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')

print(robocop)