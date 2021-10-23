from typing import List
from canvas.canvas import Canvas
from features.color import Color

PIXEL_ROW_LENGTH = 70
COLOR_MAX_VALUE = 255

class PPMWriter():
    
    @staticmethod
    def write_ppm_from_canvas(c: Canvas) -> List:
        return PPMWriter.write_ppm_header_data_from_canvas(c) + PPMWriter.write_ppm_pixel_data_from_canvas(c) + ['']
    
    @staticmethod
    def write_ppm_header_data_from_canvas(c: Canvas) -> List:
        ppm_header = ['P3']
        ppm_header.append(str(c.width) + ' ' + str(c.height))
        ppm_header.append(str(COLOR_MAX_VALUE))
        return ppm_header
    
    @staticmethod
    def write_ppm_pixel_data_from_canvas(c: Canvas) -> list[str]:
        return PPMWriter.convert_pixels_to_ppm_lines(c.pixels)

    @staticmethod
    def convert_color_to_ppm_string(col: Color) -> str:
        return ' '.join([str(PPMWriter.normalize_color_value(col.red)), str(PPMWriter.normalize_color_value(col.green)), str(PPMWriter.normalize_color_value(col.blue))])

    @staticmethod
    def normalize_color_value(color_value: float) -> int:
        if color_value > 1:
            color_value = 1
        if color_value < 0:
            color_value = 0
        return round(255 * color_value)
    
    @staticmethod
    def convert_pixels_to_ppm_lines(pixels: list[list[Color]]) -> list[str]:
        current_row_length = 0
        ppm_lines = []
        pixel_strings = []
        for pixel_row in pixels:
            for pixel in pixel_row:
                pixel_string = PPMWriter.convert_color_to_ppm_string(pixel)
                if current_row_length + len(pixel_string) > PIXEL_ROW_LENGTH:
                    ppm_lines.append(' '.join(pixel_strings))
                    pixel_strings = []
                    current_row_length = 0
                pixel_strings.append(pixel_string)
                current_row_length += len(pixel_string) + 1
            ppm_lines.append(' '.join(pixel_strings))
            pixel_strings = []
            current_row_length = 0
        return ppm_lines