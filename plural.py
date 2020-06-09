# converts words to its plural form
def pluralPlus(w):
	if w.endswith('s'):
		return w+'es'               #if it ends with s, add es
	elif w.endswith('h'):
		return w+'es'               #if it ends with h, add es
	elif w.endswith('y'):
		return w.replace('y','ies')    #if ends with y, replace with ies
	else:
		return w+'s'                #if anything else, add s

'''
Test Case:
>>> pluralPlus('pony')
'ponies'
>>> pluralPlus('nerd')
'nerds'
>>> pluralPlus('fish')
'fishes'
>>> pluralPlus('kiss')
'kisses'
>>> pluralPlus('pony')
'ponies'
'''
