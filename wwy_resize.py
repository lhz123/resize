# 2019.11.04 刘红铮
# 修改labelme_json文件夹中图片大小，
# 将原图2448*2448修改为400*400，降低内存。  

import pathlib
from PIL import Image
import os

images_root_path = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\第九批\\09_第九批\\泰国香米-2'
# path = pathlib.Path(images_root_path)
# images_path = path.glob("*/*.png")
# images_path = list(images_path)

for image_path in os.listdir(images_root_path):
# for image_path in images_path:
    images_path = os.path.join(images_root_path,image_path)
    image = Image.open(images_path)
    image = image.resize((640, 640), Image.ANTIALIAS)
    # image.save(image_path)
    image.save(images_path)
    print(images_path)

