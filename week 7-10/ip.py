class NodeVisitor(object):
    def visit(self,node):
        methodname = 'visit_' + type(node).__name__
        visitor = getattr(self,methodname, self.genvis)
        return visitor(node)
    
    """def genvis(self,node):
        raise Exception('No visit_{} method'.format(type(node).__name__))"""
        
        
class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        if node.op.type == TOP:
            return self.visit(node.sol) + self.visit(node.sag)
        elif node.op.type == CIK:
            return self.visit(node.sol) - self.visit(node.sag)
        elif node.op.type == CARP:
            return self.visit(node.sol) * self.visit(node.sag)
        elif node.op.type == BOL:
            return self.visit(node.sol) / self.visit(node.sag)

    def visit_Num(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)
