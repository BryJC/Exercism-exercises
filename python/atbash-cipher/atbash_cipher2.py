from string import ascii_lowercase, maketrans, translate
import re, string; pattern = re.compile('[\W_]+')

switch = maketrans(ascii_lowercase, ascii_lowercase[::-1])

def encode(phrase):
    x = translate(pattern.sub('', phrase), switch)
    return ' '.join(x[i:i+5] for i in range(0, len(x), 5))
    
def decode(phrase):
    x = translate(pattern.sub('', phrase), switch)
