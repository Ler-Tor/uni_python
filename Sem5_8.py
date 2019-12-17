#variant 4
import re
array = []
line = input()
array.append(line)
while line != "0":
    line = input()
    array.append(line)
    match = re.findall(r'\b\d+[.,]\d+', line)
    print(match)
