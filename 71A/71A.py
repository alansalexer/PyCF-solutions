# Problem - 71A - Codeforces
# Tags: strings
# http://codeforces.com/problemset/problem/71/A
for i in range(input()):
	s=raw_input()
	if len(s)>10:
		s=s[0]+str(len(s)-2)+s[-1]
	print s
