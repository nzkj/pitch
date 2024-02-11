import argparse
from typing import List

from errorhandler import ErrorHandler
from scanner import Scanner
from Token import Token

class Pitch():
    error_handler: ErrorHandler = ErrorHandler()

    def main(self):
        parser = argparse.ArgumentParser("pitch")
        parser.add_argument("script", nargs="?", help="Run Pitch script", type=str)
        args = parser.parse_args()
        if args.script is not None:
            self.run_file(args.script)
        else:
            self.run_repl()
    
    def run_file(self, filename: str):
        print(filename)
        with open(filename, 'r') as file:
            self.run(file.read())
            
        if (self.error_handler.hadError):
            exit()

    def run_repl(self):
        print("Welcome to Pitch REPL")
        while True:
            source = input("> ")
            if (source is None):
                break
            self.run(source)
            self.error_handler.hadError = False

    def run(self, source: str):
        scanner = Scanner(source, self.error_handler)
        tokens: List[Token] = scanner.scanTokens()

        for token in tokens:
            print(token)

if __name__ == "__main__":
    pitch = Pitch()
    pitch.main()
