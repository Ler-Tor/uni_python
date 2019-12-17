#variant 4
import re
array = []
line = input()
array.append(line)
while line != "0":
    line = input()
    array.append(line)

for x in array:
    match = re.sub(r'([^*].*)(\*\*)([^*].*)', r'\1!\3', x)
    print(match)
