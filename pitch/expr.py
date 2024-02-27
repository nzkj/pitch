from abc import ABC, abstractmethod
from Token import Token


class Expr(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Binary(Expr):
    # def __init__(self, left: Expr, operator: Token, right: Expr):
    def __init__(self, string: str):
        # self.left = left
        # self.operator = operator
        # self.right = right
        self.string = string
    
    def accept(self, visitor):
        visitor.visit_binary()


class SomeVisitor:
    def visit_binary(self, binary: Binary):
        print(f"visited binary {binary.string}")

# define object and visitor
binary = Binary("some string")
visitor = SomeVisitor()

# run the SomeVisitor on binary
binary.accept(visitor)

