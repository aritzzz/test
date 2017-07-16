import re
for i in range(input()):
    print bool(re.match(r'[+-.]?\d+[.]{1}\d+', raw_input()))
    



