from wavefront.parsed_obj import ParsedObj


class ObjParser():

    def __init__(self, filename: str) -> None:
        if filename == None:
            raise ValueError('Filename cannot be none')
        self.filename = filename
    
    def parse(self) -> ParsedObj: 
        if self.filename == None:
            raise ValueError('Filename cannot be none')
        parsed_obj = ParsedObj()
        with open(self.filename, 'r') as obj_file:
            for line in obj_file:
                self.parse_line(line, parsed_obj)
        
        return parsed_obj

    def parse_line(self, line: str, parsed_obj: ParsedObj) -> None:
        parsed_obj.ignore()        