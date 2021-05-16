import argparse
import cv2
import pytesseract
from pytesseract import Output
import numpy as np
from numpy import asarray
#ap = argparse.ArgumentParser()
#p.add_argument("-i" , "--testID.jpg" , help = "path to input image to be OCR'd", default = "stdout")
#ap.add_argument ("-o" , "--output" , help = "path to the output CSV file")
#ap.add_argument("-c" , "--min conf" , help = "minimum confidence value to filter weak text detection")
#ap.add_argument("-d" , "--dist-thresh" , type = float , default = 25.0)
#ap.add_argument("-s", "--min-size", type = int, default = 2 , help = "minimum cluster size")

#args = vars(ap.parse_args())
#np.random.seed(42)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
custom_config = r' --oem 3 --psm 11'
images = cv2.imread(r"C:\Users\King alagbe\Downloads\testID.jpg")
images = cv2.cvtColor(images, cv2.COLOR_BGR2RGB)
height, width, t = images.shape
boxes = pytesseract.image_to_data(images , config= custom_config)

print(boxes)
for x, b in enumerate(boxes.splitlines()):
    if x!=0:
    #print(b) 
     b =b.split()
     print(b) 
     if len(b) == 12:
      x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
      cv2.rectangle(images, (x, y), (w + x, h + y),(225,0,0), 2)
      cv2.putText(images, b[11], (x,y), cv2.FONT_HERSHEY_COMPLEX,0.3,(50,50,255), 1)
      

cv2.imshow("Result", images)
cv2.waitKey(0)
