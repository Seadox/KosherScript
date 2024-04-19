import unittest


import sys
import os

root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if root_folder not in sys.path:
    sys.path.insert(0, root_folder)


class TestInterpreter(unittest.TestCase):

    def setUp(self):
        self.symbol_table = SymbolTable()

    def test_simple_calc(self):
        parser = Parser([Token("INTEGER", 2), Token("PLUS"),
                        Token("INTEGER", 2), Token("EOF")])

        result = Interpreter(parser, self.symbol_table).interpret()

        self.assertEqual(result, 4)

    def test_long_calc(self):
        parser = Parser([Token("INTEGER", 2), Token("PLUS"), Token("INTEGER", 2),
                        Token("MUL"), Token("INTEGER", 2), Token("EOF")])

        result = Interpreter(parser, self.symbol_table).interpret()

        self.assertEqual(result, 6)

    def test_while_loop(self):
        Interpreter(Parser([Token("IDENTIFIER", "x"), Token("ASSIGNMENT"), Token(
            "INTEGER", 0), Token("EOF")]), self.symbol_table).interpret()

        Interpreter(Parser([Token("KEYWORD", "בזמן"), Token("IDENTIFIER", "x"), Token("LT"), Token("INTEGER", 5), Token(
            "KEYWORD", "אזי"), Token("IDENTIFIER", "x"), Token("ASSIGNMENT"), Token("IDENTIFIER", "x"), Token("PLUS"), Token("INTEGER", 1), Token('KEYWORD', 'סוף'), Token("EOF")]), self.symbol_table).interpret()

        result = Interpreter(
            Parser([Token("IDENTIFIER", "x"), Token("EOF")]), self.symbol_table).interpret()
        self.assertEqual(result, 5)

    def test_if_statement(self):
        Interpreter(Parser([Token("IDENTIFIER", "x"), Token(
            "ASSIGNMENT"), Token("INTEGER", 10)]), self.symbol_table).interpret()
        Interpreter(Parser([Token("KEYWORD", "אם"), Token("IDENTIFIER", "x"), Token("GT"), Token("INTEGER", 5), Token("KEYWORD", "אזי"), Token("IDENTIFIER", "y"), Token(
            "ASSIGNMENT"), Token("INTEGER", 1), Token("KEYWORD", "אחרת"), Token("IDENTIFIER", "y"), Token("ASSIGNMENT"), Token("INTEGER", 0), Token('KEYWORD', 'סוף'), Token("EOF")]), self.symbol_table).interpret()
        result = Interpreter(
            Parser([Token("IDENTIFIER", "y"), Token("EOF")]), self.symbol_table).interpret()

        self.assertEqual(result, 1)

    def test_bool_operators(self):
        results = []
        results.append(Interpreter(Parser([Token("INTEGER", 1), Token("EQ"), Token(
            "INTEGER", 1), Token("EOF")]), self.symbol_table).interpret())

        results.append(Interpreter(Parser([Token("INTEGER", 1), Token("GT"), Token(
            "INTEGER", 0), Token("EOF")]), self.symbol_table).interpret())

        results.append(Interpreter(Parser([Token("INTEGER", 1), Token("LT"), Token(
            "INTEGER", 2), Token("EOF")]), self.symbol_table).interpret())

        results.append(Interpreter(Parser([Token("INTEGER", 1), Token("LT"), Token(
            "INTEGER", 1), Token("EOF")]), self.symbol_table).interpret())

        results.append(Interpreter(Parser([Token("INTEGER", 1), Token("GT"), Token(
            "INTEGER", 1), Token("EOF")]), self.symbol_table).interpret())

        results.append(Interpreter(Parser([Token("INTEGER", 1), Token("EQ"), Token(
            "INTEGER", 0), Token("EOF")]), self.symbol_table).interpret())

        results.append(Interpreter(Parser([Token("INTEGER", 1), Token("GTE"), Token(
            "INTEGER", 1), Token("EOF")]), self.symbol_table).interpret())

        results.append(Interpreter(Parser([Token("INTEGER", 1), Token("LTE"), Token(
            "INTEGER", 1), Token("EOF")]), self.symbol_table).interpret())

        self.assertEqual(results, [True, True, True,
                         False, False, False, True, True])


if __name__ == "__main__":
    from src.Interpreter import Interpreter
    from src.SymbolTable import SymbolTable
    from src.Parser import Parser
    from src.Token import Token
    from src.Nodes import *

    unittest.main()
