INT = 'INTEGER'  # 'INTEGER' is 'INT'
FLOAT = 'FLOAT'  # 'FLOAT' is 'DECIMAL'
IDENTIFIER = 'IDENTIFIER'  # 'IDENTIFIER' is 'VAR'
KEYWORD = 'KEYWORD'  # 'KEYWORD' is 'VAR'
ASSIGNMENT = 'ASSIGNMENT'  # 'ASSIGNMENT'
PLUS = 'PLUS'  # 'PLUS' is 'ADD'
MINUS = 'MINUS'  # 'MINUS' is 'SUBTRACT'
MUL = 'MUL'  # 'MUL' is 'MULTIPLY'
DIV = 'DIV'  # 'DIV' is 'DIVIDE'
EQ = 'EQ'  # 'EQ' is 'EQUALS'
LESS_THAN = 'LT'  # 'LT' is 'LESS_THAN'
GREATER_THAN = 'GT'  # 'GT' is 'GREATER_THAN
GREATER_THAN_EQ = 'GTE'  # 'GTE' is 'GREATER_THAN_EQ'
LESS_THAN_EQ = 'LTE'  # 'LTE' is 'LESS_THAN_EQ'
LPAREN = 'LPAREN'  # 'LPAREN' is 'OPEN_PAREN'
RPAREN = 'RPAREN'   # 'RPAREN' is 'CLOSE_PAREN'
NEWLINE = 'NEWLINE'  # 'NEWLINE' is 'NEWLINE
EOF = 'EOF'  # 'EOF' is 'END OF FILE'

WORD_IF = 'אם'
WORD_ELSE = 'אחרת'
WORD_THEN = 'אזי'
WORD_WHILE = 'בזמן'
WORD_END = 'סוף'

KEYWORDS = [
    WORD_IF,
    WORD_ELSE,
    WORD_THEN,
    WORD_WHILE,
    WORD_END
]

IDENTIFIER_LEN = 11

DIGITS = '0123456789'
LETTERS = 'אבגדהוזחטיכלמנסעפצקרשתןםךףץ'


class Token:
    def __init__(self, _type, value=None) -> None:
        self.type = _type
        self.value = value

    def matches(self, _type, value):
        return self.type == _type and self.value == value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Token):
            return False
        return self.type == other.type and self.value == other.value

    def __repr__(self) -> str:
        return self.type + (f": {self.value}" if self.value != None else "")
