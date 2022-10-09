import cv2
import hashlib


img = cv2.imread("certificate_forged.jpg")  #Enter target Image 
rows, cols, _= img.shape

print("Rows", rows)
print("Cols", cols)

#cropping
crop_img = img[0:270, 0:1118] 

hash = hashlib.md5(crop_img)
hexa = hash.hexdigest()
print(hexa)

cv2.imshow("cropped image", crop_img)


cv2.waitKey(0)
