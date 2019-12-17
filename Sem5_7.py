#variant 4
import re
array = []
line = input()
array.append(line)
while line != "0":
    line = input()
    array.append(line)

for x in array:
    match = re.sub(r'(\w)\1+', r'\1', x)
    print(match)
