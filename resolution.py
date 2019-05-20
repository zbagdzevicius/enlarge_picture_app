from PIL import Image, ImageOps
import math
from time import time


class Resolution:
    def __init__(self, picture_location):
        self.picture = Image.open(picture_location)
        self.picture_width, self.picture_height = self.picture.size

    def change_resolution(self, how_many_times_to_enlarge):
        new_picture_width = self.picture_width * \
            round(how_many_times_to_enlarge)
        new_picture_height = self.picture_height * \
            round(how_many_times_to_enlarge)

        changed_picture = self.__make_empty_picture(
            (new_picture_width, new_picture_height))
        surounding_pixels = [(0, 0) for value in range(9)]
        for x in range(new_picture_width):
            for y in range(new_picture_height):
                try:
                    picture_coordinate_x = round(x/how_many_times_to_enlarge)
                    picture_coordinate_y = round(y/how_many_times_to_enlarge)

                    surounding_pixels[0] = self.picture.getpixel(
                        (picture_coordinate_x - 1, picture_coordinate_y - 1))
                    surounding_pixels[1] = self.picture.getpixel(
                        (picture_coordinate_x - 1, picture_coordinate_y))
                    surounding_pixels[2] = self.picture.getpixel(
                        (picture_coordinate_x - 1, picture_coordinate_y + 1))
                    surounding_pixels[3] = self.picture.getpixel(
                        (picture_coordinate_x,   picture_coordinate_y - 1))
                    surounding_pixels[4] = self.picture.getpixel(
                        (picture_coordinate_x, picture_coordinate_y))
                    surounding_pixels[5] = self.picture.getpixel(
                        (picture_coordinate_x, picture_coordinate_y + 1))
                    surounding_pixels[6] = self.picture.getpixel(
                        (picture_coordinate_x + 1, picture_coordinate_y - 1))
                    surounding_pixels[7] = self.picture.getpixel(
                        (picture_coordinate_x + 1, picture_coordinate_y))
                    surounding_pixels[8] = self.picture.getpixel(
                        (picture_coordinate_x + 1, picture_coordinate_y + 1))

                    median_pixel = self.__calculate_median_pixel(surounding_pixels)
                    changed_picture.putpixel((x, y), median_pixel)
                except:
                    pass

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
