import cv2
import numpy as np


# img1 = cv2.imread("sonbahar.jpg")
# img2 = cv2.imread("opencv.png")

# # img2'yi img1 ile aynı boyuta yeniden boyutlandır
# img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# toplam = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)


img2 = cv2.imread("sonbahar.jpg")
img1 = cv2.imread("opencv.png")

x,y,z = img1.shape
roi = img2[0:x, 0:y]

img1_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img1_gray,10,255,cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

img2_fg = cv2.bitwise_and(img1,img1,mask=mask)

toplam = cv2.add(img1_bg,img2_fg)


img2[0:x, 0:y] = toplam

cv2.imshow("resim", img1)
cv2.imshow("resim2", toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()












