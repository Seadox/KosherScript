import unittest

import sys
import os

root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if root_folder not in sys.path:
    sys.path.insert(0, root_folder)


class TestParser(unittest.TestCase):

    def test_empty(self):
        parser = Parser([])
        tree = parser.parse()
        self.assertEqual(tree, None)

    def test_parentheses(self):
        parser = Parser([Token("LPAREN"), Token("RPAREN"), Token("EOF")])
        tree = parser.parse()
        self.assertEqual(tree, None)

    def test_parser_with_assignment_and_equality(self):
        parser = Parser([Token("ASSIGNMENT"), Token("EQ"), Token("EOF")])
        tree = parser.parse()
        self.assertEqual(tree, None)


if __name__ == "__main__":
    from src.Parser import Parser
    from src.Token import Token
    from src.Nodes import *
    unittest.main()
