def letterToIndex (ch):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    idx = alphabet.find(ch)
    if idx<0:
        print ("error:letter not in the alphabet",ch)
    return idx
def indexToLetter (idx):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if idx>25:
        print('error:', idx, ' is too large')
        letter = ' '
        else:
            letter = alphabet[idx]
            return letter
