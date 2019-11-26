import cv2
import numpy as np
image = cv2.imread('./test/0.jpg')
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5) #画线
# cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)#画矩形框，左下角坐标和右上角坐标
# cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)  #画圆
# cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2) #在图片中写字，name font is not defined

# image = image[15:150,15:150] #对图片进行裁剪

b, g, r = cv2.split(image) #图片拆分
# img = cv2.merge(b, g, r) #图片合并


cv2.imshow('image',r)

cv2.waitKey(0)
cv2.destroyAllWindows()
