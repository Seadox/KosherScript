import unittest

import sys
import os

root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if root_folder not in sys.path:
    sys.path.insert(0, root_folder)


class TestLexer(unittest.TestCase):
    def test_empty(self):
        tokens = list(Lexer("").create_tokens())
        print(f"tokens: {tokens}")
        self.assertEqual(tokens, [Token("EOF")])

    def test_emprt(self):
        tokens = list(Lexer("\t\t\t\n\n\n   \n\t \n \t").create_tokens())
        self.assertEqual(tokens, [Token("NEWLINE"), Token("NEWLINE"), Token(
            "NEWLINE"), Token("NEWLINE"), Token("NEWLINE"), Token("EOF")])

    def test_numbers(self):
        tokens = list(Lexer("123 456.323 789. .232 .").create_tokens())
        self.assertEqual(tokens, [Token("INTEGER", 123), Token("FLOAT", 456.323), Token(
            "FLOAT", 789.0), Token("FLOAT", 0.232), Token("FLOAT", 0.0), Token("EOF")])

    def test_operators(self):
        tokens = list(Lexer("+ - * / = < >").create_tokens())
        self.assertEqual(tokens, [Token("PLUS"), Token("MINUS"), Token("MUL"), Token(
            "DIV"), Token("ASSIGNMENT"), Token("LT"), Token("GT"), Token("EOF")])

    def test_parentheses(self):
        tokens = list(Lexer("()").create_tokens())
        self.assertEqual(
            tokens, [Token("LPAREN"), Token("RPAREN"), Token("EOF")])

    def test_all(self):
        tokens = list(
            Lexer("123 + 456 - 789 * 0. / .1").create_tokens())
        self.assertEqual(tokens, [Token("INTEGER", 123), Token("PLUS"), Token("INTEGER", 456), Token("MINUS"), Token(
            "INTEGER", 789), Token("MUL"), Token("FLOAT", 0.0), Token("DIV"), Token("FLOAT", 0.1), Token("EOF")])

    def test_lexer_with_assignment_and_equality(self):
        lexer = Lexer("= ==")
        tokens = lexer.create_tokens()
        expected_tokens = [
            Token("ASSIGNMENT"), Token("EQ"), Token("EOF")
        ]
        self.assertEqual(tokens, expected_tokens)

    def test_lexer_with_identifiers_and_keywords(self):
        lexer = Lexer("אם אחרת בזמן")
        tokens = lexer.create_tokens()
        expected_tokens = [
            Token("KEYWORD", 'אם'),
            Token("KEYWORD", 'אחרת'),
            Token("KEYWORD", 'בזמן'),
            Token("EOF")
        ]
        self.assertEqual(tokens, expected_tokens)


if __name__ == "__main__":
    from src.Lexer import Lexer
    from src.Token import Token
    unittest.main()
