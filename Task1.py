
import cv2
import matplotlib.pyplot as plt
import numpy


image1 = cv2.imread('pic1l.jpg')
image2 = cv2.imread('pic1m.jpg')
image3 = cv2.imread('pic1d.jpg')

gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray_image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)


cv2.imshow("pic1l",gray_image1)
cv2.imshow("pic1m",gray_image2)
cv2.imshow("pic1d",gray_image3)
cv2.waitKey(0)
histogram1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
histogram2= cv2.calcHist([gray_image2], [0], None, [256], [0, 256])
histogram3 = cv2.calcHist([gray_image3], [0], None, [256], [0, 256])

plt.plot(histogram1, color='k')
cv2.imwrite("hist1.jpg",histogram1)
plt.show()
plt.plot(histogram2, color='k')
cv2.imwrite("hist2.jpg",histogram2)
plt.show()
plt.plot(histogram3, color='k')
cv2.imwrite("hist3.jpg",histogram3)
plt.show()


