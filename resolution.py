from PIL import Image, ImageOps
import math
from time import time


class Resolution:
    def __init__(self, picture_location):
        self.picture = Image.open(picture_location)
        self.picture = self.picture.convert('RGB')
        self.picture_width, self.picture_height = self.picture.size

    def change_resolution(self, how_many_times_to_enlarge):
        new_picture_width = self.picture_width * \
            round(how_many_times_to_enlarge)
        new_picture_height = self.picture_height * \
            round(how_many_times_to_enlarge)

        changed_picture = self.__make_empty_picture(
            (new_picture_width, new_picture_height))


        surounding_pixels_array = [(0, 0) for value in range(9)]
        pixels_multidimensional_array = self.picture.load()
        pixels_to_remove_for_simplicity_of_algorithm = 2 * how_many_times_to_enlarge

        for x in range(pixels_to_remove_for_simplicity_of_algorithm, new_picture_width - pixels_to_remove_for_simplicity_of_algorithm):
            for y in range(pixels_to_remove_for_simplicity_of_algorithm, new_picture_height-pixels_to_remove_for_simplicity_of_algorithm):
                picture_coordinate_x = round(x/how_many_times_to_enlarge)
                picture_coordinate_y = round(y/how_many_times_to_enlarge)

                surounding_pixels_array[0] = pixels_multidimensional_array[picture_coordinate_x - 1,picture_coordinate_y - 1]
                surounding_pixels_array[1] = pixels_multidimensional_array[picture_coordinate_x - 1,picture_coordinate_y]
                surounding_pixels_array[2] = pixels_multidimensional_array[picture_coordinate_x - 1,picture_coordinate_y + 1]
                surounding_pixels_array[3] = pixels_multidimensional_array[picture_coordinate_x,picture_coordinate_y - 1]
                surounding_pixels_array[4] = pixels_multidimensional_array[picture_coordinate_x,picture_coordinate_y]
                surounding_pixels_array[5] = pixels_multidimensional_array[picture_coordinate_x,picture_coordinate_y + 1]
                surounding_pixels_array[6] = pixels_multidimensional_array[picture_coordinate_x + 1,picture_coordinate_y - 1]
                surounding_pixels_array[7] = pixels_multidimensional_array[picture_coordinate_x + 1,picture_coordinate_y]
                surounding_pixels_array[8] = pixels_multidimensional_array[picture_coordinate_x + 1,picture_coordinate_y + 1]
                median_pixel = self.__calculate_median_pixel(surounding_pixels_array)
                changed_picture.putpixel((x, y), median_pixel)

        return changed_picture

    def __calculate_median_pixel(self, surounding_pixels):
        red = 0
        green = 0
        blue = 0
        for pixel in surounding_pixels:
            red += pixel[0]
            green += pixel[1]
            blue += pixel[2]
        median_pixel = [round(color_value/9)
                        for color_value in [red, green, blue]]
        median_pixel = (median_pixel[0], median_pixel[1], median_pixel[2])
        return median_pixel

    def __make_empty_picture(self, size):
        return Image.new("RGB", (size), 'white')
