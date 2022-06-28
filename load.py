import cv2
img=cv2.imread("Screenshot 2021-08-25 100229.png",1)

#print(img)

#print(img.shape)

cv2.imshow("ayush",img)
cv2.waitKey(0)
cv2.destroyAllWindows()