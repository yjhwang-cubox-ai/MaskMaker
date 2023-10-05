import cv2
import numpy as np

if __name__ == "__main__":
    
    img = cv2.imread("aligned_img.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, dst = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)    
    # ret, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    # dst1 = cv2.erode(dst, kernel)
    dst1 = cv2.morphologyEx(dst, cv2.MORPH_OPEN, None)
    dst2 = cv2.dilate(dst1, kernel, iterations=10)
    
    
    cv2.imwrite("mask_morph.png", dst2)
    cv2.imshow("dst", dst1)
    cv2.imshow("dst2", dst2)
    cv2.waitKey()
    
    # src = cv2.imread("aligned_img.jpg", cv2.IMREAD_GRAYSCALE)

    # dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 5)

    # cv2.imshow('src', src)
    # cv2.imshow('dst', dst)
    # cv2.waitKey()
    # cv2.destroyAllWindows()