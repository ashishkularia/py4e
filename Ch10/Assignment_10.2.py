# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith("From"):
        count = line.split()
        if len(count) is 7:
            hr = count[5].split(":")
            counts[hr[0]] = counts.get(hr[0], 0) + 1

lst = sorted([(x,y) for x,y in counts.items()])
for a,b in lst:
    print(a, b)
