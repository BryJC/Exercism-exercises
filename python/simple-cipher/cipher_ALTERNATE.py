from string import Formatter as f
from string import index

class Caesar(object):
    
    def __init__(self):
        pass
        
    @classmethod
    def encode(text):
        n = 0
        new = ''
        while True:
            x = f().get_value(n, text, None)
            y = index(string.ascii_lowercase, x)
            z = f().get_value(y+4, string.ascii_lowercase, None)
            new += z
            n += 1
            if n == len(text):
                break
        return new
        
    @classmethod
    def decode(text):
        pass

class Cipher(object):
    
    def __init__(self, key):
        self.key = key
        pass
        
    def encode(self, text):
        pass
        
    def decode(self, text):
        pass
