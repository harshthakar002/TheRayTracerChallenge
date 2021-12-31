from typing import List
from wavefront.parsed_obj import ParsedObj


class ObjParser():

    DELIMITER = ' '
    VERTEX_KEY = 'v'
    FACE_KEY = 'f'
    GROUP_KEY = 'g'
    VERTEX_NORMAL_KEY = 'vn'

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
        line_components = line.split(ObjParser.DELIMITER)
        if len(line_components) == 0:
            parsed_obj.ignore()
            return

        if line_components[0] == ObjParser.VERTEX_KEY:
            self.parse_vertex_line(line_components, parsed_obj)        
        elif line_components[0] == ObjParser.FACE_KEY:
            self.parse_face_line(line_components, parsed_obj)
        elif line_components[0] == ObjParser.GROUP_KEY:
            self.parse_group_line(line_components, parsed_obj)
        elif line_components[0] == ObjParser.VERTEX_NORMAL_KEY:
            self.parse_vertex_normal_line(line_components, parsed_obj)
        else:
            parsed_obj.ignore()
    
    def parse_vertex_line(self, line_components: List[str], parsed_obj: ParsedObj) -> None:
        if len(line_components) != 4:
            parsed_obj.ignore()
            return
        x, y, z = float(line_components[1]), float(line_components[2]), float(line_components[3])
        parsed_obj.add_vertex(x, y, z)
        parsed_obj.mark_processed()
    
    def parse_face_line(self, line_components: List[str], parsed_obj: ParsedObj) -> None:
        if len(line_components) < 4:
            parsed_obj.ignore()
            return
        vertice_indices = []
        for component in line_components[1:]:
            vertice_indices.append(component.split('/'))
        for i in range(1, len(vertice_indices) - 1):
            n1_index, n2_index, n3_index = None, None, None
            if len(vertice_indices[0]) >= 3:
                n1_index = int(vertice_indices[0][2])
            if len(vertice_indices[i]) >= 3:
                n2_index = int(vertice_indices[i][2])
            if len(vertice_indices[i+1]) >= 3:
                n3_index = int(vertice_indices[i+1][2])
            parsed_obj.add_triangle(int(vertice_indices[0][0]), int(vertice_indices[i][0]), int(vertice_indices[i + 1][0]), n1_index, n2_index, n3_index)
        parsed_obj.mark_processed()
    
    def parse_group_line(self, line_components: List[str], parsed_obj: ParsedObj) -> None:
        if len(line_components) < 2:
            parsed_obj.ignore()
            return
        name = ' '.join(line_components[1:])
        parsed_obj.add_group(name.strip())
        parsed_obj.mark_processed()
    
    def parse_vertex_normal_line(self, line_components: List[str], parsed_obj: ParsedObj) -> None:
        if len(line_components) < 4:
            parsed_obj.ignore()
            return
        x, y, z = float(line_components[1]), float(line_components[2]), float(line_components[3])
        parsed_obj.add_normal(x, y, z)
        parsed_obj.mark_processed()