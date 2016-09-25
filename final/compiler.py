
INT, TOP, CIK, CARP, BOL, LPA, RPA, END = ('INT', 'TOP', 'CIK', 'CARP', 'BOL', '(', ')', 'END')


class Tok(object):
    def __init__(self, type, deger):
        self.type = type
        self.deger = deger

    def __str__(self):       
        return 'Tok({type}, {deger})'.format(type=self.type,deger=repr(self.deger))

    def __repr__(self):
        return self.__str__()


class Lexer(object):
    def __init__(self, metin):
        self.metin = metin
        self.pos = 0
        self.currentchar = self.metin[self.pos]

    def error(self):
        raise Exception('gecersiz karakter girdiniz!')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.metin) - 1:
            self.currentchar = None  
        else:
            self.currentchar = self.metin[self.pos]

    

    def INT(self):
        
        result = ''
        while self.currentchar is not None and self.currentchar.isdigit():
            result += self.currentchar
            self.advance()
        return int(result)

    def nexttoken(self):
        
        while self.currentchar is not None:

            if self.currentchar.isdigit():
                return Tok(INT, self.INT())

            if self.currentchar == '+':
                self.advance()
                return Tok(TOP, '+')

            if self.currentchar == '-':
                self.advance()
                return Tok(CIK, '-')

            if self.currentchar == '*':
                self.advance()
                return Tok(CARP, '*')

            if self.currentchar == '/':
                self.advance()
                return Tok(BOL, '/')

            if self.currentchar == '(':
                self.advance()
                return Tok(LPA, '(')

            if self.currentchar == ')':
                self.advance()
                return Tok(RPA, ')')

            self.error()

        return Tok(END, None)



class AST(object):
    pass


class instructions(AST):
    def __init__(self, sol, orta, sag):
        self.sol = sol
        self.token = self.orta = orta
        self.sag = sag


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.deger = token.deger


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.currenttok = self.lexer.nexttoken()

    def error(self):
        raise Exception('syntax hatasi!!')

    def comparison(self, toktype):
        if self.currenttok.type == toktype:
            self.currenttok = self.lexer.nexttoken()
        else:
            self.error()

    def factor(self):
        token = self.currenttok
        if token.type == INT:
            self.comparison(INT)
            return Num(token)
        elif token.type == LPA:
            self.comparison(LPA)
            node = self.expr()
            self.comparison(RPA)
            return node

    def term(self):
        node = self.factor()

        while self.currenttok.type in (CARP, BOL):
            token = self.currenttok
            if token.type == CARP:
                self.comparison(CARP)
            elif token.type == BOL:
                self.comparison(BOL)

            node = instructions(sol=node, orta=token, sag=self.factor())

        return node

    def expr(self):
        node = self.term()

        while self.currenttok.type in (TOP, CIK):
            token = self.currenttok
            if token.type == TOP:
                self.comparison(TOP)
            elif token.type == CIK:
                self.comparison(CIK)

            node = instructions(sol=node, orta=token, sag=self.term())

        return node

    def parse(self):
        node = self.expr()
        if self.currenttok.type != END:
            self.error()
        return node



class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        msfr = getattr(self, method_name, self.genvis)
        return msfr(node)

    def genvis(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_instructions(self, node):
        if node.orta.type == TOP:
            return self.visit(node.sol) + self.visit(node.sag)
        elif node.orta.type == CIK:
            return self.visit(node.sol) - self.visit(node.sag)
        elif node.orta.type == CARP:
            return self.visit(node.sol) * self.visit(node.sag)
        elif node.orta.type == BOL:
            return self.visit(node.sol) / self.visit(node.sag)

    def visit_Num(self, node):
        return node.deger

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)


def main():
    while True:
        try:
            try:
                text = raw_input('buraya komut girin> ')
            except NameError:
                text = input('buraya komut girin> ')
        except EOFError:
            break
        if not text:
            continue

        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        print(result)


if __name__ == '__main__':
    main()
