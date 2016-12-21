import re

emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+
                        @
                        [a-zA-Z0-9.-]+
                        (\.[a-zA-Z]{2,4})
                        )''', re.VERBOSE)

checkEmail = emailRegex.search('')

threeNumComa = re.compile(r'{/d},{/d/d}|{/d/d/d}+,{/d/d/d}')
tnum = threeNumComa.search('1,234')
print(tnum)
