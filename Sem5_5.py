#variant 4
import re
p = re.compile(r'^(\b(\w)+\b).*\1.*', re.M)
array = []
line = input()
array.append(line)
while line != "0":
    line = input()
    array.append(line)

for x in array:
    count = 0
    match = re.search(p, x)
    if match != None:
        print(x)
