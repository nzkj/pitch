# Pitch

Pitch is a python implementation of a tree-walk interpreter.

## Structure of the language

Language grammar (only a subset is currently implemented, shown below)

```
expression ::= literal | unary | binary | grouping ;

literal    ::= NUMBER | STRING | "true" | "false" | "nil" ;
grouping   ::= "(" expression ")" ;
unary      ::= ( "-" | "!" ) expression ;
binary     ::= expression operator expression ;
operator   ::= "==" | "!=" | "<" | "<=" | ">" | ">=" | "+"  | "-"  | "*" | "/" ;
```

## References: 

- Crafting Interpreters - Robert Nystrom
- [Concepts of Programming Languages - Mary Elaine Califf](https://youtube.com/playlist?list=PLrB7VCHji9zj7wGQOfWNvvj691QwZ1Lam&feature=shared)
