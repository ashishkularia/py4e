import re

fh = open("regex_sum_866611.txt")
sum = 0
for x in fh:
    x = x.rstrip()
    num = re.findall('[0-9]+',x)
    for i in num:
        sum = sum + int(i)
print(sum)