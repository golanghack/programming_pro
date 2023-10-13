#! /usr/bin/env python3 

import cv2

picture = cv2.imread('simple.jpg')
cv2.imshow('Start image -> ', picture)
cv2.waitKey(-1)
cv2.destroyAllWindows()

def mutation_picture(picture, x):
    cv2.namedWindow(x, cv2.WINDOW_NORMAL)
    cv2.imshow(x, picture)
    cv2.waitKey(-1)
    cv2.destroyAllWindows()

#mutation_picture(picture [1500:800, 48:30], 'Cutting')   

change_size = (int(picture.shape[1] * 40 / 100), int(picture.shape[0] * 40 / 100))

mutation_picture(cv2.resize(picture, change_size, interpolation=cv2.INTER_AREA), 
                                'Changed size on 40%')

(hight, width, drow) = picture.shape
c = (width // 2, hight // 2)
mutation_picture(cv2.warpAffine(picture, cv2.getRotationMatrix2D(c, 45, 1), (width, hight)), 'Turn on 45 %')

copy_image = picture.copy()
cv2.line(copy_image, (810, 810), (110, 100), (10, 15, 255), 8)
mutation_picture(copy_image, 'Line')

copy_image_update = picture.copy()
cv2.putText(copy_image_update, 'WOW', (400, 400), cv2.FONT_HERSHEY_COMPLEX_SMALL, 9, (20, 205, 216), 25)
mutation_picture(copy_image_update, 'With text')