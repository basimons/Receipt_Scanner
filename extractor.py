import numpy
import matplotlib.pyplot as plt

import pytesseract as pytes
import cv2 as cv
import copy


class Extractor:
    """A class that gets in an image and uses that to find a """

    def __init__(self, image: numpy.ndarray = None):
        # Initial variables that get updated later
        self.m_depth = None
        self.m_width = None
        self.m_height = None

        # The image that gets scanned
        self.m_image = image
        self.m_image_original = copy.deepcopy(image)

        # Set status
        self.m_status = "Initialized"

        # update the stats of the image
        self.update_stats()

    def reload_image(self, image: numpy.ndarray):
        self.m_image = image
        self.m_image_original = copy.deepcopy(image)
        self.update_stats()

        pass

    def update_status(self, status: str):
        self.m_status = status

    def update_stats(self):
        try:
            self.m_height, self.m_width, self.m_depth = self.m_image.shape
        except ValueError:
            self.m_depth = 1

        self.update_status("Reinitialized")

    def preprocess(self):

        if self.m_depth > 1:
            self.m_image = cv.cvtColor(self.m_image, cv.COLOR_BGR2GRAY)

        self.m_image = cv.adaptiveThreshold(self.m_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 10)

        self.update_status("Preprocessed")

        pass

    def show(self):
        cv.imshow("Status: " + self.m_status, self.m_image)
        cv.waitKey(0)

    def save(self, name: str):
        cv.imwrite(name, self.m_image)