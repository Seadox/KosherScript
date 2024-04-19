from .Token import *
from .Nodes import *


class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.pos = -1
        self.current_token = None
        if len(tokens) > 0:
            self.advance()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        return self.current_token

    def parse(self):
        if len(self.tokens) == 0:
            return None
        expressions = []

        while self.current_token and self.current_token.type != EOF:
            expr = self.expr()
            if expr:
                expressions.append(expr)

            if self.current_token and self.current_token.type == NEWLINE:
                self.advance()
            else:
                break
        if not expressions:
            return None
        elif len(expressions) == 1:
            return expressions[0]
        else:
            return listNode(expressions)

    def parse_block(self):
        nodes = []
        while self.current_token and (self.current_token.type != KEYWORD or self.current_token.value not in (WORD_END, WORD_ELSE)):
            statement = self.expr()

            if statement:
                nodes.append(statement)

            if self.current_token and self.current_token.type == NEWLINE:
                self.advance()

        return BlockNode(nodes)

    def block(self):
        nodes = []
        while self.current_token and self.current_token.type != WORD_IF:
            node = self.expr()
            if node:
                nodes.append(node)
        return BlockNode(nodes)

    def expr(self):
        node = self.arithmetic_expr()

        while self.current_token and self.current_token.type in (LESS_THAN, GREATER_THAN, EQ, LESS_THAN_EQ, GREATER_THAN_EQ):
            op = self.current_token
            self.advance()
            right = self.arithmetic_expr()
            node = BinaryOperationNode(node, op, right)
        return node

    def arithmetic_expr(self):
        node = self.term()

        while self.current_token and self.current_token.type in (PLUS, MINUS):
            op = self.current_token
            self.advance()
            right = self.term()
            node = BinaryOperationNode(node, op, right)

        return node

    def term(self):
        node = self.factor()
        if not node or type(node) == UnaryOperationNode:
            if not node:
                return None
            return None

        while self.current_token and self.current_token.type in (MUL, DIV):
            op = self.current_token
            self.advance()
            right = self.factor()
            node = BinaryOperationNode(node, op, right)

        return node

    def if_expr(self):
        if self.current_token and self.current_token.type == KEYWORD and self.current_token.value == WORD_IF:
            self.advance()
            condition = self.expr()

            if self.current_token and self.current_token.type == KEYWORD and self.current_token.value == WORD_THEN:
                self.advance()
                then_block = self.parse_block()
                else_block = None

                if self.current_token and self.current_token.type == KEYWORD and self.current_token.value == WORD_ELSE:
                    self.advance()
                    else_block = self.parse_block()

                return IfNode(condition, then_block, else_block)

            print("Expected 'then'")
            return None

        return None

    def while_expr(self):
        if self.current_token and self.current_token.type == KEYWORD and self.current_token.value == WORD_WHILE:
            self.advance()
            condition = self.expr()

            if self.current_token and self.current_token.type == KEYWORD and self.current_token.value == WORD_THEN:
                self.advance()
                then_block = self.parse_block()

                if self.current_token and self.current_token.type == KEYWORD and self.current_token.value == WORD_END:
                    self.advance()
                    return WhileNode(condition, then_block)
                else:
                    print("Expected 'end' at the end of the 'while' loop")
                    return None
            else:
                print("Expected 'then' after the condition in the 'while' loop")
                return None
        return None

    def identifier_expr(self):
        var_name = self.current_token.value
        self.advance()
        if self.current_token and self.current_token.type == ASSIGNMENT:
            self.advance()
            assignments = [(var_name, self.expr())]

            while self.current_token and self.current_token.type == NEWLINE:
                self.advance()
                if self.current_token and self.current_token.type == IDENTIFIER:
                    var_name = self.current_token.value
                    self.advance()
                    if self.current_token and self.current_token.type == ASSIGNMENT:
                        self.advance()
                        assignments.append((var_name, self.expr()))

            return MultiAssignmentNode(assignments)

        return VariableAccessNode(var_name)

    def factor(self):
        token = self.current_token
        if token.type == NEWLINE:
            self.advance()
        elif token.type == INT:
            self.advance()
            return NumberNode(token.value)
        elif token.type == FLOAT:
            self.advance()
            return NumberNode(token.value)
        elif token.type == IDENTIFIER:
            return self.identifier_expr()
        elif token.type == LPAREN:
            self.advance()
            node = self.expr()
            if self.current_token and self.current_token.type != RPAREN:
                print("Expected ')'")
                return None
            self.advance()
            return node
        elif token.type in (PLUS, MINUS):
            next_token = self.tokens[self.pos +
                                     1] if self.pos + 1 < len(self.tokens) else None
            if token.type == MINUS and next_token and next_token.type in (INT, FLOAT):
                self.advance()
                self.advance()
                return NumberNode(-next_token.value)
            else:
                self.advance()
                return UnaryOperationNode(token, self.factor())
        elif token.type == KEYWORD:
            if token.value == WORD_IF:
                return self.if_expr()
            elif token.value == WORD_WHILE:
                return self.while_expr()
        else:
            if token.type != EOF:
                print(f"Unexpected token type: {token.type}")
            return None
