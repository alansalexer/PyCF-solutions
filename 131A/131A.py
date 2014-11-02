word=raw_input()
if len(word) == 1:
	if word[0].islower():
		print word[0].upper()
	else:
		print word[0].lower()
else:
	isMisTyped = True
	for i in xrange(1,len(word)):
		if word[i].islower():
			isMisTyped = False
			break
	if isMisTyped:
		if word[0].islower():
			print word.capitalize()
		else:
			print word.lower()
	else:
		print word
	