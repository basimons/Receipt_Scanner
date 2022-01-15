import numpy
import pandas as pd

import pytesseract as pytes
import cv2 as cv
import copy


class Extractor:
    """A class that gets in an image and uses that to find a """

    def __init__(self, image: numpy.ndarray = None) -> None:
        # Initial variables that get updated later
        self.m_depth = None
        self.m_width = None
        self.m_height = None

        self.m_ocr = pd.DataFrame()

        # The image that gets scanned
        self.m_image = image
        self.m_image_original = copy.deepcopy(image)

        # Set status
        self.m_status = "Initialized"

        # update the stats of the image
        self.update_stats()

    def reload_image(self, image: numpy.ndarray) -> None:
        self.m_image = image
        self.m_image_original = copy.deepcopy(image)
        self.update_stats()


    def update_status(self, status: str) -> None:
        self.m_status = status

    def update_stats(self) -> None:
        try:
            self.m_height, self.m_width, self.m_depth = self.m_image.shape
        except ValueError:
            self.m_depth = 1

        self.update_status("Reinitialized")

    def preprocess(self) -> None:
        # If RGB convert to Grayscale
        if self.m_depth > 1:
            self.m_image = cv.cvtColor(self.m_image, cv.COLOR_BGR2GRAY)

        # Apply adaptive thresholding
        self.m_image = cv.adaptiveThreshold(self.m_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 10)

        # Update status
        self.update_status("Preprocessed")


    def process(self) -> None:
        self.m_ocr = pytes.image_to_data(self.m_image, output_type=pytes.Output.DATAFRAME)
        self.m_ocr = self.m_ocr.dropna()


        print(pytes.image_to_string(self.m_image))



    def basic_check(self) -> list:
        items = []
        """Basic check if no stores are known"""
        for text in self.m_ocr['text']:
            # A comma or a point detected, so most likely a price is printed here
            if "," or "." in text:
                print('comma found')
            else:
                print("No values detected")


        return items


    def store_check(self):
        """Do a check if the store can be found, if so the """
        stores = ["albert heijn", "jumbo", "hema", "dirk"]



    def show(self) -> None:
        cv.imshow("Status: " + self.m_status, self.m_image)
        cv.waitKey(0)

    def save(self, name: str) -> None:
        cv.imwrite(name, self.m_image)
