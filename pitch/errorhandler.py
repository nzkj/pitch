class ErrorHandler():
    hadError = False

    def error(self, line: int, message: str):
        self.report(line, "", message)
    
    def report(self, line: int, where: str, message: str):
        print(f"[line {line}] Error{where}: {message}")
        self.hasError = True

