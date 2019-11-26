
import matplotlib.pyplot as plt
from skimage import transform
import numpy as np
import skimage.io as io
from PIL import Image
import os
import matplotlib.image as mpimg
import imghdr
import glob
import os.path
import shutil
import pathlib
# import opencv
# image_dir = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\labelme_json\\'
# file_name = os.listdir(image_dir)

# for i, name in enumerate(file_name):
#     image_path = image_dir + name +'\\'
#     # print(image_path)
#     for img in os.listdir(image_path):
#         # print(img)
#         if img in ('label.png','img.png','label_viz.png'):
#             image = Image.open(image_path+img)
#             image = image.resize((640, 640), Image.ANTIALIAS)
#             image.save(image_path+img)




# image_dir = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\第七批数据图片\\121_五常黑米\\pic'
# images = Image.open(image_dir+img)
# images = images.resize((400, 400), Image.ANTIALIAS)
# images.save(image_dir+img)

#挑出json文件中的缺少的文件名
# json_dir = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\第七批数据图片\\004_五常大米金镰刀\\json'
# image_dir = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\第七批数据图片\\004_五常大米金镰刀\\pic'
# arr=[]
# arr1=[]
# for img in os.listdir(image_dir):
#     index = img.rfind('.')
#     name = img[:index]
#     arr.append(name)
# for json in os.listdir(json_dir):
#     index = json.rfind('.')
#     json_name = json[:index]
#     arr1.append(json_name)

# for i in range(len(arr)):
#     if arr[i] not in arr1:
#         print(arr[i])   
    


#剪切文件到另一个文件夹

image_dir = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\第九批\\09_第九批\\泰国香米-2'

json_dir = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\nine_data\\new-2\\pic'

for images in os.listdir(image_dir):
    index = images.rfind('.')
    image_name = images[index:]

    if image_name == '.jpg':
        image = os.path.join(image_dir,images)
        # shutil.move(image,json_dir) #剪切
        shutil.copy(image, json_dir)  # 复制


# 复制json文件到另一个文件夹中
# images_root_path = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\new_data-4\\113_大别山红米'

# jsons_dir = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\new_data\\113_大别山红米\\json'

# json_dir = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\new_data-4\\113_大别山红米\\json'


# for image in os.listdir(images_root_path):
#     index = image.rfind('.')
#     image_name = image[:index]
#     json_name = image_name + '.json'
#     # print(json_name)
#     jsons_name = os.path.join(jsons_dir, json_name)
#     if os.path.exists(jsons_name):
    
#         shutil.copy(jsons_name,json_dir)
#     else:
#         pass

#复制图片到另一个文件夹
# images_root_path = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\第七批数据图片\\004_五常大米金镰刀\\4_red_7.8cm_single'

# # jsons_dir = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\new_data-4\\004_五常大米金镰刀\\json'

# image_save_dir = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\第七批数据图片\\004_五常大米金镰刀\\4_pic'

# for image in os.listdir(images_root_path):
#     index = image.rfind('.')
#     name = image[:index]
#     json_name = name + '.json'
#     json = os.path.join(jsons_dir, json_name)
#     image_dir = os.path.join(images_root_path,image)
#     if os.path.exists(json):
#         pass
#     else:
#         # print(image_dir)
#         shutil.copy(image_dir, image_save_dir)


#删除文件夹汇总的某些子文件夹

# fold_path = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\新数据集\\data1\\labelme_json'
# image_name_path = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\新数据集\\data1\\pic'
# new_path = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\新数据集\\data1\\a'
# for image_name in os.listdir(image_name_path):
#     index = image_name.rfind('.')
#     name = image_name[:index]
#     fold_name = name + '_json'
#     # print(fold_name)
#     fold_dir = os.path.join(fold_path, fold_name)
#     shutil.move(fold_dir,new_path)
    # if os.path.exists(fold_path):
    #     pass
    # else:
    #     print(fold_name)
    #     shutil.rmtree(fold_path)
    #     # del fold_path


        
    
#删除文件夹中的某些图片或文件夹

# images_path = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\第七批数据图片\\002_丰两优香1号米\\2_blue_7.8cm_single'

# image_dir = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\新数据集\\data1\\pic'



# for image in os.listdir(images_path):
#     images_dir = os.path.join(image_dir,image)
#     if os.path.exists(images_dir):
#         os.remove(images_dir)
#     else:
#         pass

