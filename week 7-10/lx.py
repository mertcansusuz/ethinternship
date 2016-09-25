INT, TOP, CIK, CARP, BOL, LPA, RPA, END = ('INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', '(', ')', 'EOF')


class tok(object):
    def __init__(self, type, deger):
        self.type = type
        self.deger = deger
    
class LexicalAnalyzer(object):
    def __init__(self, metin):
        self.metin = metin
        self.pos = 0
        self.currentchar = self.metin[self.pos]
        
    def error(self):
        raise Exception("error")
    
    def advance(self):
        self.pos +=1
        if self.pos > len(self.metin) - 1:
            self.currentchar = None
        else:
            self.currentchar = self.metin[self.pos]
        
    def integer(self):
        result = ''
        while self.currentchar is not None and self.currentchar.isdigit():
            result += self.currentchar
            self.advance
        return int(result)
    
    def nexttoken(self):
        while self.currentchar is not None:
            if self.currentchar.isdigit():
                return tok(INT,self.integer())
            
            if self.currentchar == '+':
                self.advance()
                return tok(TOP, '+')

            if self.currentchar == '-':
                self.advance()
                return Token(CIK, '-')
 
            if self.currentchar == '*':
                self.advance()
                return Token(CARP, '*')

            if self.currentchar == '/':
                self.advance()
                return Token(BOL, '/')

            if self.currentchar == '(':
                self.advance()
                return Token(LPA, '(')

            if self.currentchar == ')':
                self.advance()
                return Token(RPA, ')')
            self.error()
            
        return tok(END,None)
