#variant 4
import re
array = []
line = input()
array.append(line)
while line != "0":
    line = input()
    array.append(line)
for x in array:
    match = re.search(r'\b(19|[2-9][0-9]|10[0-5])', x)
    if match != None:
        print(x)
