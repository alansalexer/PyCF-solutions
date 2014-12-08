# Problem - 131A - Codeforces
# Tags: strings
# http://codeforces.com/problemset/problem/131/A
word=raw_input()
print word.swapcase() if word[1:].isupper() or len(word) == 1 else word
