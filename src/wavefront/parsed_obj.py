class ParsedObj():

    def __init__(self) -> None:
        self.processed = 0
        self.ignored = 0
    

    def ignore(self) -> None:
        self.ignored += 1