   
class Parser(object):
    def __init__(self,lexer):
        self.lexer = lexer
        self.currenttok = self.lexer.nexttoken()
        
    def error(self):
        raise Exception('error')
        
    def karsilastirma(self,tokentype):
        if self.currenttok.type == tokentype:
            self.currenttok = self.lexer.nexttoken()
        else:
            self.error()
            
    def factor(self):
        token = self.currenttoken
        if token.type == INT:
            self.karsilastirma(INT)
            return Num(token)
        elif token.type == LPA:
            self.karsilastirma(LPA)
            node = self.expr()
            self.karsilastirma(RPA)
            return node
        
    def term(self):
        node = self.factor()
        
        while self.currenttoken.type in (CARP, BOL):
            if token.type == CARP:
                self.karsilastirma(CARP)
            elif token.type == BOL:
                self.karsilastirma(BOL)
            
    
    def expr(self):
        node = self.term()
        
        while self.currenttoken.type in (TOP, CIK):
            token = self.currenttoken
            if token.type == TOP:
                self.karsilastirma(TOP)
            elif token.type == CIKAR:
                self.karsilastirma(CIK)
                
            
    def parse(self):
        node = self.expr()
        if self.currenttoken.type != END:
            self.error()
        return node
