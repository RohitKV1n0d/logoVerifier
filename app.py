import cv2
import hashlib

fake_img = cv2.imread("fake.jpg")
og_img = cv2.imread("Test_temp.jpg")  
test_img = cv2.imread("OG_certificate.jpg")  #  <--------- Enter target Image

rows_og, cols_og, _= og_img.shape
rows_test, cols_test, _= test_img.shape

crop_og_img = og_img[0:270, 0:1118] 
corp_test_img = test_img[0:270, 0:1118] 
fake_img = cv2.resize(fake_img,(1118,790))

def hasher(img):
    hash = hashlib.md5(img)
    hexa = hash.hexdigest()
    return hexa

def verifier(og,test):
    if(og == test):
        return print("Verified and Original!!!")
    else:
        fake_final = cv2.addWeighted(fake_img,0.5, test_img,0.5,0)
        cv2.imshow("Forged image", fake_final)
        cv2.waitKey(0)
        return print("Forged!!")
        


def main():
    og_digest = hasher(crop_og_img)
    test_digest = hasher(corp_test_img)

    verifier(og_digest, test_digest)

main()