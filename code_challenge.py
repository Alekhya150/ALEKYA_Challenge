# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

for _ in range(int(input())):
    if re.search(r'^(?!.*(\d)(-?\1){3})([4-6][\d]{3})(\-?[\d]{4}){3}$', input().strip()):
        print('Valid')
    else:
        print('Invalid')