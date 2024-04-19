from src.Lexer import Lexer
from src.Parser import Parser
from src.Interpreter import Interpreter
from src.SymbolTable import SymbolTable


def main():
    symbol_table = SymbolTable()
    symbol_table.set("True", 1)
    symbol_table.set("False", 0)
    symbol_table.set("PI", 3.141592653589793)

    banner = '''
  _  __         _               _____           _       _
 | |/ /        | |             / ____|         (_)     | |
 | ' / ___  ___| |__   ___ _ _| (___   ___ _ __ _ _ __ | |_
 |  < / _ \/ __| '_ \ / _ \ '__\___ \ / __| '__| | '_ \| __|
 | . \ (_) \__ \ | | |  __/ |  ____) | (__| |  | | |_) | |_
 |_|\_\___/|___/_| |_|\___|_| |_____/ \___|_|  |_| .__/ \__|
                                                 | |
                                                 |_|
    '''

    print(banner)

    while True:
        text = input(">>> ")
        if text == "צא":
            break
        lexer = Lexer(text)
        tokens = lexer.create_tokens()
        parser = Parser(tokens)
        interpreter = Interpreter(parser, symbol_table)
        result = interpreter.interpret()

        if type(result) == list:
            for r in result:
                print(r)
        else:
            if result != None:
                print(result)


if __name__ == "__main__":
    main()
