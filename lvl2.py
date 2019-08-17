import re
str = open("text2.txt").read()
print ("".join([char for char in str if char.isalpha()]))