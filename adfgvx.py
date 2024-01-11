from random import shuffle, choice
from itertools import product, accumulate

class ADFGVX:
  """ The WWI German ADFGVX cipher. """
  def __init__(self, spoly, k, alph='QWERTYUIOPASDFGHJKLZXCVBNM'):
   self.polybius = list(spoly.upper())
   self.pdim = int(len(self.polybius) ** 0.5)
   self.key = list(k.upper())
   self.keylen = len(self.key)
   self.alphabet = list(alph)
  # self.alphabet = list(alph + ('V') + ('W') + ('M') + ('T') + ('D') + ('F') + ('G') + ('H') + ('J') + ('K') + ('Z') + ('X') + ('C') + ('N'))
   pairs = [p[0] + p[1] for p in product(self.alphabet, self.alphabet)]
   self.encode = {**dict.fromkeys(self.polybius, None), **dict(zip(self.polybius, pairs))}
   self.decode = dict((v, k) for (k, v) in self.encode.items())

  def encrypt(self, msg):
      """ Encrypt with the ADFGVX cipher. """
      chars = list(''.join([self.encode[c] for c in msg.upper() if c in self.polybius or c == ' ']))
      colvecs = [(lett, chars[i:len(chars):self.keylen]) \
          for (i, lett) in enumerate(self.key)]
      colvecs.sort(key=lambda x: x[0])
      return ''.join([''.join(a[1]) for a in colvecs])

  def decrypt(self, cod):
   """ Decrypt with the ADFGVX cipher. Does not depend on spacing of encoded text """
   chars = [c for c in cod if c in self.alphabet or c == ' ']
   sortedkey = sorted(self.key)
   order = [self.key.index(ch) for ch in sortedkey]
   originalorder = [sortedkey.index(ch) for ch in self.key]
   base, extra = divmod(len(chars), self.keylen)
   strides = [base + (1 if extra > i else 0) for i in order] # shuffled column lengths
   starts = list(accumulate(strides[:-1], lambda x, y: x + y)) # shuffled starts of columns
   starts = [0] + starts                             # starting index
   ends = [starts[i] + strides[i] for i in range(self.keylen)] # shuffled ends of columns
   cols = [chars[starts[i]:ends[i]] for i in originalorder] # get reordered columns
   pairs = []                                      # recover the rows
   for i in range((len(chars) - 1) // self.keylen + 1):
    for j in range(self.keylen):
       if i * self.keylen + j < len(chars):
           pairs.append(cols[j][i])

   return ''.join([self.decode[pairs[i] + pairs[i + 1]] for i in range(0, len(pairs), 2) if pairs[i] + pairs[i + 1] in self.decode])
