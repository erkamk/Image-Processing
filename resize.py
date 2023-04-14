import cv2
import os

DATADIR = r"data dir."
PATH = r"save loc."
for img in os.listdir(DATADIR):
    original_image = cv2.imread(DATADIR + "\\" + img)
    image = cv2.resize(original_image, (700,700))
    cv2.imwrite(os.path.join(PATH , img), image)
    
