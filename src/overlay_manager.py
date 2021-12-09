import os
import logging
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


class OverlayManager():
    """Class for handling the weather overlay
    and putting together the final image"""

    def __init__(self):
        """Instantiate the class"""
        pass

    def _get_default_font(self, size=24):
        """Returns the default font"""
        return ImageFont.truetype("fonts/Roboto-Medium.ttf", size)

    def set_bg_image(self, frame):
        """Sets the background image"""
        self.bg = Image.fromarray(frame)

    def _get_stroke_colour(self):
        """Returns the text stroke colour"""
        return (0, 0, 0)

    def _get_stroke_width(self):
        """Returns the text stroke width"""
        return 5

    def _get_fill_colour(self):
        """Returns the text fill colour"""
        return (255, 255, 255)

    def overlay_weather(self, temperature, text):
        """Overlays the weather"""
        logging.info('Overlaying weather information on image')
        title_text = str(str(temperature) + '°C - ' + text).upper()
        draw = ImageDraw.Draw(self.bg)
        title_font = self._get_default_font(100)
        tw, th = draw.textsize(title_text, font=title_font, stroke_width=self._get_stroke_width())
        position_x = (self.bg.width - tw) / 2
        position_y = (self.bg.height - th) / 2
        draw.text(
            (position_x, position_y),
            title_text,
            font=title_font,
            fill=self._get_fill_colour(),
            stroke_width=self._get_stroke_width(),
            stroke_fill=self._get_stroke_colour())
        self.final = self.bg

    def get_final_image(self):
        """Returns the final image"""
        return self.final

    def get_local_path(self):
        """Returns the local image path"""
        return '/tmp/twitter-weather.jpeg'

    def save_img_to_tmp_folder(self):
        """Returns the final file-like image object"""
        self.final.save(self.get_local_path(), "JPEG")
