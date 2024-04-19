class SymbolTable:
    def __init__(self) -> None:
        self.symbols = {}

    def get(self, name):
        value = self.symbols.get(name)
        if value == None:
            print(f"Variable '{name}' not defined")
            return None
        return value

    def set(self, name, value):
        self.symbols[name] = value

    def remove(self, name):
        self.symbols.pop(name)

    def __repr__(self) -> str:
        return str(self.symbols)
