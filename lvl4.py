from urllib.request import urlopen
import re
k = 85		
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
#num = "12345"
num = str(16044/2)

pat = re.compile("and the next nothing is (\d+)")

while True:
	content = urlopen(url % num).read().decode('utf-8')
	print(content)
	match = pat.search(content)
	if match == None:
		break
	num = match.group(1)
	k += 1
	print(k)