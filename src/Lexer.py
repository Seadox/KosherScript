from .Token import *


class Lexer:
    def __init__(self, text) -> None:
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self) -> None:
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(
            self.text) else None

    def create_tokens(self) -> list[Token]:
        tokens = []
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in "\n;":
                tokens.append(Token(NEWLINE))
                self.advance()
            elif self.current_char in DIGITS or self.current_char == '.':
                tokens.append(self.number())
            elif self.current_char in LETTERS:
                tokens.append(self.identifier())
            elif self.current_char == '+':
                tokens.append(Token(PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(RPAREN))
                self.advance()
            elif self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    tokens.append(Token(EQ))
                elif self.current_char == '>':
                    self.advance()
                    tokens.append(Token(GREATER_THAN_EQ))
                elif self.current_char == '<':
                    self.advance()
                    tokens.append(Token(LESS_THAN_EQ))
                else:
                    tokens.append(Token(ASSIGNMENT))
            elif self.current_char == '<':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    tokens.append(Token(LESS_THAN_EQ))
                else:
                    tokens.append(Token(LESS_THAN))
            elif self.current_char == '>':
                self.advance()

                if self.current_char == '=':
                    self.advance()
                    tokens.append(Token(GREATER_THAN_EQ))
                else:
                    tokens.append(Token(GREATER_THAN))
            else:
                print(f"Invalid character '{self.current_char}'")
                return []

        tokens.append(Token(EOF))
        return tokens

    def number(self) -> Token:
        num_str = ''
        dot_count = 0
        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if num_str.startswith('.'):
            num_str = '0' + num_str

        if num_str.endswith('.'):
            num_str += '0'

        if dot_count == 0:
            return Token(INT, int(num_str))
        else:
            return Token(FLOAT, float(num_str))

    def identifier(self):
        id_str = ''
        while self.current_char != None and self.current_char in LETTERS + DIGITS + '_':
            id_str += self.current_char
            self.advance()
        token_type = KEYWORD if id_str in KEYWORDS else IDENTIFIER

        if len(id_str) > IDENTIFIER_LEN:
            print(
                f"Variable '{id_str}' is too long. Make sure it is less than {IDENTIFIER_LEN} characters long.")
            return Token(EOF)

        return Token(token_type, id_str)
