import json
import io
import matplotlib.pyplot as plt
import base64
import numpy as np
import PIL
from PIL import Image
import scipy.misc


def img_b64_to_arr(img_b64):
    f = io.BytesIO()
    f.write(base64.b64decode(img_b64))
    img_arr = np.array(PIL.Image.open(f))
    # print(img_arr)
    # image = img_arr.resize((640,640))
    return img_arr

# json_file = 'b.json'
# with open(json_file,'r') as f:
#     with open('b.txt','w') as fp:
        
#         js = json.load(f)
#         print(js)
#         fp.write(json.dumps(js))


# 双线性差值
def bilinear_interpolation(arr):
    src_h, src_w, channel = arr.shape
    dst_h, dst_w = 640, 640
    if src_h == dst_h and src_w == dst_w:
        return arr.copy()
    dst_img = np.zeros((dst_h,dst_w,3),dtype=np.uint8)
    scale_x, scale_y = float(src_w) / dst_w, float(src_h) / dst_h
    for i in range(3):
        for dst_y in range(dst_h):
            for dst_x in range(dst_w):
 
                # find the origin x and y coordinates of dst image x and y
                # use geometric center symmetry
                # if use direct way, src_x = dst_x * scale_x
                src_x = (dst_x + 0.5) * scale_x - 0.5
                src_y = (dst_y + 0.5) * scale_y - 0.5
 
                # find the coordinates of the points which will be used to compute the interpolation
                src_x0 = int(np.floor(src_x))
                src_x1 = min(src_x0 + 1 ,src_w - 1)
                src_y0 = int(np.floor(src_y))
                src_y1 = min(src_y0 + 1, src_h - 1)
 
                # calculate the interpolation
                temp0 = (src_x1 - src_x) * arr[src_y0,src_x0,i] + (src_x - src_x0) * arr[src_y0,src_x1,i]
                temp1 = (src_x1 - src_x) * arr[src_y1,src_x0,i] + (src_x - src_x0) * arr[src_y1,src_x1,i]
                dst_img[dst_y,dst_x,i] = int((src_y1 - src_y) * temp0 + (src_y - src_y0) * temp1)
 
    return dst_img



json_file = '0.json'
output_json_file = 'g.json'
with open(json_file,'r') as f:
      
    js = json.load(f)
    img = img_b64_to_arr(js['imageData'])
    image = bilinear_interpolation(img)
    print(image)
    # image = base64.b64decode(image)
    # print('jkbvc')
    # image = image.decodes(encoding='UTF-8')
    # print(image)
    # js['iamgeData'] = image
    with open(output_json_file, 'w') as file_out:
        file_out.write(json.dumps(image))
        file_out.close()
    # print(img)
    # plt.imshow(image)
    # plt.show()
    # print(js)
    # fp.write(json.dumps(js))







#删除json文件中imageData
# json_file = '1.json'

# def process_json(input_json_file, output_json_file):
#     file_in = open(input_json_file, 'r') #读取json文件
#     file_out = open(output_json_file, 'w') #写入json文件
#     # load数据到变量json_data
#     json_data = json.load(file_in)
#     # print (json_data)
#     # print ("after update  --->")
#     # print (type(json_data))
    
#     # 修改json中的数据
#     json_datat = json_data.pop("imageData") # 键shape的值为一个列表，且列表元素为字典
#     # print (json_data)

#     # 将修改后的数据写回文件
#     file_out.write(json.dumps(json_data))
#     # old_path = 'D:\\gree_rice_rcognition\\Mask_RCNN-master'
#     # new_path = 'D: \\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\four_five_data\\save'
#     # shutil.copyfile(os.path.join(old_path, output_json_file),
#     #                   os.path.join(new_path, output_json_file))
#     file_in.close()
#     file_out.close()

# process_json(json_file,'b.json')


