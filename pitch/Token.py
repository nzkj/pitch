from tokentype import TokenType

class Token():
    token_type: TokenType
    lexeme: str
    literal: object
    line: int

    def __init__(self, token_type: TokenType, lexme: str, literal: object, line: int):
        self.token_type = token_type
        self.lexeme = lexme
        self.literal = literal
        self.line = line
    
    def __str__(self) -> str:
        return self.token_type.__str__() + ", " + self.lexeme + ", " + self.literal.__str__();

