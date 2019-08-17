import re
str = open("text3.txt").read()
print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", str)))