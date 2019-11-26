import numpy as np
import cv2

n = 0 
img1 = cv2.imread('0.jpg', cv2.IMREAD_GRAYSCALE) 
img2 = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE) 
height, width = img1.shape 
for line in range(height):
     
     for pixel in range(width):
         
         if img1[line][pixel] != img2[line][pixel]:
             
            n = n + 1 
print(n)

# import cv2

# import numpy as np
# image1 = './0.jpg'
# image2 = './img.png'
# image1 = cv2.imread(image1)

# image2 = cv2.imread(image2)
# difference = cv2.subtract(image1, image2)
# # if difference is all zeros it will return False
# result = not np.any(difference)


# if result is True:
#     print('same')
# else:

#     cv2.imwrite('result.jpg',difference)
#     print('different')


# from PIL import Image
# from PIL import ImageChops



# image_one = Image.open('0.jpg')
# image_two = Image.open('img.png')

# diff = ImageChops.difference(image_one, image_two)

# if diff.getbbox() is None:
#     # 图片间没有任何不同则直接退出
#     print('same') 
# else:
#     print('different')
    




