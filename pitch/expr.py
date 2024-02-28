from abc import ABC, abstractmethod
from typing import Any
from Token import Token

# -----
# Visitor design pattern implementation
# -----
"""
Notes:
If I want to add a new operation to my expressions, `Evaluate`, I create a new object and define the operation function for each expression type.
"""

class Expr(ABC):
    @abstractmethod
    def accept(self, visitor: 'Visitor'):
        raise NotImplementedError("Subclass must implement the accept() method")

class Binary(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right
    
    def accept(self, visitor: 'Visitor') -> Any:
        visitor.visit_binary(self)

class EvaluateVisitor:
    def visit_binary(self, binary: Binary):
        # implementation of evaluate here
        pass


# -----
# A more Pythonic approach?
# -----
"""
Notes:
If I want to add a new operation to my expressions, then I simply have to add it in the class.

Python doesn't have the same issue as it supports dynamic dispatch (unlike C++, but I guess you can get similar functionality using dynamic_cast?).
 
In C++ we want to manage dependencies and be able to have functions that can be performed on any `Expr` object. We have something like `Expr->Evaluate()`, and the compiler will choose the overridden method.
However, in Python we don't need things to be passed around by specified type - we don't need to have a base `Expr` object. We have "duck typing" such that we can call a method on an object and if it has it, it will do it - "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

If we add a new operation, we don't need all child classes to implement the operation for the code to compile.

The Visitor design pattern still has the advantage of separating concerns, e.g. all evaluate functionality is in one place (object).

Bit confusing but I think I understand.

"""

class Binary:
    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right
    
    def evaluate(self):
        # implementation of evaluate here
        pass
