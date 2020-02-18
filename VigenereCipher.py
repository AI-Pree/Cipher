class VigenereCipher(object):
    def __init__(self,key,alphabet):
        self.key = key
        self.alphabet = alphabet
        
    def encode(self,text):
        l = ""
        for i, a in enumerate(text):
            if a in self.alphabet:
                im = i % len(self.key) if i >= len(self.key) else i
                m = self.alphabet.index(self.key[im]) + self.alphabet.index(a)
                m = m  - len(self.alphabet) if m > len(self.alphabet)-1 else m
                l += self.alphabet[m]
            else:
                l += a
        return l
        
    def decode(self,text):
        d = ""
        for i, a  in enumerate(text):
            if a in self.alphabet:
                im = i % len(self.key) if i >= len(self.key) else i
                m = self.alphabet.index(a)-self.alphabet.index(self.key[im])
                print("my",self.alphabet.index(self.key[im]))
                m = len(self.alphabet)+m if m < 0 else m
                d += self.alphabet[m]
            else:
                d += a
        return d