pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = "original()"
    first = original[0]
    if first == 'a' or first == "e" or first == 'i' or first == 'o' or first == 'u':
        co_word = original + pyg
        print co_word
    else:
        new_word = original[1:] + original[0] + pyg
        print new_word
else:
    print 'empty'