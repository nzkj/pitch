import argparse

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

# This seems pretty painful and I'm not sure I can be bothered
class GenerateAST():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Generate AST tool")
        
        self.parser.add_argument('output_dir')
    
    def run(self):
        arguments = self.parser.parse_args()

        self.define_ast(arguments.output_dir, "expr", [
                        "Binary   : Expr left, Token operator, Expr right",
                        "Grouping : Expr expression",
                        "Literal  : Object value",
                        "Unary    : Token operator, Expr right"
                        ]
        )

    def define_ast(self, output_dir: str, base_name: str, ast_types: list[str]):
        path: str = f"{output_dir}/{base_name}.py"

        output = f"""
class {base_name}
    {self.define_types(base_name, ast_types)}
"""

        with open(path, 'w') as file:
            file.write(output.strip())
    
    def define_types(self, base_name: str, ast_types: list[str]):
        for ast_type in ast_types:
            elements: str = ast_type.split(":")
            class_name: str = elements[0]
            fields: str = elements[1]
            self.define_type(base_name, class_name, fields)

    def define_type(self):
        output = f"""
test
"""

if __name__ == '__main__':
    tool = GenerateAST()
    tool.run()
