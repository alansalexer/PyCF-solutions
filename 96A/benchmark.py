import re, string, timeit

s = "1000011101111111100"

def fixed_str_set(s):
    return 'YES' if '0000000' in s or '1111111' in s else 'NO'

def changeable_str_set(s):
    return 'YES' if '0'*7 in s or '1'*7 in s else 'NO'

def tricky_str_set(s):
    return ['NO','YES']['0'*7 in s or '1'*7 in s]

print "fixed      :",timeit.Timer('f(s)', 'from __main__ import s,fixed_str_set as f').timeit(1000000)
print "changeable     :",timeit.Timer('f(s)', 'from __main__ import s,changeable_str_set as f').timeit(1000000)
print "tricky :",timeit.Timer('f(s)', 'from __main__ import s,tricky_str_set as f').timeit(1000000)