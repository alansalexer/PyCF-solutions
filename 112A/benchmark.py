import re, string, timeit

s1='aaaa'
s2='aaab'

def cmp_set(s1,s2):
    return cmp(s1,s2)

def cmp_plain_set(s1,s2):
	if s1 > s2:
		return 1
	elif s1 == s2:
		return 0
	else:
		return -1

def star_unpack_set(s1,s2):
    return cmp(*[s1,s2])

print "cmp      :",timeit.Timer('f(s1,s2)', 'from __main__ import s1,s2,cmp_set as f').timeit(1000000)
print "cmp_plain      :",timeit.Timer('f(s1,s2)', 'from __main__ import s1,s2,cmp_plain_set as f').timeit(1000000)
print "star_unpack :",timeit.Timer('f(s1,s2)', 'from __main__ import s1,s2,star_unpack_set as f').timeit(1000000)