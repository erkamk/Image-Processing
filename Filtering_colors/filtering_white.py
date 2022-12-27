import cv2
import numpy as np

image = cv2.imread("/file_path_here")
scale_percent = 15 
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized non-filtered image", resized)

lower = np.array([0,0,0])
upper = np.array([230,230,230])

hsv = cv2.cvtColor(resized, cv2.COLOR_RGB2HSV)
mask = cv2.inRange(hsv, lower, upper)
filtered = cv2.bitwise_and(resized, resized, mask=mask)

cv2.imshow("Mask", mask)
cv2.imshow("Filtered", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
