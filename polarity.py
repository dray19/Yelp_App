import pandas as pd
import numpy as np

def ngrams(input, n):
    input = input.split(' ')
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output


class zack_pol:

    def __init__(self,text, lex2):
        self.text = text
        self.lex2 = lex2

    def score(self):
        tt = str(self.text)
        splt = tt.split()
        score = []
        for word in splt:
            if self.lex2.get(word) != None:
                    val = self.lex2.get(word)
                    score.append(val)
            else:
                pass
        gram_2 = [' '.join(x) for x in ngrams(tt, 2)]
        for word2 in gram_2:
            if self.lex2.get(word2) != None:
                    val = self.lex2.get(word2)
                    score.append(val)
            else:
                pass
        gram_3 = [' '.join(x) for x in ngrams(tt, 3)]
        for word3 in gram_3:
            if self.lex2.get(word3) != None:
                    val = self.lex2.get(word3)
                    score.append(val)
            else:
                pass
        if score == []:
            z = 0
            return(z)
        else:
            sc = np.mean(score)
            return(sc)
