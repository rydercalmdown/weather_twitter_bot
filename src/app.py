import os
import time
import logging
import cv2
import numpy as np

from camera_getter import CameraGetter
from overlay_manager import OverlayManager
from weather_getter import WeatherGetter
from twitter_manager import TwitterManager


class WeatherTwitterBot():
    """Class for managing the weather twitter bot"""

    def __init__(self):
        self.cg = CameraGetter()
        self.om = OverlayManager()
        self.wg = WeatherGetter()
        self.tm = TwitterManager()

    def _show_image_preview(self, image):
        """Shows a preview of the image"""
        image = np.uint8(image)
        cv2.imshow('image', image)
        cv2.waitKey(0)

    def run(self):
        """Run the application"""
        # Get the current frame
        frame = self.cg.get_current_frame()
        if str(type(frame)) == str(type(None)):
            logging.error('No frame detected')
            return
        # Get the current weather
        self.wg.get_weather()
        temp = self.wg.temp
        desc = self.wg.description
        if temp is None:
            logging.error('No temp')
            return
        if desc is None:
            logging.error('No Desc')
            return
        # Overlay the weather on the image
        self.om.set_bg_image(frame)
        self.om.overlay_weather(temp, desc)
        final_image = self.om.get_final_image()
        self.om.save_img_to_tmp_folder()
        # Post to twitter
        logging.info('Posting to twitter')
        self.tm.post_to_twitter(self.om.get_local_path(), "Today's Weather")

    def run_cron(self):
        """Runs the application on a loop"""
        try:
            while True:
                self.run()
                time.sleep(86400)
        except KeyboardInterrupt:
            print('Exiting')


if __name__ =="__main__":
    logging.basicConfig(level=logging.DEBUG)
    wtb = WeatherTwitterBot()
    wtb.run()
