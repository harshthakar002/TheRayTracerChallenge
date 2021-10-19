from typing import List
from canvas.canvas import canvas

class ppm_writer():
    
    @staticmethod
    def write_ppm_from_canvas(c: canvas) -> List:
        ppm_header = ppm_writer.write_ppm_header_data_from_canvas(c)
        ppm_text = []
        return ppm_header + ppm_text
    
    @staticmethod
    def write_ppm_header_data_from_canvas(c: canvas) -> List:
        ppm_header = ['P3']
        ppm_header.append(str(c.width) + ' ' + str(c.height))
        ppm_header.append('255')
        return ppm_header