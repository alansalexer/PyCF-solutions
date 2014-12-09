# Problem - 112A - Codeforces
# Tags: strings
# http://codeforces.com/problemset/problem/112/A
s1=raw_input().lower()
s2=raw_input().lower()

if s1==s2:
	print 0
elif s1<s2:
	print -1
else:
	print 1