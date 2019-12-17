#variant 5

import re

array = []
line = input()
array.append(line)
while line != "0":
    line = input()
    array.append(line)

for x in array:
    match = re.search(r'\s\bcat', x)
    if match != None:
        print(x)
