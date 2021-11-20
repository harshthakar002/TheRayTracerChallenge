from patterns.pattern import Pattern

class TwoPatternedPattern(Pattern):

    def __init__(self, pattern1: Pattern, pattern2: Pattern) -> None:
        self.pattern1 = pattern1
        self.pattern2 = pattern2
        super().__init__()