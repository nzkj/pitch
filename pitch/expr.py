from dataclasses import dataclass
from typing import Any, Union
from Token import Token
from tokentype import TokenType

Expr = Union['Binary', 'Grouping', 'Literal', 'Unary']

def parenthesize(name: str, *exprs: Expr) -> str:
    """Create a parenthesized string representation of the expressions."""
    string = f"({name}"
    for expr in exprs:
        string += f" {expr.print()}"
    string += ")"
    return string

@dataclass
class Binary:
    left: Expr
    operator: Token
    right: Expr

    def print(self) -> str:
        return parenthesize(self.operator.lexeme, self.left, self.right)

@dataclass
class Grouping:
    expression: Expr

    def print(self) -> str:
        return parenthesize("group", self.expression)

@dataclass
class Literal:
    value: Any

    def print(self) -> str:
        return self.value.__str__()

@dataclass
class Unary:
    operator: Token
    right: Expr

    def print(self) -> str:
        return parenthesize(self.operator.lexeme, self.right)

if __name__ == "__main__":
    print("Running")

    expression: Expr = Binary(
        Unary(
            Token(TokenType.MINUS, "-", None, 1), 
            Literal(123)
        ),
        Token(TokenType.STAR, "*", None, 1),
        Grouping(Literal(45.67))
    )
    
    print("Results")
    print(expression.print())

