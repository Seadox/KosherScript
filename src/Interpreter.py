from .SymbolTable import SymbolTable
from .Parser import Parser
from .Token import *


class Interpreter:
    def __init__(self, parser: Parser, symbol_table: SymbolTable) -> None:
        self.parser = parser
        self.symbol_table = symbol_table

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)

    def visit(self, node):
        if node is None:
            return None

        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name, None)

        if method is None:
            print(f"No visit_{type(node).__name__} method")
        return method(node)

    def visit_BinaryOperationNode(self, node):
        left_value = self.visit(node.left)
        right_value = self.visit(node.right)

        if left_value is None or right_value is None:
            print("Invalid binary operation: One of the operands is None")

        if node.op.type == PLUS:
            return left_value + right_value
        elif node.op.type == MINUS:
            return left_value - right_value
        elif node.op.type == MUL:
            return left_value * right_value
        elif node.op.type == DIV:
            return left_value / right_value
        elif node.op.type == ASSIGNMENT:
            self.symbol_table.set(left_value, right_value)
            return right_value
        elif node.op.type == LESS_THAN:
            return left_value < right_value
        elif node.op.type == GREATER_THAN:
            return left_value > right_value
        elif node.op.type == LESS_THAN_EQ:
            return left_value <= right_value
        elif node.op.type == GREATER_THAN_EQ:
            return left_value >= right_value
        elif node.op.type == EQ:
            return left_value == right_value

    def visit_NumberNode(self, node):
        return node.value

    def visit_UnaryOperationNode(self, node):
        if node.operator.type == PLUS:
            return self.visit(node.node)
        elif node.operator.type == MINUS:
            return -self.visit(node.node)

    def visit_VariableAccessNode(self, node):
        return self.symbol_table.get(node.var_name)

    def visit_AssignmentNode(self, node):
        visited = self.visit(node.value)
        if visited is not None:
            self.symbol_table.set(node.var_name, visited)

    def visit_IfNode(self, node):
        condition = self.visit(node.condition)
        if condition:
            visited = self.visit(node.then_block)
            return visited
        elif node.else_block is not None:
            return self.visit(node.else_block)

    def visit_WhileNode(self, node):
        while self.visit(node.condition):
            self.visit(node.block)

            if node.condition == False:
                break

    def visit_BlockNode(self, node):
        for child in node.children:
            self.visit(child)

    def visit_MultiAssignmentNode(self, node):
        for var_name, value in node.assignments:
            self.symbol_table.set(var_name, self.visit(value))
        return None

    def visit_listNode(self, node):
        return [self.visit(child) for child in node.children]
