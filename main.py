import cv2 as cv
import pytesseract as pytes

import pandas as pd
import matplotlib.pyplot as plt
from extractor import Extractor

pytes.pytesseract.tesseract_cmd = "C:\\Users\\Bram\\miniconda3\\Library\\bin\\tesseract.exe"

# Read image from which text needs to be extracted
img = cv.imread("Test_Image3.jpeg")

ex = Extractor(img)

ex.preprocess()

ex.process()

ex.show()


# run tesseract, returning the bounding boxes
ocr = pytes.image_to_data(img, output_type=pytes.Output.DATAFRAME)





