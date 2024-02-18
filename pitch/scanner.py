from typing import List

from errorhandler import ErrorHandler
from Token import Token
from tokentype import TokenType

class Scanner():
    source: str
    error_handler: ErrorHandler

    tokens: List[Token] = []
    start: int = 0
    current: int = 0
    line: int = 1

    keywords = {
        "and": TokenType.AND,
        "class": TokenType.CLASS,
        "else": TokenType.ELSE,
        "false": TokenType.FALSE,
        "for": TokenType.FOR,
        "fun": TokenType.FUN,
        "if": TokenType.IF,
        "nil": TokenType.NIL,
        "or": TokenType.OR,
        "print": TokenType.PRINT,
        "return": TokenType.RETURN,
        "super": TokenType.SUPER,
        "this": TokenType.THIS,
        "true": TokenType.TRUE,
        "var": TokenType.VAR,
        "while": TokenType.WHILE
    }

    def __init__(self, source: str, error_handler: ErrorHandler):
        self.source = source
        self.error_handler = error_handler

    def scanTokens(self) -> List[Token]:
        while(not self.at_end()):
            self.start = self.current
            self.scanToken()
        
        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def at_end(self) -> bool:
        print("At " + self.source[self.current] + " end: " + str(self.current) + ">=" + str(len(self.source)-1))
        booleam = self.current >= len(self.source)-1
        print(booleam)
        return booleam

    def scanToken(self) -> None:
        c: str = self.advance()
        print("scanning token: " + c)
        match c:
            case '(':
                self.add_token(TokenType.LEFT_PAREN)
            case ')':
                self.add_token(TokenType.RIGHT_PAREN)
            case '{':
                self.add_token(TokenType.LEFT_BRACE)
            case '}':
                self.add_token(TokenType.RIGHT_BRACE)
            case ',':
                self.add_token(TokenType.COMMA)
            case '.':
                self.add_token(TokenType.DOT)
            case '-':
                self.add_token(TokenType.MINUS)
            case '+':
                self.add_token(TokenType.PLUS)
            case ';':
                self.add_token(TokenType.SEMICOLON)
            case '*':
                self.add_token(TokenType.STAR)
            case '!':
                self.add_token(TokenType.BANG_EQUAL if self.pair('=') else TokenType.BANG)
            case '=':
                self.add_token(TokenType.EQUAL_EQUAL if self.pair('=') else TokenType.EQUAL)
            case '<':
                self.add_token(TokenType.LESS_EQUAL if self.pair('=') else TokenType.LESS)
            case '>':
                self.add_token(TokenType.GREATER_EQUAL if self.pair('=') else TokenType.GREATER_EQUAL)
            case '/':
                if self.pair('/'):
                    while self.peek() != '/n' and not self.at_end():
                        self.advance()
                else:
                    self.add_token(TokenType.SLASH)
            
            # Ignore whitespace
            case ' ':
                pass
            case '\r':
                pass
            case '\t':
                pass

            case '\n':
                self.line += 1

            case '"':
                self.scan_string()
            
            case _:
                if self.is_digit(c):
                    self.scan_number()
                elif self.is_alpha(c):
                    self.scan_identifier()
                else:
                    self.error_handler.error(self.line, "Unexpected character.")
    
    def scan_identifier(self) -> None:
        while self.is_alpha_numeric(self.peek()):
            self.advance()
        text: str = self.source[self.start:self.current+1]
        print("Trying: " + text)
        if text in self.keywords:
            token_type: TokenType = self.keywords[text]
        else:
            token_type = TokenType.IDENTIFIER
        self.add_token(token_type)

    # Single character only
    def is_alpha(self, c: str) -> bool:
        return c.isalpha() or c == '_'
    
    # Single character only
    def is_digit(self, c: str) -> bool:
        return c.isdigit()
    
    def is_alpha_numeric(self, c: str) -> bool:
        return self.is_alpha(c) or self.is_digit(c)

    def scan_string(self) -> None:
        while self.peek() != '"' and not self.at_end():
            if self.peek() == '\n':
                self.line += 1
            self.advance()
        
        if self.at_end():
            self.error_handler.error(self.line, "Unterminated string.")
            return
        
        # Advance through closing "
        self.advance()

        self.add_token(TokenType.STRING, self.source[self.start+1:self.current-1]) # fix slice
    
    def scan_number(self) -> None:
        while self.is_digit(self.peek()):
            self.advance()
            
        # Look for a decimal part
        if self.peek() == '.' and self.is_digit(self.doublePeek()):
            self.advance()

            while self.is_digit(self.peek()):
                self.advance()

        self.add_token(TokenType.NUMBER, float(self.source[self.start:self.current+1]))

    def doublePeek(self) -> str:
        if self.current + 1 >= len(self.source):
            return '\0'
        return self.source[self.current + 1]

    def pair(self, expected: str) -> bool:
        if self.at_end():
            return False
        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True
    
    def peek(self) -> str:
        if self.at_end():
            return '\0'
        return self.source[self.current]
        

    def advance(self) -> str:
        char: str = self.source[self.current]
        self.current += 1
        return char

    def add_token(self, token_type: TokenType, literal: object = None) -> None:
        text: str = self.source[self.start:self.current+1]
        self.tokens.append(Token(token_type, text, literal, self.line));
