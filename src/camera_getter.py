import os
import logging
import time
from rtsparty import Stream


class CameraGetter():
    """Class for retrieving frames via RTSP from the camera"""
    
    def __init__(self):
        """Instantiate the class"""
        self._setup_stream()
    
    def _setup_stream(self):
        """Sets up the camera stream"""
        logging.info('Connecting to camera')
        self.stream = Stream(self._get_rtsp_url())
        logging.info('Camera connected')

    def _get_rtsp_url(self):
        """Returns the RTSP URL of the camera"""
        return os.environ['RTSP_URL']
    
    def get_current_frame(self):
        """Returns the current frame from the camera"""
        logging.info('Getting current frame')
        frame = self.stream.get_frame()
        while self.stream.is_frame_empty(frame):
            logging.debug('No frame - Waiting to get another frame')
            time.sleep(3)
            frame = self.stream.get_frame()
        return frame
