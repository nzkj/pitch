from abc import ABC, abstractmethod

# Example we want to create
"""
Questions:
Is using the visitor design pattern suited for a Python implementation?


`Expr` is the base class for all expression classes.
    Contains accept(), and all visitors

Java implementation:
    package com.craftinginterpreters.lox;

    abstract class Expr { 
      static class Binary extends Expr {
        Binary(Expr left, Token operator, Expr right) {
          this.left = left;
          this.operator = operator;
          this.right = right;
        }

        final Expr left;
        final Token operator;
        final Expr right;
      }

      // Other expressions...
    }

How can this be transferred to Python, potentially a functional implementation rather than a visitor?

"""

