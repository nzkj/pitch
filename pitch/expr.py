from abc import ABC, abstractmethod
from Token import Token

class Expr(ABC):
    @abstractmethod
    def accept(self):
        pass

class Binary(Expr):
    left: Expr
    operator: Token
    right: Expr

    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right
