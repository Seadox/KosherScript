class BinaryOperationNode:
    def __init__(self, left, op, right) -> None:
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self) -> str:
        return f"({self.left}, {self.op}, {self.right})"


class NumberNode:
    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"{self.value}"


class AssignmentNode:
    def __init__(self, var_name, value) -> None:
        self.var_name = var_name
        self.value = value

    def __repr__(self) -> str:
        return f"({self.var_name}, {self.value})"


class UnaryOperationNode:
    def __init__(self, operator, node) -> None:
        self.operator = operator
        self.node = node

    def __repr__(self) -> str:
        return f"({self.operator}, {self.node})"


class VariableAssignmentNode:
    def __init__(self, var_name, value) -> None:
        self.var_name = var_name
        self.value = value

    def __repr__(self) -> str:
        return f"({self.var_name}, {self.value})"


class VariableAccessNode:
    def __init__(self, var_name) -> None:
        self.var_name = var_name

    def __repr__(self) -> str:
        return f"{self.var_name}"


class IfNode:
    def __init__(self, condition, then_block, else_block=None) -> None:
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

    def __repr__(self) -> str:
        return f"{self.condition}"


class WhileNode:
    def __init__(self, condition, block) -> None:
        self.condition = condition
        self.block = block

    def __repr__(self) -> str:
        return f"{self.condition}"


class BlockNode:
    def __init__(self, children) -> None:
        self.children = children

    def __repr__(self) -> str:
        return f"{self.children}"


class MultiAssignmentNode:
    def __init__(self, assignments):
        self.assignments = assignments

    def __repr__(self):
        return f"MultiAssignmentNode({self.assignments})"


class listNode:
    def __init__(self, children) -> None:
        self.children = children

    def __repr__(self) -> str:
        return f"{self.children}"
