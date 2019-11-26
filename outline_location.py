import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

image = './test/7.jpg'
new_name = 'a.jpg'
savefile = './test'
# image = os.listdir(image_file)
save_image = os.path.join(savefile, new_name)

img = cv2.imread(image)
width = img.shape[1]
height = img.shape[0]
x = max(width, height)
img = cv2.copyMakeBorder(img, int((x-height)/2), int((x-height)/2),
                         int((x-width)/2), int((x-width)/2), cv2.BORDER_CONSTANT, value=0)

image = cv2.resize(img, (1000, 1000), interpolation=cv2.INTER_LANCZOS4)

img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

img = cv2.medianBlur(img, 5)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 200,
                           param1=70, param2=40, minRadius=200, maxRadius=400)

# print(len(circles[0])
if np.all(circles == None):
    print('fv')
else:

    x = circles[0][0][0]
    y = circles[0][0][1]
    r = circles[0][0][2]
    # cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)
    cv2.imwrite(save_image,image)
    image = image[int(y-r)-10:int(y+r)+10,int(x-r)-10:int(x+r)+10]
cv2.imshow('detected circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

